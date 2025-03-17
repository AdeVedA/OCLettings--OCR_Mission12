# Structure de la Base de Données - Modèles Django

## 1. Application `lettings`

### **Address** :

Modèle représentant une adresse.
```python
class Address(models.Model):
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])
```
Attributs :
- number (PositiveIntegerField): Le numéro de la maison ou batiment (maximum 4 digits).
- street (CharField): Le nom de la rue (maximum 64 characters).
- city (CharField): Le nom de la ville (maximum 64 characters).
- state (CharField): Le code de l'état (2 characters).
- zip_code (PositiveIntegerField): Le ZIP code (maximum 5 digits).
- country_iso_code (CharField): Le code ISO du pays (3 characters).

### **Letting** (lié à une `Address` via ForeignKey) :

Modèle représentant une location.
```python
class Letting(models.Model):
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
```
Attributs :
- title (CharField): L'intitulé de la location (maximum 256 characters).
- address (OneToOneField): Une relation one-to-one avec le modèle `Address`.


## 2. Application `profiles`

### **Profile** (lié au `User` Django via OneToOne) :

Modèle représentant un profil utilisateur.
```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)
```
Attributes :
- user (User): Une relation one-to-one avec le modèle `User`.
- favorite_city (str): La ville préférée de l'utilisateur (optionel).