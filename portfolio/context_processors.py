from django.utils.translation import get_language
from .translations import get_translation

def translation_processor(request):
    """Context processor para fornecer função de tradução aos templates"""
    current_language = get_language() or 'pt-br'
    
    # Mapear códigos de idioma
    if current_language == 'en-us':
        current_language = 'en'
    
    return {
        'current_language': current_language,
    }