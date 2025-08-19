# -*- coding: utf-8 -*-
"""
Configurações do Django para o projeto Portfolio

Este arquivo contém todas as configurações principais do Django.
Para mais informações sobre este arquivo, veja:
https://docs.djangoproject.com/en/4.2/topics/settings/

Para a lista completa de configurações e seus valores, veja:
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# PyMySQL não é necessário para desenvolvimento local com SQLite

# Caminho base do projeto - diretório onde está o manage.py
BASE_DIR = Path(__file__).resolve().parent.parent

# AVISO DE SEGURANÇA: mantenha a chave secreta em produção!
# Esta chave é usada para criptografia em sessões, cookies, etc.
SECRET_KEY = 'django-insecure-your-secret-key-here-change-in-production'

# AVISO DE SEGURANÇA: não execute com debug ligado em produção!
# DEBUG = True mostra erros detalhados (apenas para desenvolvimento)
DEBUG = True

# Lista de hosts/domínios que este site Django pode servir
# Em produção, adicione seu domínio: ['meusite.com', 'www.meusite.com']
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.vercel.app',
    'portifolio.pieritech.com.br',
    'www.portifolio.pieritech.com.br',
]

# Aplicações Django instaladas neste projeto
INSTALLED_APPS = [
    'django.contrib.admin',        # Interface administrativa do Django
    'django.contrib.auth',         # Sistema de autenticação (usuários, grupos, permissões)
    'django.contrib.contenttypes', # Framework de tipos de conteúdo
    'django.contrib.sessions',     # Sessões (manter usuário logado)
    'django.contrib.messages',     # Sistema de mensagens (sucesso, erro, etc.)
    'django.contrib.staticfiles',  # Gerenciamento de arquivos estáticos (CSS, JS, imagens)
    'portfolio',                   # Nossa aplicação principal do portfólio
]

# Lista de middlewares - processam requisições antes de chegar às views
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',        # Segurança (HTTPS, etc.)
    'django.contrib.sessions.middleware.SessionMiddleware', # Gerencia sessões
    'django.middleware.locale.LocaleMiddleware',            # Middleware para idiomas
    'django.middleware.common.CommonMiddleware',            # Funcionalidades comuns
    'django.middleware.csrf.CsrfViewMiddleware',           # Proteção contra CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Autenticação de usuários
    'django.contrib.messages.middleware.MessageMiddleware',    # Sistema de mensagens
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Proteção contra clickjacking
]

# Módulo principal de URLs do projeto
ROOT_URLCONF = 'portfolio_project.urls'

# Configurações dos templates (arquivos HTML)
TEMPLATES = [
    {
        # Motor de templates do Django
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Diretórios onde procurar templates personalizados
        'DIRS': [BASE_DIR / 'templates'],
        # Procurar templates dentro das pastas dos apps
        'APP_DIRS': True,
        # Opções adicionais
        'OPTIONS': {
            # Processadores de contexto - variáveis disponíveis em todos os templates
            'context_processors': [
                'django.template.context_processors.debug',    # Informações de debug
                'django.template.context_processors.request',  # Objeto request
                'django.template.context_processors.i18n',     # Informações de idioma
                'django.contrib.auth.context_processors.auth', # Usuário logado
                'django.contrib.messages.context_processors.messages', # Mensagens
                'portfolio.context_processors.translation_processor', # Tradução customizada
            ],
        },
    },
]

# Aplicação WSGI para deploy em produção
WSGI_APPLICATION = 'portfolio_project.wsgi.application'

# Configuração do banco de dados
# SQLite é ideal para desenvolvimento e projetos pequenos
DATABASES = {
    'default': {
        # Motor do banco de dados (SQLite)
        'ENGINE': 'django.db.backends.sqlite3',
        # Caminho para o arquivo do banco SQLite
        'NAME': str(BASE_DIR / 'db.sqlite3'),  # Convertido para string para Vercel
    }
}

# Validadores de senha - garantem senhas seguras
AUTH_PASSWORD_VALIDATORS = [
    {
        # Não permite senhas similares a informações do usuário
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        # Senha deve ter pelo menos 8 caracteres
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        # Não permite senhas muito comuns (123456, password, etc.)
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        # Não permite senhas totalmente numéricas
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Idioma do projeto (português do Brasil)
LANGUAGE_CODE = 'pt-br'

# Idiomas disponíveis
LANGUAGES = [
    ('pt-br', 'Português'),
    ('en', 'English'),
]

# Diretório para arquivos de tradução
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Fuso horário (Brasília)
TIME_ZONE = 'America/Sao_Paulo'

# Ativar internationalização (suporte a múltiplos idiomas)
USE_I18N = True

# Ativar suporte a fuso horário
USE_TZ = True

# URL para acessar arquivos estáticos (CSS, JS, imagens)
STATIC_URL = '/static/'
# Diretórios onde procurar arquivos estáticos durante o desenvolvimento
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
# Diretório onde os arquivos estáticos serão coletados para produção
STATIC_ROOT = BASE_DIR / 'staticfiles'

# URL para acessar arquivos de media (uploads de usuários)
MEDIA_URL = '/media/'
# Diretório onde os arquivos de media são armazenados
MEDIA_ROOT = BASE_DIR / 'media'

# Tipo de campo de chave primária padrão para novos modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ===============================================
# CONFIGURAÇÕES DE EMAIL
# ===============================================

# Backend de email - ATIVADO para Gmail SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Para testar apenas no console (descomente a linha abaixo):
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Configurações para envio real via Gmail SMTP
EMAIL_HOST = 'smtp.gmail.com'           # Servidor SMTP do Gmail
EMAIL_PORT = 587                        # Porta para TLS
EMAIL_USE_TLS = True                    # Usar criptografia TLS
EMAIL_HOST_USER = 'luisdpieri.tech@gmail.com'    # Seu email
EMAIL_HOST_PASSWORD = 'zadxxmuzghmwpaxf'   # Senha de app do Gmail (não a senha normal!)
DEFAULT_FROM_EMAIL = 'luisdpieri.tech@gmail.com' # Email remetente padrão

# COMO CONFIGURAR A SENHA DE APP DO GMAIL:
# 1. Acesse: https://myaccount.google.com/security
# 2. Ative a verificação em duas etapas
# 3. Crie uma 'Senha de app' para Django
# 4. Substitua 'your-app-password-here' pela senha gerada

# ===============================================
# CONFIGURAÇÕES PARA PRODUÇÃO (AWS)
# ===============================================

# Verificar se está rodando na AWS
if os.environ.get('AWS_DEPLOYMENT') or os.environ.get('DJANGO_ENVIRONMENT') == 'production':
    print("Rodando em PRODUCAO na AWS!")
    
    # SEGURANÇA: Desabilitar debug em produção
    DEBUG = False
    
    # SECRET KEY vem de variável de ambiente
    SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)
    
    # Domínios permitidos
    ALLOWED_HOSTS = [
        'localhost',
        '127.0.0.1',
        '.elasticbeanstalk.com',  # Para AWS Elastic Beanstalk
        '.amazonaws.com',         # Para AWS
        'portfolio-luis.com',     # Seu domínio personalizado
        'www.portfolio-luis.com', # WWW do seu domínio
    ]
    
    # ===============================================
    # BANCO DE DADOS AWS RDS (PostgreSQL)
    # ===============================================
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('RDS_DB_NAME', 'portfolio'),
            'USER': os.environ.get('RDS_USERNAME', 'postgres'),
            'PASSWORD': os.environ.get('RDS_PASSWORD'),
            'HOST': os.environ.get('RDS_HOSTNAME', 'localhost'),
            'PORT': os.environ.get('RDS_PORT', '5432'),
        }
    }
    
    # ===============================================
    # AWS S3 PARA ARQUIVOS ESTÁTICOS E MEDIA
    # ===============================================
    
    # AWS S3 Configurações
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', 'portfolio-static-files')
    AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', 'us-east-1')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    
    # Configurações de arquivos estáticos
    AWS_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    
    # Configurações de arquivos de media
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
    
    # ===============================================
    # SEGURANÇA EM PRODUÇÃO
    # ===============================================
    
    # Força HTTPS
    SECURE_SSL_REDIRECT = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    
    # ===============================================
    # LOGGING
    # ===============================================
    
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '/opt/python/log/django.log',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'INFO',
                'propagate': True,
            },
        },
    }

# ===============================================
# CONFIGURAÇÕES PARA VERCEL - SIMPLIFICADO
# ===============================================
elif os.environ.get('VERCEL'):
    print("Rodando em PRODUCAO no Vercel!")
    
    # Manter DEBUG = True temporariamente para ver erros
    DEBUG = True
    
else:
    # ===============================================
    # CONFIGURAÇÕES PARA DESENVOLVIMENTO LOCAL
    # ===============================================
    print("Rodando em DESENVOLVIMENTO local")
    
    # Manter configurações atuais para desenvolvimento
    pass  # As configurações já definidas acima são mantidas