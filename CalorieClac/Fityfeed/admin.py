from django.contrib import admin
from .models import *
# Register your models here.

class ComidaAdmin(admin.ModelAdmin):
    class Meta:
        model=ComidaItem
    list_display=['nombre']
    list_filter=['nombre']

admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(UsuarioComidaitem)
admin.site.register(ComidaItem, ComidaAdmin)