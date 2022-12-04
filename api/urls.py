from django.urls import include, path
from django.views.generic import TemplateView
from .views import PlaceViewSet, IfPlace, GetPlace, GetList, AddPlace
from rest_framework import routers

router = routers.SimpleRouter()
router.register("places", PlaceViewSet)

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("<str:place>", IfPlace.as_view(), name="tf"),
    path("get/<str:letter>", GetPlace.as_view(), name="getplace"),
    path("list/<str:letter>", GetList.as_view(), name="listplace"),
    path("create/<str:place>", AddPlace.as_view(), name="createplace"),
    path("api/", include(router.urls), name="places"),
]
