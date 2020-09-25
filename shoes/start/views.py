from shoes import models
from rest_framework import viewsets
from shoes.start import serializers

class ManufactuterViewSet(viewsets.ModelViewSet):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer

class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ShoeType.objects.all()
    serializer_class = serializers.ShoeTypeSerializer

class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = models.ShoeColor.objects.all()
    serializer_class = serializers.ShoeColorSerializer

class ShoeViewSet(viewsets.ModelViewSet):
    queryset = models.Shoe.objects.all()
    serializer_class = serializers.ShoeSerializer
