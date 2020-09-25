from shoes import models
from rest_framework import serializers

class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ['name', 'website']

class ShoeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ShoeType
        fields = ['style']

class ShoeColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ShoeColor
        fields = ['color_name']

class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Shoe
        fields = ['size', 'brandname', 'manufacturer', 'color', 'material', 'shoe_type', 'fasten_type']