from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Algeria_cities
from .serializer import Algeria_cities_Serializer
from rest_framework.views import Response,APIView
class All(ModelViewSet):
    queryset=Algeria_cities.objects.all()
    serializer_class=Algeria_cities_Serializer
class Wilaya(APIView):
    def get(self,request,num):
       try: 
        ret = Algeria_cities.objects.filter(wilaya_code=num)
        ser=Algeria_cities_Serializer(ret,many=True)
        return Response(ser.data)
       except Exception as e:
          return Response({"error":str(e)})