from django.contrib import admin

from proyectos.models import Proyecto, Tarea

class TareaInline(admin.StackedInline):
    model = Tarea
    extra = 0

class ProyectoAdmin(admin.ModelAdmin):
    fields = ['nombre', 'fecha_pub']
    inlines = [TareaInline]
    list_display = ('nombre', 'fecha_pub')
    list_filter = ['fecha_pub']
    search_fields = ['nombre']

admin.site.register(Proyecto, ProyectoAdmin)
