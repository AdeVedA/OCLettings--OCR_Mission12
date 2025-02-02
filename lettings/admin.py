from django.contrib import admin

from .models import Address, Letting

"""
Admin configuration for the lettings app.

Registers the Address and Letting models to the admin interface for management.
"""

admin.site.register(Letting)
admin.site.register(Address)
