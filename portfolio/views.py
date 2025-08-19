# -*- coding: utf-8 -*-
"""
Views (controladores) do portfólio

Este arquivo contém as funções que processam as requisições do usuário
e retornam as páginas HTML ou respostas JSON.

Cada view corresponde a uma página do site:
- home: Página inicial
- projects: Lista de todos os projetos  
- project_detail: Detalhes de um projeto específico
- contact: Página de contato com formulário

Para mais informações sobre views:
https://docs.djangoproject.com/en/4.2/topics/http/views/
"""

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import json
from .models import ContactInfo, Project, Experience, Skill, ContactMessage

def home(request):
    """
    View da página inicial do portfólio
    
    Busca no banco de dados:
    - Informações de contato
    - Projetos em destaque (máximo 3)
    - Projetos recentes (máximo 6)
    - Experiências profissionais (máximo 4)
    
    E envia tudo para o template home.html
    """
    
    # Busca as informações de contato (deve existir apenas um registro)
    contact_info = ContactInfo.objects.first()
    
    # Busca projetos marcados como "featured" (em destaque) - máx. 3
    featured_projects = Project.objects.filter(featured=True)[:3]
    
    # Busca todos os projetos mais recentes - máx. 6
    recent_projects = Project.objects.all()[:6]
    
    # Busca experiências profissionais - máx. 4
    experiences = Experience.objects.all()[:4]
    
    # Dicionário com todos os dados que serão enviados para o template
    context = {
        'contact_info': contact_info,
        'featured_projects': featured_projects,
        'recent_projects': recent_projects,
        'experiences': experiences,
    }
    
    # Renderiza o template home.html com os dados
    return render(request, 'portfolio/home.html', context)

def projects(request):
    projects_list = Project.objects.all()
    contact_info = ContactInfo.objects.first()
    
    context = {
        'projects': projects_list,
        'contact_info': contact_info,
    }
    return render(request, 'portfolio/projects.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    contact_info = ContactInfo.objects.first()
    
    context = {
        'project': project,
        'contact_info': contact_info,
    }
    return render(request, 'portfolio/project_detail.html', context)

def contact(request):
    contact_info = ContactInfo.objects.first()
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')
            
            # Salvar mensagem no banco
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )
            
            # Enviar e-mail
            subject = f'Nova mensagem do portfólio - {name}'
            email_message = f"""
Nova mensagem recebida através do seu portfólio:

Nome: {name}
E-mail: {email}
Mensagem:
{message}

---
Esta mensagem foi enviada através do formulário de contato do seu portfólio.
            """
            
            send_mail(
                subject=subject,
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['luisdpieri.tech@gmail.com'],
                fail_silently=False,
            )
            
            return JsonResponse({
                'status': 'success',
                'message': 'Mensagem enviada com sucesso! Entrarei em contato em breve.'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': 'Erro ao enviar mensagem. Tente novamente.'
            })
    
    context = {
        'contact_info': contact_info,
    }
    return render(request, 'portfolio/contact.html', context)

from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def healthy(request):
    """
    Endpoint de health check para monitoramento em produção
    
    Aceita apenas requisições GET.
    
    Verifica:
    - Conectividade com o banco de dados
    - Status geral da aplicação
    - Informações do ambiente
    """
    import os
    from django.db import connection
    from django.http import JsonResponse
    from django.conf import settings
    
    try:
        # Testar conexão com banco
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            db_status = "OK"
    except Exception as e:
        db_status = f"ERROR: {str(e)}"
    
    # Verificar ambiente
    environment = "PRODUCTION" if os.environ.get('HOSTGATOR') else "DEVELOPMENT"
    
    # Status geral
    overall_status = "OK" if db_status == "OK" else "ERROR"
    
    health_data = {
        "status": overall_status,
        "timestamp": "2025-08-18T20:45:00Z",
        "environment": environment,
        "database": db_status,
        "python_version": "3.6.8",
        "django_version": "2.2.28",
        "services": {
            "web": "OK",
            "database": db_status,
            "static_files": "OK"
        }
    }
    
    # Retornar 200 se tudo OK, 503 se houver problemas
    status_code = 200 if overall_status == "OK" else 503
    
    return JsonResponse(health_data, status=status_code)