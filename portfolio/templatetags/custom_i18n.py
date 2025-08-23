from django import template
from django.utils.translation import get_language

register = template.Library()

# Dicionário de traduções direto no template tag
TRANSLATIONS = {
    'pt-br': {
        # Menu
        'Portfólio': 'Portfólio',
        'Sobre': 'Sobre', 
        'Habilidades': 'Habilidades',
        'Contato': 'Contato',
        'Currículo': 'Currículo',
        
        # Hero Section
        'Olá, meu nome é': 'Olá, meu nome é',
        'Eu construo experiências digitais com foco no usuário final.': 'Eu construo experiências digitais com foco no usuário final.',
        'Minha jornada através do suporte técnico e da gestão de projetos me deu uma visão clara sobre as reais necessidades dos clientes. Hoje, aplico essa perspectiva como Desenvolvedor de Software para construir soluções que não são apenas tecnicamente sólidas, mas verdadeiramente eficazes.': 'Minha jornada através do suporte técnico e da gestão de projetos me deu uma visão clara sobre as reais necessidades dos clientes. Hoje, aplico essa perspectiva como Desenvolvedor de Software para construir soluções que não são apenas tecnicamente sólidas, mas verdadeiramente eficazes.',
        'Confira meu trabalho!': 'Confira meu trabalho!',
        
        # Sections
        'Algumas Coisas Que Construí': 'Algumas Coisas Que Construí',
        'Sobre Mim': 'Sobre Mim',
        'Nenhum projeto encontrado. Adicione projetos no painel administrativo.': 'Nenhum projeto encontrado. Adicione projetos no painel administrativo.',
        'Ver todos os projetos': 'Ver todos os projetos',
        'Ver Projeto': 'Ver Projeto',
        
        # About Section
        'Sou Desenvolvedor de Software e estudante de Engenharia da Computação, e minha carreira é a prova de que diferentes experiências constroem um profissional mais completo. Antes de me dedicar ao código, atuei em áreas como P&D, implantação de soluções e suporte técnico avançado com tecnologias de Telemetria e Vídeo-Telemetria.': 'Sou Desenvolvedor de Software e estudante de Engenharia da Computação, e minha carreira é a prova de que diferentes experiências constroem um profissional mais completo. Antes de me dedicar ao código, atuei em áreas como P&D, implantação de soluções e suporte técnico avançado com tecnologias de Telemetria e Vídeo-Telemetria.',
        'Essa vivência me ensinou a ouvir o cliente, a entender a fundo os desafios do usuário final e a gerenciar projetos com foco em resultados. Foi essa busca por criar soluções mais eficazes que me levou ao desenvolvimento de software.': 'Essa vivência me ensinou a ouvir o cliente, a entender a fundo os desafios do usuário final e a gerenciar projetos com foco em resultados. Foi essa busca por criar soluções mais eficazes que me levou ao desenvolvimento de software.',
        'Meu objetivo profissional é utilizar a tecnologia para otimizar processos e criar soluções intuitivas. Acredito que minha habilidade de unir a visão técnica do desenvolvimento de software com a experiência prática em processos e necessidades do cliente é o que me permite agregar valor de forma consistente e significativa em cada projeto que participo.': 'Meu objetivo profissional é utilizar a tecnologia para otimizar processos e criar soluções intuitivas. Acredito que minha habilidade de unir a visão técnica do desenvolvimento de software com a experiência prática em processos e necessidades do cliente é o que me permite agregar valor de forma consistente e significativa em cada projeto que participo.',
        'Experiência': 'Experiência',
        'Desenvolvedor Web': 'Desenvolvedor Web',
        'KF Marketing - Freelance': 'KF Marketing - Freelance',
        'Desenvolvimento de soluções web completas, da criação de interfaces e APIs até a modelagem de bancos de dados.': 'Desenvolvimento de soluções web completas, da criação de interfaces e APIs até a modelagem de bancos de dados.',
        'Especialista em Soluções e Produtos IoT': 'Especialista em Soluções e Produtos IoT',
        'Jimi IoT Brasil': 'Jimi IoT Brasil',
        'Responsável por todo o ciclo do cliente, do suporte técnico à implementação de projetos e análise de novos produtos.': 'Responsável por todo o ciclo do cliente, do suporte técnico à implementação de projetos e análise de novos produtos.',
        
        # Expertise Cards
        'Fundamentos Sólidos': 'Fundamentos Sólidos',
        'Código de qualidade como base para criar soluções escaláveis e sustentáveis a longo prazo.': 'Código de qualidade como base para criar soluções escaláveis e sustentáveis a longo prazo.',
        'Visão do Cliente': 'Visão do Cliente',
        'Minha vivência com clientes me permite criar soluções web focadas em usabilidade e na resolução de suas dores reais.': 'Minha vivência com clientes me permite criar soluções web focadas em usabilidade e na resolução de suas dores reais.',
        'Resolução de Problemas': 'Resolução de Problemas',
        'Análise a fundo de cada desafio para aplicar a tecnologia como ferramenta na otimização de processos e resultados.': 'Análise a fundo de cada desafio para aplicar a tecnologia como ferramenta na otimização de processos e resultados.',
        
        # Skills Section
        'Gestão de Projetos e Processos': 'Gestão de Projetos e Processos',
        'Front-End': 'Front-End',
        'Backend': 'Backend',
        'Banco de Dados': 'Banco de Dados',
        'UI/UX': 'UI/UX',
        
        # Footer
        'Projetado e Desenvolvido por Luis Pieri': 'Projetado e Desenvolvido por Luis Pieri',
        'E-mail copiado!': 'E-mail copiado!',
        
        # Time
        '2025 - Presente': '2025 - Presente',
        '2023 - 2025': '2023 - 2025',
        
        # Contact Page
        'Contato - Portfolio': 'Contato - Portfolio',
        'Vamos Trabalhar Juntos': 'Vamos Trabalhar Juntos',
        'Estou sempre interessado em novas oportunidades e projetos empolgantes. Se você tem uma ideia específica em mente ou apenas quer explorar possibilidades, adoraria ouvir de você.': 'Estou sempre interessado em novas oportunidades e projetos empolgantes. Se você tem uma ideia específica em mente ou apenas quer explorar possibilidades, adoraria ouvir de você.',
        'E-mail': 'E-mail',
        'Telefone': 'Telefone',
        'Localização': 'Localização',
        'Nome': 'Nome',
        'Mensagem': 'Mensagem',
        'Enviar Mensagem': 'Enviar Mensagem',
        
        # Projects Page
        'Projetos - Portfolio': 'Projetos - Portfolio',
        'Voltar aos projetos': 'Voltar aos projetos',
        'Todos os Projetos': 'Todos os Projetos',
        'Uma visão completa do meu trabalho, incluindo aplicações web, sistemas e experiências digitais.': 'Uma visão completa do meu trabalho, incluindo aplicações web, sistemas e experiências digitais.',
        'Nenhum projeto encontrado.': 'Nenhum projeto encontrado.',
        'Adicione projetos no painel administrativo.': 'Adicione projetos no painel administrativo.',
    },
    'en': {
        # Menu
        'Portfólio': 'Portfolio',
        'Sobre': 'About',
        'Habilidades': 'Skills', 
        'Contato': 'Contact',
        'Currículo': 'Resume',
        
        # Hero Section
        'Olá, meu nome é': 'Hello, my name is',
        'Eu construo experiências digitais com foco no usuário final.': 'I build digital experiences focused on end users.',
        'Minha jornada através do suporte técnico e da gestão de projetos me deu uma visão clara sobre as reais necessidades dos clientes. Hoje, aplico essa perspectiva como Desenvolvedor de Software para construir soluções que não são apenas tecnicamente sólidas, mas verdadeiramente eficazes.': 'My journey through technical support and project management has given me a clear vision of real client needs. Today, I apply this perspective as a Software Developer to build solutions that are not only technically sound, but truly effective.',
        'Confira meu trabalho!': 'Check out my work!',
        
        # Sections
        'Algumas Coisas Que Construí': 'Some Things I\'ve Built',
        'Sobre Mim': 'About Me',
        'Nenhum projeto encontrado. Adicione projetos no painel administrativo.': 'No projects found. Add projects in the admin panel.',
        'Ver todos os projetos': 'View all projects',
        'Ver Projeto': 'View Project',
        
        # About Section
        'Sou Desenvolvedor de Software e estudante de Engenharia da Computação, e minha carreira é a prova de que diferentes experiências constroem um profissional mais completo. Antes de me dedicar ao código, atuei em áreas como P&D, implantação de soluções e suporte técnico avançado com tecnologias de Telemetria e Vídeo-Telemetria.': 'I am a Software Developer and Computer Engineering student, and my career is proof that different experiences build a more complete professional. Before dedicating myself to code, I worked in areas such as R&D, solution implementation and advanced technical support with Telemetry and Video-Telemetry technologies.',
        'Essa vivência me ensinou a ouvir o cliente, a entender a fundo os desafios do usuário final e a gerenciar projetos com foco em resultados. Foi essa busca por criar soluções mais eficazes que me levou ao desenvolvimento de software.': 'This experience taught me to listen to clients, to deeply understand end-user challenges and to manage projects with a focus on results. It was this quest to create more effective solutions that led me to software development.',
        'Meu objetivo profissional é utilizar a tecnologia para otimizar processos e criar soluções intuitivas. Acredito que minha habilidade de unir a visão técnica do desenvolvimento de software com a experiência prática em processos e necessidades do cliente é o que me permite agregar valor de forma consistente e significativa em cada projeto que participo.': 'My professional goal is to use technology to optimize processes and create intuitive solutions. I believe that my ability to unite the technical vision of software development with practical experience in processes and client needs is what allows me to add value consistently and meaningfully in every project I participate in.',
        'Experiência': 'Experience',
        'Desenvolvedor Web': 'Web Developer',
        'KF Marketing - Freelance': 'KF Marketing - Freelance',
        'Desenvolvimento de soluções web completas, da criação de interfaces e APIs até a modelagem de bancos de dados.': 'Development of complete web solutions, from creating interfaces and APIs to database modeling.',
        'Especialista em Soluções e Produtos IoT': 'IoT Solutions and Products Specialist',
        'Jimi IoT Brasil': 'Jimi IoT Brasil',
        'Responsável por todo o ciclo do cliente, do suporte técnico à implementação de projetos e análise de novos produtos.': 'Responsible for the entire customer cycle, from technical support to project implementation and analysis of new products.',
        
        # Expertise Cards
        'Fundamentos Sólidos': 'Solid Foundations',
        'Código de qualidade como base para criar soluções escaláveis e sustentáveis a longo prazo.': 'Quality code as a foundation for creating scalable and long-term sustainable solutions.',
        'Visão do Cliente': 'Client Vision',
        'Minha vivência com clientes me permite criar soluções web focadas em usabilidade e na resolução de suas dores reais.': 'My experience with clients allows me to create web solutions focused on usability and solving their real pain points.',
        'Resolução de Problemas': 'Problem Solving',
        'Análise a fundo de cada desafio para aplicar a tecnologia como ferramenta na otimização de processos e resultados.': 'In-depth analysis of each challenge to apply technology as a tool in optimizing processes and results.',
        
        # Skills Section
        'Gestão de Projetos e Processos': 'Project and Process Management',
        'Front-End': 'Front-End',
        'Backend': 'Backend',
        'Banco de Dados': 'Database',
        'UI/UX': 'UI/UX',
        
        # Footer
        'Projetado e Desenvolvido por Luis Pieri': 'Designed and Developed by Luis Pieri',
        'E-mail copiado!': 'Email copied!',
        
        # Time
        '2025 - Presente': '2025 - Present',
        '2023 - 2025': '2023 - 2025',
        
        # Contact Page
        'Contato - Portfolio': 'Contact - Portfolio',
        'Vamos Trabalhar Juntos': 'Let\'s Work Together',
        'Estou sempre interessado em novas oportunidades e projetos empolgantes. Se você tem uma ideia específica em mente ou apenas quer explorar possibilidades, adoraria ouvir de você.': 'I\'m always interested in new opportunities and exciting projects. If you have a specific idea in mind or just want to explore possibilities, I\'d love to hear from you.',
        'E-mail': 'Email',
        'Telefone': 'Phone',
        'Localização': 'Location',
        'Nome': 'Name',
        'Mensagem': 'Message',
        'Enviar Mensagem': 'Send Message',
        
        # Projects Page
        'Projetos - Portfolio': 'Projects - Portfolio',
        'Voltar aos projetos': 'Back to projects',
        'Todos os Projetos': 'All Projects',
        'Uma visão completa do meu trabalho, incluindo aplicações web, sistemas e experiências digitais.': 'A complete view of my work, including web applications, systems and digital experiences.',
        'Nenhum projeto encontrado.': 'No projects found.',
        'Adicione projetos no painel administrativo.': 'Add projects in the admin panel.',
        
        # Project Status
        'Online': 'Live',
        'Desenvolvimento': 'Development',
        'Concluído': 'Completed',
    }
}

@register.simple_tag
def custom_trans(text):
    """Template tag para tradução customizada"""
    current_language = get_language() or 'pt-br'
    
    # Mapear códigos de idioma se necessário
    if current_language == 'en-us':
        current_language = 'en'
    
    # Buscar tradução
    return TRANSLATIONS.get(current_language, {}).get(text, text)

@register.simple_tag
def project_title(project):
    """Retorna o título do projeto no idioma atual"""
    current_language = get_language() or 'pt-br'
    if current_language == 'en-us':
        current_language = 'en'
    
    # Debug
    print(f"[PROJECT_TITLE] Idioma: {current_language}, Projeto: {project.title}")
    print(f"[PROJECT_TITLE] title_en: {project.title_en}")
    
    result = project.get_title(current_language)
    print(f"[PROJECT_TITLE] Resultado: {result}")
    return result

@register.simple_tag
def project_description(project):
    """Retorna a descrição do projeto no idioma atual"""
    try:
        current_language = get_language() or 'pt-br'
        if current_language == 'en-us':
            current_language = 'en'
        
        if hasattr(project, 'get_description') and callable(project.get_description):
            return project.get_description(current_language)
        else:
            # Fallback manual se método não existir
            if current_language == 'en' and hasattr(project, 'description_en') and project.description_en:
                return project.description_en
            return project.description if hasattr(project, 'description') else ''
    except Exception as e:
        print(f"[ERROR] project_description: {e}")
        return project.description if hasattr(project, 'description') else ''

@register.simple_tag
def project_status(project):
    """Retorna o status do projeto traduzido"""
    current_language = get_language() or 'pt-br'
    if current_language == 'en-us':
        current_language = 'en'
    
    status_display = project.get_status_display()
    return custom_trans(status_display)