from django.contrib import admin
from .models import Recipes

class RecipesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'updated_at']
    list_filter = ['title', 'price', 'created_at']
admin.site.register(Recipes, RecipesAdmin)
# Register your models here.
