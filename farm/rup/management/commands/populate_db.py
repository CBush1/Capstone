from django.core.management.base import BaseCommand
import requests
import json
from rup.models import Pesticide

class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get("https://data.oregon.gov/resource/az53-86zj.json")
        data = json.loads(response.text)
        for i in range(len(data)):
            registrant_name = data[i]['registrant_name']
            product_name = data[i]['product_name']
            epa_number = data[i]['epa_no']
            active_ingredient = data[i]['active_ingredient']
            reason_for_restricted_use_classification = data[i]['reason_for_restricted_use_classification']


            pesticide = Pesticide(registrant_name=registrant_name,
                                    product_name=product_name,
                                    epa_number=epa_number,
                                    rui=reason_for_restricted_use_classification,
                                    active_ingredient=active_ingredient,
                                    )
            pesticide.save()
