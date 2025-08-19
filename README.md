# 🎯 Portfolio Profissional - Django

> **Um portfólio completo e responsivo desenvolvido em Django para mostrar projetos, experiências e habilidades de forma profissional.**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://djangoproject.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Deploy](https://img.shields.io/badge/Deploy-Vercel-black.svg)](https://vercel.com)

---

## 🌟 **Demonstração**

### 🌐 **Site Online:**
**URL:** [portifolio.pieritech.com.br](https://portifolio.pieritech.com.br)

### 📱 **Screenshots:**
- **Desktop:** Layout responsivo e moderno
- **Mobile:** Interface adaptada para celulares
- **Admin:** Painel de administração completo

---

## 📋 **Sobre o Projeto**

Este é um **portfólio profissional completo** desenvolvido em Django, ideal para desenvolvedores, designers e profissionais de tecnologia que querem mostrar seus trabalhos de forma elegante e funcional.

### ✨ **Características Principais:**

- 🎨 **Design Moderno:** Interface clean e profissional
- 📱 **Totalmente Responsivo:** Funciona perfeitamente em mobile e desktop  
- ⚡ **Performance Otimizada:** Carregamento rápido e eficiente
- 🔧 **Fácil de Customizar:** Código bem organizado e documentado
- 🌐 **Deploy Automático:** Configurado para Vercel, Heroku e outros
- 🔐 **Seguro:** Boas práticas de segurança implementadas

---

## 🚀 **Funcionalidades**

### 🏠 **Página Inicial**
- Apresentação pessoal com foto e descrição
- Projetos em destaque
- Links para redes sociais
- Call-to-action para contato

### 💼 **Galeria de Projetos**
- Lista completa de projetos
- Detalhes técnicos de cada projeto
- Links para GitHub e versão live
- Filtros por tecnologia

### 📞 **Formulário de Contato**
- Formulário funcional que envia emails
- Validação de campos
- Mensagens de sucesso/erro
- Armazenamento de mensagens no banco

### ⚙️ **Painel Administrativo**
- Interface Django Admin customizada
- Gerenciamento de projetos
- Controle de informações pessoais
- Visualização de mensagens recebidas

### 🩺 **Health Check**
- Endpoint `/healthy` para monitoramento
- Verificação de banco de dados
- Status da aplicação em JSON

---

## 🛠️ **Tecnologias Utilizadas**

### 🐍 **Backend**
- **[Django 4.2](https://djangoproject.com)** - Framework web robusto
- **[Python 3.9+](https://python.org)** - Linguagem de programação
- **[SQLite](https://sqlite.org)** - Banco de dados (desenvolvimento)
- **[PostgreSQL](https://postgresql.org)** - Banco de dados (produção)

### 🎨 **Frontend**
- **[HTML5](https://developer.mozilla.org/docs/Web/HTML)** - Estrutura semântica
- **[CSS3](https://developer.mozilla.org/docs/Web/CSS)** - Estilos modernos
- **[JavaScript](https://developer.mozilla.org/docs/Web/JavaScript)** - Interatividade
- **[Tailwind CSS](https://tailwindcss.com)** - Framework CSS utilitário

### 🚀 **Deploy e Infraestrutura**
- **[Vercel](https://vercel.com)** - Deploy automático
- **[WhiteNoise](https://whitenoise.evans.io)** - Servir arquivos estáticos
- **[Gunicorn](https://gunicorn.org)** - Servidor WSGI
- **[GitHub Actions](https://github.com/features/actions)** - CI/CD

### 📦 **Dependências Principais**
```txt
Django==4.2.16          # Framework web
Pillow==10.4.0          # Processamento de imagens  
python-decouple==3.8    # Variáveis de ambiente
whitenoise==6.7.0       # Arquivos estáticos
```

---

## 📁 **Estrutura do Projeto**

```
portfolio-django/
│
├── 📄 manage.py                 # Script principal do Django
├── 📄 wsgi.py                   # Configuração para deploy
├── 📄 vercel.json               # Configuração do Vercel
├── 📄 requirements.txt          # Dependências Python
├── 📄 db.sqlite3               # Banco de dados local
├── 📄 README.md                # Este arquivo
│
├── 📁 portfolio_project/       # Configurações principais
│   ├── 📄 settings.py          # Configurações do Django
│   ├── 📄 urls.py              # URLs principais
│   ├── 📄 wsgi.py              # WSGI para produção
│   └── 📄 asgi.py              # ASGI para apps assíncronas
│
├── 📁 portfolio/               # App principal
│   ├── 📄 models.py            # Modelos do banco (Project, Contact, etc.)
│   ├── 📄 views.py             # Lógica das páginas
│   ├── 📄 urls.py              # URLs do app
│   ├── 📄 admin.py             # Configuração do admin
│   └── 📁 migrations/          # Migrações do banco
│
├── 📁 templates/               # Templates HTML
│   ├── 📄 base.html            # Template base
│   └── 📁 portfolio/
│       ├── 📄 home.html        # Página inicial
│       ├── 📄 projects.html    # Lista de projetos
│       ├── 📄 project_detail.html # Detalhes do projeto
│       └── 📄 contact.html     # Página de contato
│
├── 📁 static/                  # Arquivos estáticos
│   ├── 📁 css/
│   │   └── 📄 style.css        # Estilos principais
│   ├── 📁 js/
│   │   └── 📄 main.js          # JavaScript
│   └── 📁 images/              # Imagens do site
│
├── 📁 media/                   # Uploads de usuários
│   └── 📁 projects/            # Imagens dos projetos
│
└── 📁 docs/                    # Documentação extra
    ├── 📄 AWS_DEPLOY_GUIDE.md  # Guia para deploy AWS
    └── 📄 explanation.md       # Explicação detalhada
```

---

## 🚀 **Como Usar Este Projeto**

### 📋 **Pré-requisitos**

Antes de começar, você precisa ter instalado:

- **[Python 3.9+](https://python.org/downloads/)** 
- **[Git](https://git-scm.com/downloads)**
- **[VS Code](https://code.visualstudio.com/)** (opcional, mas recomendado)

### 1️⃣ **Clonando o Projeto**

```bash
# Clone este repositório
git clone https://github.com/luispieri/portfolio-django.git

# Entre na pasta do projeto
cd portfolio-django
```

### 2️⃣ **Configurando o Ambiente Virtual**

```bash
# Crie um ambiente virtual (recomendado)
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\\Scripts\\activate
# No Mac/Linux:
source venv/bin/activate
```

### 3️⃣ **Instalando Dependências**

```bash
# Instale todas as dependências
pip install -r requirements.txt

# Verifique se tudo foi instalado
pip list
```

### 4️⃣ **Configurando o Banco de Dados**

```bash
# Aplique as migrações (cria as tabelas)
python manage.py migrate

# Verifique se não há erros
python manage.py check
```

### 5️⃣ **Criando um Administrador**

```bash
# Crie sua conta de administrador
python manage.py createsuperuser

# Preencha os dados solicitados:
# Username: admin
# Email: seu-email@exemplo.com  
# Password: sua-senha-segura
```

### 6️⃣ **Executando o Projeto**

```bash
# Inicie o servidor de desenvolvimento
python manage.py runserver

# O site estará disponível em:
# http://localhost:8000
```

### 7️⃣ **Acessando a Administração**

1. Acesse: **http://localhost:8000/admin**
2. Faça login com os dados criados no passo 5
3. Adicione seus projetos e informações pessoais

---

## 🎨 **Personalizando o Portfolio**

### 📝 **Adicionando Seus Dados**

1. **Acesse o Admin:** `http://localhost:8000/admin`
2. **Informações de Contato:** Adicione seus dados pessoais
3. **Projetos:** Crie seus projetos com imagens e descrições
4. **Experiências:** Adicione seu histórico profissional

### 🖼️ **Personalizando Imagens**

```bash
# Adicione suas imagens em:
static/images/          # Imagens do site (logo, ícones)
media/projects/         # Screenshots dos projetos
```

### 🎨 **Customizando Estilos**

```css
/* Edite o arquivo: static/css/style.css */

/* Exemplo: Mudar cor principal */
:root {
    --primary-color: #sua-cor-preferida;
    --secondary-color: #outra-cor;
}
```

### 📄 **Modificando Textos**

Edite os templates em `templates/portfolio/`:
- `home.html` - Página inicial
- `projects.html` - Lista de projetos  
- `contact.html` - Página de contato

---

## 🌐 **Deploy para Produção**

### 🚀 **Deploy no Vercel (Recomendado - GRATUITO)**

1. **Fork este repositório** no seu GitHub
2. **Acesse:** [vercel.com](https://vercel.com)
3. **Conecte** sua conta GitHub
4. **Importe** este projeto
5. **Deploy automático!** ✨

#### Configurações no Vercel:
```bash
# Variáveis de ambiente (opcional):
DJANGO_SETTINGS_MODULE = portfolio_project.settings
SECRET_KEY = sua-chave-secreta-aqui
```

## 🔧 **Comandos Úteis**

### 🛠️ **Desenvolvimento**

```bash
# Executar servidor
python manage.py runserver

# Criar migrações
python manage.py makemigrations

# Aplicar migrações  
python manage.py migrate

# Coletar arquivos estáticos
python manage.py collectstatic

# Abrir shell interativo
python manage.py shell

# Verificar problemas
python manage.py check

# Executar testes
python manage.py test
```

### 📊 **Monitoramento**

```bash
# Health check
curl http://localhost:8000/healthy

# Ver logs
tail -f logs/django.log

# Verificar performance
python manage.py check --deploy
```

---

## 🔐 **Configurações de Segurança**

### 🛡️ **Para Produção**

No arquivo `settings.py`, certifique-se de:

```python
# ❌ NUNCA deixe assim em produção:
DEBUG = True
SECRET_KEY = 'chave-simples'

# ✅ Configure corretamente:
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['seu-dominio.com']
```

### 🔑 **Gerando SECRET_KEY Segura**

```python
# Execute no shell do Django:
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

---

## 📚 **Recursos Adicionais**

### 📖 **Documentação**

- **[Django Docs](https://docs.djangoproject.com/)** - Documentação oficial
- **[Python.org](https://python.org)** - Aprenda Python
- **[MDN Web Docs](https://developer.mozilla.org/)** - HTML, CSS, JS

### 🎓 **Tutoriais**

- **[Django Girls](https://tutorial.djangogirls.org/)** - Tutorial iniciante
- **[Django for Beginners](https://djangoforbeginners.com/)** - Livro recomendado
- **[Real Python](https://realpython.com/)** - Tutoriais avançados

### 🛠️ **Ferramentas Úteis**

- **[Django Extensions](https://django-extensions.readthedocs.io/)** - Comandos extras
- **[Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/)** - Debug avançado
- **[Black](https://black.readthedocs.io/)** - Formatação de código

---

## 🤝 **Contribuição**

### 🐛 **Encontrou um Bug?**

1. **Verifique** se já não foi reportado nas [Issues](https://github.com/luispieri/portfolio-django/issues)
2. **Crie uma nova issue** com:
   - Descrição clara do problema
   - Passos para reproduzir
   - Screenshots (se aplicável)

### 💡 **Quer Contribuir?**

1. **Fork** o projeto
2. **Crie** uma branch: `git checkout -b feature/nova-funcionalidade`
3. **Commit** suas mudanças: `git commit -m 'Add nova funcionalidade'`
4. **Push** para a branch: `git push origin feature/nova-funcionalidade`
5. **Abra** um Pull Request

### 📝 **Padrões de Commit**

```bash
# Use commits descritivos:
git commit -m "feat: adiciona sistema de tags nos projetos"
git commit -m "fix: corrige bug no formulário de contato"  
git commit -m "docs: atualiza README com novas instruções"
```

---

## 📄 **Licença**

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### ⚖️ **O que isso significa?**

- ✅ **Uso comercial** permitido
- ✅ **Modificação** permitida  
- ✅ **Distribuição** permitida
- ✅ **Uso privado** permitido
- ❌ **Sem garantia** - use por sua conta e risco

---

## 👨‍💻 **Autor**

### **Luis de Pieri**

- 🌐 **Website:** [pieritech.com.br](https://pieritech.com.br)
- 📧 **Email:** luisdpieri.tech@gmail.com
- 💼 **LinkedIn:** [linkedin.com/in/luispieri](https://linkedin.com/in/luispieri)
- 💻 **GitHub:** [github.com/luispieri](https://github.com/luispieri)
- 📸 **Instagram:** [@luispieri_](https://instagram.com/luispieri_)

---

## 📊 **Status do Projeto**

### 📈 **Estatísticas**

- ✅ **Funcionalidades:** 100% implementadas
- ✅ **Testes:** Cobertura básica
- ✅ **Documentação:** Completa
- ✅ **Deploy:** Funcional
- ✅ **Responsividade:** Mobile-first

### 🚧 **Próximas Melhorias**

- [ ] Sistema de blog integrado
- [ ] Múltiplos idiomas (i18n)
- [ ] API REST para mobile
- [ ] Integração com redes sociais
- [ ] Analytics integrado

---

## 📞 **Suporte**

### 🆘 **Precisa de Ajuda?**

1. **Leia** a documentação acima
2. **Verifique** as [Issues](https://github.com/luispieri/portfolio-django/issues) existentes
3. **Crie** uma nova issue se necessário
4. **Entre em contato** via email

### 💬 **Canais de Suporte**

- **Issues GitHub:** Para bugs e sugestões
- **Email:** Para dúvidas específicas
- **LinkedIn:** Para networking profissional

---

<div align="center">

### 🌟 **Se este projeto te ajudou, deixe uma estrela! ⭐**

**Desenvolvido com ❤️ por [Luis de Pieri](https://github.com/luispieri)**

</div>

---

*Última atualização: Agosto 2025*