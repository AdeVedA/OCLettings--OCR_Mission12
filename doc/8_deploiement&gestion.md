# procédures de déploiement et de gestion de l'application


## Procédures de Déploiement

### Pipeline CI/CD (GitHub Actions)

1. **Lint & Tests** :
   ```yaml
   jobs:
     lint-and-test:
       name: Tests et Validation
       runs-on: ubuntu-latest
       steps:
         - name: récupérer le code du repo
           uses: actions/checkout@v4
   
         - name: Configuration Python
           uses: actions/setup-python@v4
           with:
             python-version: "3.12"
   
         - name: Installation des dépendances
           run: |
             python -m pip install --upgrade pip
             pip install -r requirements.txt
   
         - name: Linting avec flake8
           run: flake8 .
   
         - name: Tests avec pytest
           run: |
             pytest --maxfail=1 --disable-warnings -q
             pytest --cov=src --cov-report=term-missing --cov-fail-under=90
           env:
             SENTRY_DSN: "${{ secrets.SENTRY_DSN }}"
             SECRET_KEY: "${{ secrets.SECRET_KEY_DJANGO }}"
   ```

2. **Build & push** :
   ```yaml
     build-and-push:
       name: Build de l'image et push sur dockhub
       runs-on: ubuntu-latest
       needs: lint-and-test
   
       steps:
         - name: récupérer le repo
           uses: actions/checkout@v3
   
         - name: set up docker buildx
           uses: docker/setup-buildx-action@v2
     
         - name: log in to docker hub
           uses: docker/login-action@v2
           with:
             username: ${{ secrets.DOCKERHUB_USERNAME }}
             password: ${{ secrets.DOCKERHUB_PASSWORD }}
   
         - name: build the docker image
           run: |
             docker build \
               --build-arg SENTRY_DSN="${{ secrets.SENTRY_DSN }}" \
               --build-arg SECRET_KEY_DJANGO="${{ secrets.SECRET_KEY_DJANGO }}" \
               -t "${{ secrets.DOCKER_IMAGE_NAME }}:${{ github.sha }}" .
       
         - name: push docker image to docker hub
           run: docker push ${{ secrets.DOCKER_IMAGE_NAME }}:${{ github.sha }}
   ```

   avec pour dockerfile :
   ```Dockerfile
   # Utiliser une image Python officielle comme image de base
   FROM python:3.12-slim

   # Définir des variables d'environnement (pas générer de __pycache__ et logs directs en terminal)
   ENV PYTHONDONTWRITEBYTECODE=1 \
      PYTHONUNBUFFERED=1

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
   ENV ALLOWED_HOSTS=localhost,127.0.0.1,oc-lettings-yua5.onrender.com
   ENV DJANGO_CSRF_TRUSTED_ORIGINS=https://localhost,https://oc-lettings-yua5.onrender.com
   ENV DATABASE_ENGINE=sqlite3
   ENV DATABASE_NAME=oc-lettings-site.sqlite3

   # Collecter les fichiers statiques pour whitenoise
   RUN python manage.py collectstatic --noinput

   # Exposer le port sur lequel s'exécute l'application
   EXPOSE 8000

   # Commande pour démarrer l'application
   CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
   ```


3. **Déploiement sur Render** :
   ```yaml
     deploy:
       name: Déploiement sur Render
       runs-on: ubuntu-latest
       needs: build-and-push
   
       steps:
         - name: Déclencher le déploiement sur Render
           run: curl "${{secrets.RENDER_HOOK}}:${{ github.sha }}"
   ```
---

## Procédures Manuelles

1. **Lancer le conteneur** :
   ```bash
   docker run --name oc_lettings_container \
     -e SENTRY_DSN=$SENTRY_DSN \
     -p 8000:8000 [dockerhub-user]/oc-lettings:[tag]
   ```

2. **Monitoring avec Sentry** :
- Activer le SDK dans `settings.py` :
```python
import sentry_sdk

sentry_sdk.init(
    dsn=f"{os.getenv('SENTRY_DSN')}",
    send_default_pii=True,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
```