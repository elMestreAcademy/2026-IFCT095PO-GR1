# Django

## 7) Core

- **Concepto MVT**: Model–Template–View; diferencias con MVC.
- **Creación de proyecto y apps**: `django-admin startproject`, `manage.py startapp`.
- **Estructura de directorios de Django**: `settings.py`, `urls.py`, `wsgi.py/asgi.py`.
- **Settings**: `INSTALLED_APPS`, `MIDDLEWARE`, `TEMPLATES`, `DATABASES`, `LANGUAGE_CODE`, `TIME_ZONE`, `USE_TZ`.
- **URLs y views**: funciones vs **Class‑Based Views** (CBV); `path`, `re_path`, `include`.
- **Templates**: motor de plantillas, contexto, filtros/etiquetas.
- **Modelos y ORM**: campos, relaciones (**FK**, **ManyToMany**, **OneToOne**), **migraciones** (`makemigrations/migrate`).
- **Admin**: registro de modelos, personalización básica.
- **Formularios**: `forms.Form`/`ModelForm`, validación, mensajes.
- **Autenticación y autorización**: User model, **login/logout**, permisos y grupos, decoradores (`login_required`, `permission_required`).
- **Archivos estáticos y media**: `STATIC_URL`, `STATICFILES_DIRS`, `collectstatic`; `MEDIA_URL/MEDIA_ROOT`.
- **Middleware** y **señales** (signals) básicas.
- **i18n/l10n**: **`LANGUAGE_CODE`**, **traducciones** (`gettext`), formatos; **Time Zone**.
- **Testing en Django**: `TestCase`, client de pruebas; *opcional*: **pytest‑django**.

---

## 8) APIs y tiempo real (opcionales, según tiempo)

- **Django REST Framework (DRF)**: serializers, viewsets, routers, paginación, permisos, throttling.
- **Autenticación para APIs**: tokens, JWT (nociones), CORS.
- **Django Channels / WebSockets** (muy opcional): conceptos y demo mínima.

---

## 9) Seguridad (imprescindibles)

- **Gestión de secretos** y `.env`.
- **Hashing de contraseñas**, salting; no almacenar texto plano.
- **TLS/HTTPS** (nociones; el cifrado asimétrico se explica a alto nivel).
- **CSRF/XSS/Clickjacking** en Django y cómo lo mitiga.
- **Validación y sanitización**.

---

## 10) Calidad, registros y observabilidad

- **Formateo y linting**: Black, isort, flake8/ruff.
- **Logging** en Django: configuración básica, handlers.
- **Cobertura** de pruebas (coverage) y pipeline simple de CI (GitHub Actions).

---

## 11) Despliegue y operaciones

- **WSGI/ASGI**: Gunicorn/Uvicorn.
- **Servidor web**: Nginx como reverse proxy (nociones).
- **Base de datos en producción**: Postgres + variables de entorno.
- **Static/media en prod**: `collectstatic`, CDN o S3 (conceptos).
- **Docker** (opcional): contenedores para dev/prod.
- **12‑Factor App** aplicado a Django (resumen).

---

## 12) Proyecto integrador (entregable)

- Backlog con historias (autenticación, CRUD, permisos, formularios, seed de datos).
- Hitos: MVP local → pruebas → despliegue de demo.
- Rúbrica: funcionalidad, código, pruebas, documentación, *readme*, despliegue.
