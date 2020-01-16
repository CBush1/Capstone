"""As i Add things here, write a comment explaining what
it does so i don't comment out imporant things that break the code.

If something is always commented out, just delete it."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Pesticide, Name, Location, LocationPesticide, UserProfile, Formulation


admin.site.register(Pesticide)
admin.site.register(Name)
admin.site.register(Location)
admin.site.register(LocationPesticide)
admin.site.register(UserProfile)
admin.site.register(Formulation)
