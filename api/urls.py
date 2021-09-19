from django.urls import path
from django.views.generic import TemplateView
from .views import ifPlace, getPlace, getList, addPlace

urlpatterns = [
        path('', TemplateView.as_view(template_name='index.html'), name='index'),
        path('<str:place>', ifPlace.as_view(), name='tf'),
        path('get/<str:letter>', getPlace.as_view(), name='getplace'),
        path('list/<str:letter>', getList.as_view(), name='listplace'),
        path('create/<str:place>', addPlace.as_view(), name='createplace'),
        ]
