from django.core.management.base import BaseCommand
from portfolio.models import Project, Experience, Skill, ContactInfo

class Command(BaseCommand):
    help = 'Popula o banco com dados de exemplo'

    def handle(self, *args, **options):
        # Criar informações de contato
        contact_info, created = ContactInfo.objects.get_or_create(
            defaults={
                'email': 'seu@email.com',
                'phone': '+55 (11) 99999-9999',
                'location': 'São Paulo, Brasil',
                'github_url': 'https://github.com/seuusuario',
                'linkedin_url': 'https://linkedin.com/in/seuperfil',
                'bio': 'I craft digital experiences through clean code and thoughtful design. Specialized in modern web technologies and scalable solutions.',
                'available_for_work': True,
            }
        )

        # Limpar projetos existentes
        Project.objects.all().delete()
        self.stdout.write('Projetos existentes removidos.')

        # Criar projetos
        projects_data = [
            {
                'title': 'Currículo HTML',
                'description': 'Um projeto essencial para aprimorar minhas habilidades em desenvolvimento front-end e aplicação de estilos responsivos.',
                'year': 2025,
                'status': 'live',
                'technologies': 'HTML, CSS, JavaScript',
                'project_url': 'https://cv.pieritech.com.br',
                'github_url': 'https://github.com/luispieri/curriculo-html',
                'featured': True,
                'order': 1,
            },
            {
                'title': 'Encurtador de Links Pro',
                'description': 'Sistema completo de encurtamento de URLs com painel administrativo e recursos avançados. Projeto desenvolvido com arquitetura MVC usando Node.js e Express, incluindo funcionalidades de URLs personalizadas, QR codes automáticos, sistema de expiração configurável, analytics de cliques e painel administrativo com autenticação JWT.',
                'year': 2025,
                'status': 'live',
                'technologies': 'Node.js, Express, MySQL2, JavaScript, HTML5, CSS3, JWT, Bcrypt, QRCode, Moment, CORS, Compression',
                'project_url': 'https://encurtador-links-34n9.onrender.com/',
                'github_url': 'https://github.com/luispieri/encurtador-links',
                'featured': True,
                'order': 2,
            },
            {
                'title': 'Sistema de Controle Financeiro',
                'description': 'API REST completa para sistema de controle financeiro pessoal desenvolvida com Arquitetura Hexagonal (Ports & Adapters). Oferece gerenciamento completo de usuários, contas bancárias, transações financeiras, categorias personalizáveis, relatórios e dashboard administrativo. Sistema robusto com autenticação JWT, autorização por roles, validação de dados, rate limiting e documentação Swagger completa.',
                'year': 2025,
                'status': 'development',
                'technologies': 'Node.js, TypeScript, Express.js, MySQL, JWT, bcrypt, Helmet, CORS, Joi, Swagger/OpenAPI, Morgan, ESLint, Jest, Docker',
                'featured': True,
                'order': 3,
            },
            {
                'title': 'Sistema de Cadastro de Clientes - Pieri Tech',
                'description': 'Sistema completo de cadastro e login com upload de foto de perfil, dashboard e gerenciamento de usuários. Inclui CRUD completo de usuários, diferentes níveis de perfil (Administrador, Usuario Padrao, Visualizador), autenticação segura e interface responsiva.',
                'year': 2025,
                'status': 'development',
                'technologies': 'PHP 8+, MySQL, HTML5, CSS3, JavaScript ES6+, Bootstrap 5, Docker, Docker Compose',
                'featured': True,
                'order': 4,
            },
            {
                'title': 'Website GF Interiores',
                'description': 'Website institucional e portfólio para um escritório de design de interiores, que apresenta projetos, serviços e a história da empresa através de uma experiência visual elegante, com design moderno e totalmente adaptável para todos os dispositivos.',
                'year': 2025,
                'status': 'live',
                'technologies': 'HTML5, CSS3, JavaScript, Font Awesome, Google Fonts',
                'project_url': 'https://gfinteriores.com.br/',
                'featured': True,
                'order': 5,
            },
            {
                'title': 'Pieri Pro Services - Website Profissional',
                'description': 'Site institucional moderno e responsivo para a Pieri Pro Services, empresa especializada em serviços de limpeza, reparos e soluções para residências e empresas em São José dos Campos - SP. O projeto apresenta uma estrutura MVC com Express.js, oferecendo formulário de contato inteligente com integração WhatsApp, design adaptativo, dark mode automático e otimizações SEO.',
                'year': 2025,
                'status': 'development',
                'technologies': 'Node.js, Express.js, HTML5, CSS3, JavaScript ES6+, Bootstrap 5, Font Awesome 6, CSSO, Terser, SVGO, Imagemin, ESLint, Stylelint, Prettier',
                'featured': True,
                'order': 6,
            },
            {
                'title': 'Website T Franco Cosméticos - Beleza e Qualidade',
                'description': 'Website profissional para empresa de cosméticos com foco em produtos capilares de alta qualidade. O projeto inclui páginas institucionais, catálogo de produtos (Perfectlux, HairVive, Maginific) e sistema para captar distribuidores.',
                'year': 2025,
                'status': 'development',
                'technologies': 'HTML5, CSS3, JavaScript, Google Fonts, Font Awesome',
                'featured': True,
                'order': 7,
            },
            {
                'title': 'PieriTech - Website',
                'description': 'Website temporário "Em Breve" da Pieri Tech, empresa em desenvolvimento focada em projetos web, sistemas e soluções em TI. Página com design moderno e responsivo com animações CSS.',
                'year': 2025,
                'status': 'live',
                'technologies': 'HTML5, CSS3, JavaScript',
                'project_url': 'https://pieritech.com.br/',
                'github_url': 'https://github.com/luispieri/pieritech-website',
                'featured': True,
                'order': 8,
            }
        ]

        for project_data in projects_data:
            project = Project.objects.create(**project_data)
            self.stdout.write(f'Projeto criado: {project.title}')

        # Criar experiências de exemplo
        experiences_data = [
            {
                'company': 'Tech Startup Inc.',
                'role': 'Full Stack Developer',
                'description': 'Developed and maintained web applications using modern technologies.',
                'start_year': 2023,
                'current': True,
                'order': 1,
            },
            {
                'company': 'Digital Agency',
                'role': 'Frontend Developer',
                'description': 'Created responsive websites and user interfaces for various clients.',
                'start_year': 2022,
                'end_year': 2023,
                'order': 2,
            }
        ]

        for exp_data in experiences_data:
            experience, created = Experience.objects.get_or_create(
                company=exp_data['company'],
                role=exp_data['role'],
                defaults=exp_data
            )
            if created:
                self.stdout.write(f'Experiência criada: {experience.role} at {experience.company}')

        # Criar habilidades de exemplo
        skills_data = [
            {'name': 'JavaScript', 'category': 'frontend', 'level': 90, 'order': 1},
            {'name': 'React', 'category': 'frontend', 'level': 85, 'order': 2},
            {'name': 'Vue.js', 'category': 'frontend', 'level': 80, 'order': 3},
            {'name': 'Python', 'category': 'backend', 'level': 90, 'order': 1},
            {'name': 'Django', 'category': 'backend', 'level': 85, 'order': 2},
            {'name': 'Node.js', 'category': 'backend', 'level': 75, 'order': 3},
            {'name': 'PostgreSQL', 'category': 'database', 'level': 80, 'order': 1},
            {'name': 'MongoDB', 'category': 'database', 'level': 70, 'order': 2},
            {'name': 'Git', 'category': 'tools', 'level': 90, 'order': 1},
            {'name': 'Docker', 'category': 'tools', 'level': 75, 'order': 2},
        ]

        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'Habilidade criada: {skill.name}')

        self.stdout.write(
            self.style.SUCCESS('Dados de exemplo criados com sucesso!')
        )