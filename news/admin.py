from django.contrib import admin
from .models import News_model

class NewsAdmin(admin.ModelAdmin):
    list_display=('header','text', 'created_at', 'changed_at', 'is_published')
    list_display_links = ('header', 'text')
    search_fields = ('header', 'text')

  
admin.site.register(News_model, NewsAdmin) # order is important
# Register your models here.
