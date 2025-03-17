# Description du Projet

![OrangeCountyLettings_Ad](https://user.oc-static.com/upload/2023/07/20/1689880374259_Orange%20County%20Lettings%20Ad.png)

**OC Lettings** est une **application web Django** permettant de lister des *locations immobilières* et de présenter les *profils utilisateurs*.

La version 2.0.0 (https://oc-lettings-yua5.onrender.com/) est le résultat de ces spécifications/modifications :

## Étape 1 : Améliorer l’architecture modulaire

   - Séparation en **trois applications** (`oc_lettings_site`, `lettings`, `profiles`)
   - **Migration des données** et gestion restructurée des **templates et URLs**.

## Étape 2 : Réduire les divers problèmes sur le projet

   - Correction de **bugs**,
   - Amélioration du **linting**,
   - Gestion des **erreurs 404 et 500** avec pages aux *images personnalisées*,
   - Écriture des **tests unitaires et d'intégration**,
   - **Docstrings et documentation** complète.

## Étape 3 : Surveiller l’application et ses erreurs via Sentry

   - Détection et suivi/monitoring centralisé des erreurs avec logs structurés.

## Étape 4 : Mettre en place le pipeline CI/CD et le déploiement

Lors du commit/push sur la branche github main du projet, ce workflow permet l'automatisation : 

1. de la validation du **linting** flake8 et des **tests** pytest (avec validation pour une couverture supérieure à 80%),

2. du **build Docker** et du push de l'image versionnée sur **DockerHub**,

3. du **déploiement** sur Render.

## Étape 5 : Documenter l’application

   - Génération de la documentation via Sphinx 
   - Déploiement sur Read the Docs.
