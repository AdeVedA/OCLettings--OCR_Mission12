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
   - Mettez-vous à la racine du projet, activez l'environnement virtuel puis :
   ```bash
   # pour vérifier le linting :
   flake8
   ```

   ```bash
   # pour éxecuter les tests (unitaires & intégration):
   pytest
   ```
