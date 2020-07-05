from django.contrib import admin

# Register your models here.
from .models import Urls

class UrlsAdmin(admin.ModelAdmin):
    list_display = ['original_url', 'id', 'created_date']
    search_fields = ['id', 'original_url', 'shortened_url', 'created_date']
    list_filter = ['created_date']

admin.site.register(Urls, UrlsAdmin)