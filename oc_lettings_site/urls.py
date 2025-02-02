from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", include("profiles.urls")),
    path("", include("lettings.urls")),
    path("admin/", admin.site.urls),
]


# Assigning these views to the Django handlers
handler404 = "oc_lettings_site.views.custom_404_view"
handler500 = "oc_lettings_site.views.custom_500_view"
