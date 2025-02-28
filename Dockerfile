# Utiliser une image Python officielle comme image de base
FROM python:3.12-slim

# Définir des variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install gunicorn

# Copier le projet
COPY . /app/

# Arguments de build définis dans votre workflow GitHub Actions
ARG SENTRY_DSN
ARG SECRET_KEY_DJANGO

# Définir les variables d'environnement
ENV SENTRY_DSN=${SENTRY_DSN}
ENV SECRET_KEY=${SECRET_KEY_DJANGO}
ENV DEBUG=0
ENV ALLOWED_HOSTS=localhost,127.0.0.1
ENV DJANGO_CSRF_TRUSTED_ORIGINS=https://localhost
ENV DATABASE_ENGINE=sqlite3
ENV DATABASE_NAME=oc-lettings-site.sqlite3

# Collecter les fichiers statiques pour whitenoise
RUN python manage.py collectstatic --noinput

# Exposer le port sur lequel s'exécute l'application
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]