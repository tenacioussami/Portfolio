from django.contrib import admin
from django.utils.html import format_html
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'thumbnail', 'created_at')
    list_filter = ('technology',)
    search_fields = ('title', 'technology', 'short_description')
    ordering = ('-created_at',)

    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'short_description', 'technology')
        }),
        ('Details', {
            'fields': ('description', 'github_link', 'image')
        }),
    )

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:40px; border-radius:4px;" />', obj.image.url)
        return "—"
    thumbnail.short_description = 'Image'
