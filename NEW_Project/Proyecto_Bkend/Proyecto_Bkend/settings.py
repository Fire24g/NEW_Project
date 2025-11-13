"""
Configuración de Django para el proyecto Proyecto_Bkend.

Generado por 'django-admin startproject' usando Django 5.2.8.

Para más información sobre este archivo visita
https://docs.djangoproject.com/en/5.2/topics/settings/

Para ver la lista completa de ajustes y sus valores consulta
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os
from django.core.exceptions import ImproperlyConfigured

# Construye rutas dentro del proyecto como BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def load_env_file() -> None:
    """Carga un archivo .env local si está disponible.

    El proyecto prioriza el archivo junto a settings.py, pero también revisa los
    directorios superiores para permitir el uso del `.env` ubicado en la raíz
    del repositorio durante el desarrollo.
    """

    candidate_paths = [
        BASE_DIR / ".env",
        BASE_DIR.parent / ".env",
        BASE_DIR.parent.parent / ".env",
    ]

    for env_path in candidate_paths:
        if env_path.exists():
            with env_path.open() as env_file:
                for line in env_file:
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    key, value = line.split("=", 1)
                    os.environ.setdefault(key.strip(), value.strip())
            break


def get_env(name: str, default: str | None = None, *, required: bool = False) -> str | None:
    """Obtiene una variable de entorno y permite exigir su presencia."""

    value = os.environ.get(name, default)
    if required and value is None:
        raise ImproperlyConfigured(
            f"Falta definir la variable de entorno obligatoria: {name}"
        )
    return value


load_env_file()

# Configuración rápida para desarrollo: no es apta para producción
# Revisa https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# ADVERTENCIA: mantén secreta la clave usada en producción.
SECRET_KEY = get_env("DJANGO_SECRET_KEY", "coloca-una-clave-segura")

# ADVERTENCIA: no ejecutes con debug activo en producción.
DEBUG = get_env("DJANGO_DEBUG", "False").lower() in {"1", "true", "yes"}

ALLOWED_HOSTS = [
    host.strip() for host in get_env("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",") if host.strip()
]


# Definición de aplicaciones instaladas

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestion_PRJ',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Proyecto_Bkend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Proyecto_Bkend.wsgi.application'


# Configuración de la base de datos
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / get_env('DJANGO_DB_PATH', 'db.sqlite3'),
    }
}


# Validación de contraseñas
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internacionalización
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# Archivos estáticos (CSS, JavaScript, imágenes)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Tipo de clave primaria por defecto
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
