# Guide d'Utilisation

## Cas d'utilisation typiques


1. **Visiteur** :

   - Accès à la page d'accueil (`/`).
   - Navigation vers `/lettings/` pour voir une liste des locations, puis en découvrir les détails par simple clic sur l'une d'elles.
   - Navigation vers `/profiles/` pour voir une liste des profils d'utilisateurs, puis en découvrir les détails par simple clic sur l'un d'eux.

2. **Administrateur** :

   - Gestion des lettings et profiles via l'interface admin Django `/admin/`.
   - Validation de nouveaux profils ou mises à jour des listings.

3. **Développeur** :

   ```bash
   # Exécuter les tests
   pytest --cov=lettings --cov=profiles --cov-report=html

   # Vérifier le linting
   flake8 oc_lettings_site lettings profiles
   ```