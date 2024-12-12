from django.urls import path, include
from winemanager.routers import router


urlpatterns = [
    path("api/", include(router.urls)),
]
