from rest_framework import routers
from winemanager.views import WinemakerViewSet, WineBottleViewSet

router = routers.DefaultRouter()
router.register(r"winemakers", WinemakerViewSet)
router.register(r"winebottles", WineBottleViewSet)
