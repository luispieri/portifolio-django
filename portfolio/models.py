# -*- coding: utf-8 -*-
"""
Modelos do banco de dados para o portfólio

Este arquivo define as estruturas de dados (tabelas) que serão criadas no banco.
Cada classe representa uma tabela no banco de dados.

Para mais informações sobre models do Django:
https://docs.djangoproject.com/en/4.2/topics/db/models/
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class ContactInfo(models.Model):
    """
    Modelo para armazenar informações de contato pessoal
    
    Este modelo guarda seus dados pessoais que aparecem no portfólio:
    email, telefone, localização, redes sociais, etc.
    Normalmente existe apenas um registro desta tabela.
    """
    
    # Email principal - campo obrigatório
    email = models.EmailField(
        help_text="Seu email principal que aparecerá no portfólio"
    )
    
    # Telefone - campo opcional
    phone = models.CharField(
        max_length=20, 
        blank=True,
        help_text="Seu telefone (formato livre, ex: (11) 99999-9999)"
    )
    
    # Localização - onde você mora/trabalha
    location = models.CharField(
        max_length=100,
        help_text="Sua cidade/estado (ex: São Paulo, SP)"
    )
    
    # URLs das redes sociais - todos opcionais
    github_url = models.URLField(
        blank=True,
        help_text="URL do seu perfil no GitHub"
    )
    linkedin_url = models.URLField(
        blank=True,
        help_text="URL do seu perfil no LinkedIn"
    )
    twitter_url = models.URLField(
        blank=True,
        help_text="URL do seu perfil no Twitter"
    )
    
    # Biografia - descrição sobre você
    bio = models.TextField(
        help_text="Uma breve descrição sobre você e sua carreira"
    )
    
    # Se está disponível para trabalho
    available_for_work = models.BooleanField(
        default=True,
        help_text="Marque se você está procurando emprego/projetos"
    )
    
    class Meta:
        # Nomes que aparecem no Django Admin
        verbose_name = "Informação de Contato"
        verbose_name_plural = "Informações de Contato"
    
    def __str__(self):
        """Como este objeto será exibido no Django Admin"""
        return f"Contato - {self.email}"

class Project(models.Model):
    """
    Modelo para armazenar projetos do portfólio
    
    Cada projeto é um trabalho que você desenvolveu e quer mostrar.
    Pode ser um site, app, sistema, etc.
    """
    
    # Opções de status do projeto
    STATUS_CHOICES = [
        ('live', 'Online'),           # Projeto no ar, funcionando
        ('development', 'Desenvolvimento'), # Ainda sendo desenvolvido
        ('completed', 'Concluído'),   # Terminado mas não necessariamente online
    ]
    
    # Título do projeto - campo obrigatório
    title = models.CharField(
        max_length=200,
        help_text="Nome do seu projeto (ex: E-commerce de Roupas)"
    )
    
    # Descrição detalhada do projeto
    description = models.TextField(
        help_text="Explique o que o projeto faz, qual problema resolve, etc."
    )
    
    # Ano que o projeto foi criado/concluído
    year = models.IntegerField(
        help_text="Ano de conclusão do projeto (ex: 2024)"
    )
    
    # Status atual do projeto
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='completed',
        help_text="Situação atual do projeto"
    )
    
    # Tecnologias usadas (separadas por vírgula)
    technologies = models.TextField(
        help_text="Tecnologias separadas por vírgula (ex: Python, Django, JavaScript, React)"
    )
    
    # URL do projeto (se estiver online)
    project_url = models.URLField(
        blank=True, 
        null=True,
        help_text="Link para acessar o projeto online (se houver)"
    )
    
    # URL do repositório no GitHub
    github_url = models.URLField(
        blank=True, 
        null=True,
        help_text="Link para o código no GitHub"
    )
    
    # Imagem de capa do projeto
    image = models.ImageField(
        upload_to='projects/', 
        blank=True, 
        null=True,
        help_text="Screenshot ou imagem representativa do projeto"
    )
    
    # Se é um projeto em destaque (aparece na home)
    featured = models.BooleanField(
        default=False,
        help_text="Marque para exibir este projeto na página inicial"
    )
    
    # Ordem de exibição (menor número aparece primeiro)
    order = models.IntegerField(
        default=0,
        help_text="Ordem de exibição (0 = primeiro, 1 = segundo, etc.)"
    )
    
    # Data de criação do registro (automático)
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Data em que o projeto foi adicionado ao portfólio"
    )
    
    # Data da última atualização (automático)
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Data da última modificação do projeto"
    )
    
    class Meta:
        # Ordem padrão: primeiro por ordem, depois por ano (mais recente primeiro)
        ordering = ['order', '-year']
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
    
    def __str__(self):
        """Como este projeto será exibido no Django Admin"""
        return self.title
    
    def get_technologies_list(self):
        """
        Converte a string de tecnologias em uma lista
        
        Por exemplo: "Python, Django, React" -> ["Python", "Django", "React"]
        """
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.TextField()
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    current = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-start_year']
        verbose_name = "Experiência"
        verbose_name_plural = "Experiências"
    
    def __str__(self):
        return f"{self.role} at {self.company}"
    
    def get_year_range(self):
        if self.current or not self.end_year:
            return f"{self.start_year} - Present"
        return f"{self.start_year} - {self.end_year}"

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools & Others'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    level = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Nível de 0 a 100"
    )
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order']
        verbose_name = "Habilidade"
        verbose_name_plural = "Habilidades"
    
    def __str__(self):
        return f"{self.name} ({self.level}%)"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
    
    def __str__(self):
        return f"Message from {self.name} - {self.email}"