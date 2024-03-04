from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.client.models import ClientCategory


@admin.register(ClientCategory)
class ClientCategoryAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name')
