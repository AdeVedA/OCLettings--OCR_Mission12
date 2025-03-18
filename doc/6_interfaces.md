# Interface de Programmation

## URLs Disponibles

### Lettings App

| Route | Vue associée | Description |
|-------|---------------|-------------|
| `/lettings/` | `index` | Liste toutes les locations |
| `/lettings/<int:letting_id>/` | `letting` | Détails d'une location spécifique |

### Profiles App

| Route | Vue associée | Description |
|-------|---------------|-------------|
| `/profiles/` | `index` | Liste des profils utilisateurs |
| `/profiles/<int:profile_id>/` | `profile` | Profil utilisateur détaillé |
