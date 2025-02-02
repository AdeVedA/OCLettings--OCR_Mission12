from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration class for the profiles application.

    Attributes:
        default_auto_field (str): The default type for auto-created primary keys.
        name (str): The name of the application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"
