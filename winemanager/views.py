from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from winemanager.models import WineBottle, Winemaker
from winemanager.serializers import WinemakerSerializer, WineBottleSerializer


class WinemakerViewSet(viewsets.ModelViewSet):
    queryset = Winemaker.objects.all()
    serializer_class = WinemakerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name", "address"]
    ordering_fields = ["name"]


class WineBottleViewSet(viewsets.ModelViewSet):
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
