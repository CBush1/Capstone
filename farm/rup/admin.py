
from django.contrib import admin
from .models import Pesticide, Applicator, Name
# admin.site.register(Pesticide, PesticideAdmin)
admin.site.register(Applicator)
admin.site.register(Name)

class PesticideAdmin(admin.ModelAdmin):
    fieldsests = [
        (None,                  {'fields':
        ['use']}),
                ('Product Used', {'fields':
        ['product_name']}),
    ]
admin.site.register(Pesticide, PesticideAdmin)
