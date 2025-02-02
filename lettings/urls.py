from django.urls import path

from . import views

"""
URL configuration for the lettings app.

Defines the URL patterns for the lettings application, linking views to specific paths.

Variables:
    urlpatterns (list): A list of URL patterns for the lettings app.
"""

app_name = "lettings"
urlpatterns = [
    path("lettings/", views.lettings_index, name="lettings_index"),
    path("lettings/<int:letting_id>/", views.letting, name="letting"),
]
