from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Empleado, Proyecto, Tarea


class HomeView(TemplateView):
    template_name = 'gestion_PRJ/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'proyectos_count': Proyecto.objects.count(),
                'empleados_count': Empleado.objects.count(),
                'tareas_abiertas': Tarea.objects.exclude(estado=Tarea.Estado.COMPLETADA).count(),
            }
        )
        return context


class ProyectoListView(ListView):
    model = Proyecto
    template_name = 'gestion_PRJ/proyecto_list.html'
    context_object_name = 'proyectos'


class ProyectoCreateView(CreateView):
    model = Proyecto
    fields = ['nombre', 'descripcion', 'cliente', 'fecha_inicio', 'fecha_termino', 'estado']
    template_name = 'gestion_PRJ/proyecto_form.html'
    success_url = reverse_lazy('gestion:proyecto_list')


class ProyectoUpdateView(UpdateView):
    model = Proyecto
    fields = ['nombre', 'descripcion', 'cliente', 'fecha_inicio', 'fecha_termino', 'estado']
    template_name = 'gestion_PRJ/proyecto_form.html'
    success_url = reverse_lazy('gestion:proyecto_list')


class ProyectoDeleteView(DeleteView):
    model = Proyecto
    template_name = 'gestion_PRJ/proyecto_confirm_delete.html'
    success_url = reverse_lazy('gestion:proyecto_list')


class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'gestion_PRJ/empleado_list.html'
    context_object_name = 'empleados'


class EmpleadoCreateView(CreateView):
    model = Empleado
    fields = ['nombres', 'apellidos', 'correo', 'rol']
    template_name = 'gestion_PRJ/empleado_form.html'
    success_url = reverse_lazy('gestion:empleado_list')


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    fields = ['nombres', 'apellidos', 'correo', 'rol']
    template_name = 'gestion_PRJ/empleado_form.html'
    success_url = reverse_lazy('gestion:empleado_list')


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'gestion_PRJ/empleado_confirm_delete.html'
    success_url = reverse_lazy('gestion:empleado_list')


class TareaListView(ListView):
    model = Tarea
    template_name = 'gestion_PRJ/tarea_list.html'
    context_object_name = 'tareas'


class TareaCreateView(CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'proyecto', 'asignado_a', 'fecha_vencimiento', 'estado', 'prioridad']
    template_name = 'gestion_PRJ/tarea_form.html'
    success_url = reverse_lazy('gestion:tarea_list')


class TareaUpdateView(UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'proyecto', 'asignado_a', 'fecha_vencimiento', 'estado', 'prioridad']
    template_name = 'gestion_PRJ/tarea_form.html'
    success_url = reverse_lazy('gestion:tarea_list')


class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = 'gestion_PRJ/tarea_confirm_delete.html'
    success_url = reverse_lazy('gestion:tarea_list')
