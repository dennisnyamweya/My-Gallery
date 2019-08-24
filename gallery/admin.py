from django.contrib import admin
from .models import Category,Picture

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category,CategoryAdmin)


class PictureAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','category', 'location', 'created', 'updated']
    list_filter = [ 'created', 'updated','category']
    list_editable = ['location','category']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Picture,PictureAdmin)