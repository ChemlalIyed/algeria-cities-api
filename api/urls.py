from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Wilaya,All,Wilaya_list
router = DefaultRouter()
router.register('',Wilaya_list)
urlpatterns = [
    path('v1/communes/',All.as_view({'get': 'list'})),
    path('v1/wilayas/communes/<int:num>',Wilaya.as_view()),
    path('v1/wilayas/',include(router.urls))
]
