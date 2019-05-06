from django.core.management.base import BaseCommand
import requests
import json
from rup.models import Pesticide

class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get("https://data.oregon.gov/resource/az53-86zj.json?$$app_token=XGAD8q6M7qOimb3nCwDhG4e0P")
        data = json.loads(response.text)
        for i in range(len(data)):
            product_name = data[i]['product_name']
            epa_number = data[i]['epa_no']
            reason_for_restricted_use_classification = data[i]['reason_for_restricted_use_classification']

            pesticide = Pesticide(product_name=product_name,
                                    epa_number=epa_number,
                                    rui=reason_for_restricted_use_classification)
            pesticide.save()
