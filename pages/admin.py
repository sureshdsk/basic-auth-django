from django.contrib import admin

from .models import Page

class PagesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"page_slug": ("page_title",)}
    fields = ['page_title', 'page_slug', 'published_date', 'page_content','is_private']

admin.site.register(Page,PagesAdmin)