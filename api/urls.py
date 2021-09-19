from django.urls import path
from .views import ifPlace, getPlace 

urlpatterns = [
        path('<str:place>', ifPlace.as_view(), name='tf'),
        path('letter/<str:letter>', getPlace.as_view(), name='getplace'),
        ]
