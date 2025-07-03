from rest_framework.serializers import Serializer,ModelSerializer
from .models import Algeria_cities
class Algeria_cities_Serializer(ModelSerializer):
    class Meta:
        model=Algeria_cities
        fields="__all__"