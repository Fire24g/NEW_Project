# Generado manualmente para definir el esquema inicial de gestion_PRJ
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=30)),
                ('empresa', models.CharField(blank=True, max_length=120)),
            ],
            options={'ordering': ['nombre']},
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=120)),
                ('apellidos', models.CharField(max_length=120)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('rol', models.CharField(choices=[('ANALISTA', 'Analista'), ('DESARROLLADOR', 'Desarrollador'), ('QA', 'QA'), ('LIDER', 'Líder de proyecto'), ('UX', 'Diseñador UX')], max_length=20)),
            ],
            options={'ordering': ['apellidos', 'nombres']},
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('PLANIFICACION', 'Planificación'), ('EN_PROGRESO', 'En progreso'), ('BLOQUEADO', 'Bloqueado'), ('FINALIZADO', 'Finalizado')], default='PLANIFICACION', max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='gestion_PRJ.cliente')),
            ],
            options={'ordering': ['-fecha_inicio', 'nombre']},
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('EN_PROGRESO', 'En progreso'), ('COMPLETADA', 'Completada'), ('BLOQUEADA', 'Bloqueada')], default='PENDIENTE', max_length=20)),
                ('prioridad', models.CharField(choices=[('BAJA', 'Baja'), ('MEDIA', 'Media'), ('ALTA', 'Alta')], default='MEDIA', max_length=10)),
                ('asignado_a', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tareas', to='gestion_PRJ.empleado')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='gestion_PRJ.proyecto')),
            ],
            options={'ordering': ['fecha_vencimiento', 'prioridad']},
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('lider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipos_liderados', to='gestion_PRJ.empleado')),
                ('miembros', models.ManyToManyField(blank=True, related_name='equipos', to='gestion_PRJ.empleado')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipos', to='gestion_PRJ.proyecto')),
            ],
            options={'ordering': ['nombre']},
        ),
    ]
