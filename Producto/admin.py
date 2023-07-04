from django.contrib import admin
from .models import Tienda, Modelo, Marca

# Register your models here.
class TiendaAdmin(admin.ModelAdmin):
	readonly_fields=("created","updated")
	
class ModeloAdmin(admin.ModelAdmin):
	readonly_fields=("created","updated")

class MarcaAdmin(admin.ModelAdmin):
	readonly_fields=("created","updated")

admin.site.register(Tienda, TiendaAdmin)

admin.site.register(Modelo, ModeloAdmin)

admin.site.register(Marca, MarcaAdmin)
