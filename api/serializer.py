from rest_framework.serializers import Serializer,ModelSerializer
from .models import Algeria_cities,Algeria_Wilaya
class Algeria_cities_Serializer(ModelSerializer):
    class Meta:
        model=Algeria_cities
        fields=["num","commune_name","commune_name_ascii" ,"daira_name","daira_name_ascii","wilaya_code","wilaya_name","wilaya_name_ascii"]

class Algeria_Wilaya_Serializer(ModelSerializer):
    class Meta:
        model=Algeria_Wilaya
        fields=["wilaya_code","wilaya_name_ascii","wilaya_name"]