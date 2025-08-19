"""
WSGI - Web Server Gateway Interface

Este arquivo é o ponto de entrada para servidores web como Vercel, Heroku, etc.
Ele conecta o servidor web com a aplicação Django.

O que faz cada linha:
1. Importa bibliotecas necessárias
2. Define qual arquivo de configurações usar (settings.py)
3. Sinaliza que está rodando no Vercel (para usar configurações de produção)
4. Cria a aplicação Django
5. Cria um alias 'app' que o Vercel espera encontrar
"""

import os
from django.core.wsgi import get_wsgi_application

# Diz ao Django onde encontrar as configurações do projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

# Sinaliza que está rodando no Vercel (ativa configurações de produção)
os.environ.setdefault('VERCEL', '1')

# Cria a aplicação Django que o servidor web irá usar
application = get_wsgi_application()

# O Vercel procura por uma variável chamada 'app'
app = application