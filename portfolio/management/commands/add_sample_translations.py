from django.core.management.base import BaseCommand
from portfolio.models import Project

class Command(BaseCommand):
    help = 'Adiciona traduções de exemplo para os projetos existentes'

    def handle(self, *args, **options):
        projects = Project.objects.all()
        
        if not projects.exists():
            self.stdout.write(
                self.style.WARNING('Nenhum projeto encontrado. Execute primeiro: python manage.py populate_sample_data')
            )
            return
        
        # Traduções de exemplo (você pode ajustar conforme seus projetos)
        sample_translations = {
            'title_patterns': {
                'E-commerce': 'E-commerce Platform',
                'Sistema': 'System',
                'Aplicativo': 'Application', 
                'Website': 'Website',
                'Portfólio': 'Portfolio',
                'Dashboard': 'Dashboard',
                'API': 'API',
                'Blog': 'Blog'
            },
            'description_replacements': {
                'Desenvolvimento de': 'Development of',
                'aplicação web': 'web application',
                'sistema completo': 'complete system',
                'interface moderna': 'modern interface',
                'funcionalidades avançadas': 'advanced features',
                'experiência do usuário': 'user experience',
                'responsivo': 'responsive',
                'banco de dados': 'database',
                'autenticação': 'authentication',
                'gestão': 'management',
                'controle': 'control',
                'administração': 'administration'
            }
        }
        
        updated_count = 0
        
        for project in projects:
            # Se já tem tradução, pula
            if project.title_en and project.description_en:
                continue
            
            # Traduzir título
            title_en = project.title
            for pt_word, en_word in sample_translations['title_patterns'].items():
                if pt_word.lower() in project.title.lower():
                    title_en = project.title.replace(pt_word, en_word)
                    break
            
            # Traduzir descrição
            description_en = project.description
            for pt_phrase, en_phrase in sample_translations['description_replacements'].items():
                description_en = description_en.replace(pt_phrase, en_phrase)
            
            # Se não conseguiu traduzir automaticamente, usar texto genérico
            if title_en == project.title:
                title_en = f"{project.title} (English version)"
            
            if description_en == project.description:
                description_en = f"English description for {project.title}. This is a sample translation - please update with actual content."
            
            # Atualizar projeto
            project.title_en = title_en
            project.description_en = description_en
            project.save()
            
            updated_count += 1
            self.stdout.write(f"[OK] Adicionada tradução para: {project.title}")
        
        if updated_count > 0:
            self.stdout.write(
                self.style.SUCCESS(f'\nSucesso! {updated_count} projetos atualizados com traduções.')
            )
            self.stdout.write(
                self.style.WARNING('Nota: As traduções são exemplos genéricos. Acesse o Django Admin para editá-las.')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('Todos os projetos já possuem traduções!')
            )