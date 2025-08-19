# Sistema de tradução customizado para contornar limitações do gettext no Windows

TRANSLATIONS = {
    'pt-br': {
        'Portfólio': 'Portfólio',
        'Sobre': 'Sobre', 
        'Habilidades': 'Habilidades',
        'Contato': 'Contato',
        'Currículo': 'Currículo',
        'Projetado e Desenvolvido por Luis Pieri': 'Projetado e Desenvolvido por Luis Pieri',
    },
    'en': {
        'Portfólio': 'Portfolio',
        'Sobre': 'About',
        'Habilidades': 'Skills', 
        'Contato': 'Contact',
        'Currículo': 'Resume',
        'Projetado e Desenvolvido por Luis Pieri': 'Designed and Developed by Luis Pieri',
    }
}

def get_translation(text, language_code='pt-br'):
    """Retorna a tradução do texto para o idioma especificado"""
    return TRANSLATIONS.get(language_code, {}).get(text, text)