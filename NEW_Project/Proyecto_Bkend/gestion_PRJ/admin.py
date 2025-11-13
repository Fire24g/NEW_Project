from django.contrib import admin

from . import models


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'empresa', 'correo', 'telefono')
    search_fields = ('nombre', 'empresa', 'correo')


@admin.register(models.Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'rol', 'correo')
    search_fields = ('nombres', 'apellidos', 'correo')
    list_filter = ('rol',)


@admin.register(models.Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cliente', 'estado', 'fecha_inicio', 'fecha_termino')
    list_filter = ('estado', 'cliente')
    search_fields = ('nombre', 'cliente__nombre')
    autocomplete_fields = ('cliente',)


@admin.register(models.Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'proyecto', 'lider')
    search_fields = ('nombre', 'proyecto__nombre')
    autocomplete_fields = ('proyecto', 'lider', 'miembros')


@admin.register(models.Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'proyecto', 'estado', 'prioridad', 'fecha_vencimiento', 'asignado_a')
    list_filter = ('estado', 'prioridad', 'proyecto')
    search_fields = ('titulo', 'proyecto__nombre', 'asignado_a__nombres', 'asignado_a__apellidos')
    autocomplete_fields = ('proyecto', 'asignado_a')
