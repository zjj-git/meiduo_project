from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ReadOnlyModelViewSet
from areas.models import Area
from . import serializers
from rest_framework_extensions.cache.mixins import CacheResponseMixin


class AreasViewSet(CacheResponseMixin, ReadOnlyModelViewSet):
    """
    list:
    返回所有省份的信息

    retrieve:
    返回特定省或市的下属行政规划区域
    """

    # queryset = Area.objects.all()
    def get_queryset(self):
        if self.action == 'list':
            return Area.objects.filter(parent=None)
        else:
            return Area.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.AreaSerialier
        else:
            return serializers.SubAreaSerializer

