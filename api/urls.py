from django.urls import path
from .views import ifPlace 

urlpatterns = [
        path('<str:place>', ifPlace.as_view(), name='tf'),
        ]
