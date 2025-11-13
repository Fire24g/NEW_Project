from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=120)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=30, blank=True)
    empresa = models.CharField(max_length=120, blank=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self) -> str:
        return f"{self.nombre} ({self.empresa or 'Sin empresa'})"


class Empleado(models.Model):
    class Rol(models.TextChoices):
        ANALISTA = 'ANALISTA', 'Analista'
        DESARROLLADOR = 'DESARROLLADOR', 'Desarrollador'
        QA = 'QA', 'QA'
        LIDER = 'LIDER', 'Líder de proyecto'
        UX = 'UX', 'Diseñador UX'

    nombres = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=120)
    correo = models.EmailField(unique=True)
    rol = models.CharField(max_length=20, choices=Rol.choices)

    class Meta:
        ordering = ['apellidos', 'nombres']

    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos}"


class Proyecto(models.Model):
    class Estado(models.TextChoices):
        PLANIFICACION = 'PLANIFICACION', 'Planificación'
        EN_PROGRESO = 'EN_PROGRESO', 'En progreso'
        BLOQUEADO = 'BLOQUEADO', 'Bloqueado'
        FINALIZADO = 'FINALIZADO', 'Finalizado'

    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='proyectos')
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PLANIFICACION)

    class Meta:
        ordering = ['-fecha_inicio', 'nombre']

    def __str__(self) -> str:
        return f"{self.nombre} ({self.get_estado_display()})"


class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='equipos')
    lider = models.ForeignKey(
        Empleado,
        on_delete=models.SET_NULL,
        related_name='equipos_liderados',
        null=True,
        blank=True,
    )
    miembros = models.ManyToManyField(Empleado, related_name='equipos', blank=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self) -> str:
        return f"{self.nombre} - {self.proyecto.nombre}"


class Tarea(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        EN_PROGRESO = 'EN_PROGRESO', 'En progreso'
        COMPLETADA = 'COMPLETADA', 'Completada'
        BLOQUEADA = 'BLOQUEADA', 'Bloqueada'

    class Prioridad(models.TextChoices):
        BAJA = 'BAJA', 'Baja'
        MEDIA = 'MEDIA', 'Media'
        ALTA = 'ALTA', 'Alta'

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    asignado_a = models.ForeignKey(
        Empleado,
        on_delete=models.SET_NULL,
        related_name='tareas',
        null=True,
        blank=True,
    )
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)
    prioridad = models.CharField(max_length=10, choices=Prioridad.choices, default=Prioridad.MEDIA)

    class Meta:
        ordering = ['fecha_vencimiento', 'prioridad']

    def __str__(self) -> str:
        return f"{self.titulo} - {self.get_estado_display()}"
