# Proyecto de Gestión de Proyectos (Back End)

Este proyecto corresponde a la actividad Nº5 de Programación Back End. Implementa una plataforma básica para administrar clientes, proyectos, equipos, empleados y tareas.

## Requisitos previos
- Python 3.11+
- Pipenv o `venv`
- SQLite (incluida por defecto en Python)

## Configuración del entorno
1. Clona el repositorio y entra al directorio raíz:
   ```bash
   git clone <URL-del-repo>
   cd backact
   ```
2. Crea un entorno virtual e instala dependencias:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\\Scripts\\activate
   pip install -r requirements.txt
   ```
   > Si aún no existe `requirements.txt`, puedes crear uno con `pip freeze > requirements.txt` una vez instaladas tus dependencias.
3. Copia `.env.example` a `.env` y ajusta los valores:
   ```bash
   cp .env.example .env
   ```
   - `DJANGO_SECRET_KEY`: genera una clave con `python -c "import secrets; print(secrets.token_urlsafe(50))"`
   - `DJANGO_DEBUG`: `True` para desarrollo, `False` para entrega/producción.
   - `DJANGO_ALLOWED_HOSTS`: dominios o IP permitidos separados por comas.
   - `DJANGO_DB_PATH`: ruta del archivo SQLite (por defecto `db.sqlite3`).

4. Aplica migraciones y carga datos de prueba:
   ```bash
   python NEW_Project/Proyecto_Bkend/manage.py migrate
   python NEW_Project/Proyecto_Bkend/manage.py loaddata gestion_PRJ/fixtures/sample_data.json
   ```

5. Crea un superusuario para el panel de administración:
   ```bash
   python NEW_Project/Proyecto_Bkend/manage.py createsuperuser
   ```

6. Ejecuta el servidor de desarrollo:
   ```bash
   python NEW_Project/Proyecto_Bkend/manage.py runserver
   ```

   El servidor estará disponible en `http://127.0.0.1:8000/`.

## Estructura principal
- `NEW_Project/Proyecto_Bkend/Proyecto_Bkend`: configuración global de Django.
- `NEW_Project/Proyecto_Bkend/gestion_PRJ`: aplicación con modelos, vistas y urls del sistema.
- `templates/`: plantillas HTML para las vistas basadas en clases.
- `gestion_PRJ/fixtures/`: datos de prueba reutilizables.

## CRUD disponibles
Se implementan tres CRUD completos (listar, crear, actualizar, eliminar):
- Proyectos
- Empleados
- Tareas

Cada vista utiliza CBV (`ListView`, `CreateView`, `UpdateView`, `DeleteView`) y protege los formularios mediante tokens CSRF.

## Datos de prueba
`gestion_PRJ/fixtures/sample_data.json` contiene clientes, empleados, proyectos, equipos y tareas con relaciones coherentes. Puedes cargarla con `loaddata` tras ejecutar las migraciones.

## Auditoría y seguridad
- Las credenciales y configuraciones sensibles se leen desde variables de entorno.
- `DEBUG` se controla por variable de entorno para evitar exponer información en entornos compartidos.
- El archivo `db.sqlite3` se excluye del repositorio mediante `.gitignore`.
- Se documentan pasos para crear superusuario sin compartir credenciales.

## Checklist técnico
- `manage.py runserver` se inicia sin errores después de configurar `.env` y migraciones.
- Documentación clara en este README.
- `.env.example` presente.
- 5 entidades con relaciones (`Cliente`, `Proyecto`, `Equipo`, `Empleado`, `Tarea`).
- Administración configurada con filtros, búsqueda y datos precargados.

## Plantilla de reporte para auditoría (Semana 2)
Utiliza la siguiente estructura cuando debas auditar un repositorio de otro equipo:

```
Equipo auditor:
Repo auditado:
URL auditada:
Fecha/hora:

Hallazgo:
- Tipo (CSRF / XSS / Validación / SQL / Settings / Session / Método HTTP)
- Archivo (ruta)
- Descripción breve
- Evidencia (pantalla / log / salida de curl)
- Reproducible (sí/no) y pasos
- Riesgo (Alto/Medio/Bajo)
- Solución propuesta (fragmento de código o explicación)
```

> **Nota:** Este repositorio mantiene la rama `main` alineada con `work` para que el equipo auditor pueda revisar los cambios directamente en la rama principal.

### ¿Cómo sincronizar `work` con `main`?
Sigue estos comandos cada vez que termines una funcionalidad en `work` y quieras que esté disponible también en `main`:

```bash
git checkout work           # asegúrate de estar en la rama de trabajo
git pull                    # trae los últimos cambios remotos de work
git checkout main           # cambia a la rama principal
git pull                    # actualiza main antes de fusionar
git merge work              # fusiona el trabajo confirmado
git push origin main        # publica los cambios en la rama principal remota
```

Si trabajas en equipo, puedes optar por abrir un Pull Request desde `work` hacia `main`. Asegúrate de que todas las pruebas y checklist se hayan ejecutado antes de completar la fusión.

## Próximos pasos sugeridos
- Añadir pruebas unitarias para vistas y modelos.
- Configurar CI/CD para ejecutar `manage.py check` y pruebas.
- Incorporar autenticación para limitar el acceso a formularios en producción.
