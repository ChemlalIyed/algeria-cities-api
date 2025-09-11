from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .models import Algeria_cities,Algeria_Wilaya
from .serializer import Algeria_cities_Serializer,Algeria_Wilaya_Serializer
from rest_framework.views import Response,APIView
class All(ModelViewSet):
    queryset=Algeria_cities.objects.all()
    serializer_class=Algeria_cities_Serializer

    
class Wilaya(APIView):
    def get(self,request,num):
       if num <=0 or num >58:
          return Response({"error":"there is no wilaya with this number (1-58)"})
       try: 
        ret = Algeria_cities.objects.filter(wilaya_code=num)
        ser=Algeria_cities_Serializer(ret,many=True)
        return Response(ser.data)
       except Exception as e:
          return Response({"error":str(e)})

class Wilaya_list(ModelViewSet):
   serializer_class=Algeria_Wilaya_Serializer
   queryset=Algeria_Wilaya.objects.all().order_by('wilaya_code')
   lookup_field='wilaya_code'
   http_method_names=["get"]