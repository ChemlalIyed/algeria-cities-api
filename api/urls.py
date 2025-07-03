from django.urls import path
from .views import Wilaya,All
urlpatterns = [
    path('',All.as_view({'get': 'list'})),
    path('<int:num>/',Wilaya.as_view())
]
