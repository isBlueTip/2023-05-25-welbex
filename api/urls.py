from django.urls import include, path
from rest_framework import routers

from cargo.views import CargoViewSet
from trucks.views import TruckViewSet

app_name = "api"
router = routers.DefaultRouter()
router.register("cargo", CargoViewSet, basename="cargo")
router.register("trucks", TruckViewSet, basename="trucks")

urlpatterns = [
    path("", include(router.urls)),
]
