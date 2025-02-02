from django.urls import path

from . import views

"""
URL configuration for the profiles app.

Defines the URL patterns for the profiles application, linking views to specific paths.

Variables:
    urlpatterns (list): A list of URL patterns for the profiles app.
"""

app_name = "profiles"
urlpatterns = [
    path("profiles/", views.profiles_index, name="profiles_index"),
    path("profiles/<str:username>/", views.profile, name="profile"),
]
