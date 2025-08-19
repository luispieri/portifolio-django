from django.contrib import admin
from .models import ContactInfo, Project, Experience, Skill, ContactMessage

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'location', 'available_for_work')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('email', 'phone', 'location', 'bio')
        }),
        ('Redes Sociais', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url')
        }),
        ('Disponibilidade', {
            'fields': ('available_for_work',)
        }),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'status', 'featured', 'order')
    list_filter = ('status', 'featured', 'year')
    search_fields = ('title', 'description')
    list_editable = ('featured', 'order')
    ordering = ('order', '-year')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'description', 'year', 'status')
        }),
        ('Detalhes Técnicos', {
            'fields': ('technologies', 'project_url', 'github_url', 'image')
        }),
        ('Configurações de Exibição', {
            'fields': ('featured', 'order')
        }),
    )

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start_year', 'end_year', 'current', 'order')
    list_filter = ('current', 'start_year')
    search_fields = ('company', 'role')
    list_editable = ('order',)
    ordering = ('-start_year',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level', 'order')
    list_filter = ('category',)
    search_fields = ('name',)
    list_editable = ('level', 'order')
    ordering = ('category', 'order')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'read')
    list_filter = ('read', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = "Marcar como lida"
    
    actions = [mark_as_read]