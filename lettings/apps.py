from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Configuration class for the lettings app.

    Attributes:
        default_auto_field (str): Specifies the type of auto field to use for primary keys.
        name (str): The name of the application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "lettings"
