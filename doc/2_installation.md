# Instructions d'Installation

## Prérequis

- Git,
- Python 3.12+,
- Sentry,
- Docker (pour le déploiement)

## Étapes Installation

1. Cloner le repository dans le répertoire de votre choix :

   ```bash
   git clone https://github.com/AdeVedA/OCLettings--OCR_Mission12.git
   cd OCLettings--OCR_Mission12
   ```

2. Créer un environnement virtuel:
   ```bash
   python -m venv venv # pour Windows | pour Linux : `python3 -m venv venv`
   venv\Scripts\activate # pour Windows | pour Linux : `source env/bin/activate` 
   ```

3. Installer les dépendances dans cet environnement activé:
   ```bash
   pip install -r requirements.txt
   ```

4. Configurer les variables d'environnement dans un fichier à la racine du projet `.env` :
   ```ini
   # Django settings
   DEBUG=False
   SECRET_KEY="votre secret_key django"
   ALLOWED_HOSTS=localhost,127.0.0.1,{votre nom de domaine de production}
   DJANGO_CSRF_TRUSTED_ORIGINS=https://localhost:8000,{votre url de production}

   # Database settings
   DATABASE_ENGINE='sqlite3'
   DATABASE_NAME='oc-lettings-site.sqlite3'

   # Sentry DSN
   SENTRY_DSN='{votre dsn sentry pour le projet}'
   ```

5. Migrations et lancement du server :
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```