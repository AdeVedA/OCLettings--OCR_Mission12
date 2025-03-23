# Guide de Démarrage Rapide

## Lancer le site localement

```bash
python manage.py runserver
```

Accédez à `http://localhost:8000` pour la page d'accueil et `/admin/` pour l'interface administrateur.

## Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### ou Création d'un superutilisateur (Admin)

```bash
python manage.py createsuperuser
# Saisir email et mot de passe lors des prompts
```