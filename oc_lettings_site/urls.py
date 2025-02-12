# from django.conf import settings
from django.contrib import admin

# from django.http import Http404
from django.urls import include, path

from . import views

# from django.views.defaults import page_not_found, server_error


urlpatterns = [
    path("", views.index, name="index"),
    path("", include("profiles.urls")),
    path("", include("lettings.urls")),
    path("admin/", admin.site.urls),
]


# Assigning these views to the Django handlers
handler404 = "oc_lettings_site.views.custom_404_view"
handler500 = "oc_lettings_site.views.custom_500_view"

"""
if settings.DEBUG:
    urlpatterns += [
        path("404/", page_not_found, {"exception": Http404()}),
        path("500/", server_error),
    ]
"""
