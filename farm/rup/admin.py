
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Pesticide, Applicator, Name, Location, LocationPesticide, LocationManager


admin.site.register(Pesticide)
admin.site.register(Applicator)
admin.site.register(Name)
admin.site.register(Location)
admin.site.register(LocationPesticide)
admin.site.register(LocationManager)


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Name
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
