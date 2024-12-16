from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from winemanager.models import WineBottle, Winemaker
from winemanager.serializers import WinemakerSerializer, WineBottleSerializer


class WinemakerViewSet(viewsets.ModelViewSet):
    """
    Standard Django Viewset providing default actions for Winemaker model.

    GET /api/winemakers/ - List all winemakers
    POST /api/winemakers/ - Create a new winemaker
    GET /api/winemakers/{id}/ - Retrieve a winemaker by id
    PUT /api/winemakers/{id}/ - Update a winemaker by id
    DELETE /api/winemakers/{id}/ - Delete a winemaker by id
    """

    queryset = Winemaker.objects.all()
    serializer_class = WinemakerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name", "address"]
    ordering_fields = ["name"]


class WineBottleViewSet(viewsets.ModelViewSet):
    """
    Standard Viewset providing default actions for WineBottle model.

    Additional custom action `by_winemaker` is added to list all wine bottles from a given winemaker.

    GET /api/winebottles/ - List all wine bottles
    POST /api/winebottles/ - Create a new wine bottle
    GET /api/winebottles/{id}/ - Retrieve a wine bottle by id
    PUT /api/winebottles/{id}/ - Update a wine bottle by id
    DELETE /api/winebottles/{id}/ - Delete a wine bottle by id
    """

    queryset = WineBottle.objects.all()
    serializer_class = WineBottleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["style", "year", "winemaker"]
    search_fields = ["name", "taste", "description"]
    ordering_fields = ["year", "name", "count_in_winecellar"]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    @action(detail=False, methods=["get"])
    def by_winemaker(self, request):
        winemaker_id = request.query_params.get("winemaker_id")
        if winemaker_id:
            wines = WineBottle.objects.filter(winemaker_id=winemaker_id)
            serializer = self.get_serializer(wines, many=True)
            return Response(serializer.data)
        return Response({"error": "winemaker_id is required"}, status=400)
