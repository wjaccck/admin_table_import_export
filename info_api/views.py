from django.shortcuts import render
from rest_framework import permissions
# Create your views here.
import django_filters
from rest_framework import viewsets
from rest_framework import filters as source_filter
import rest_framework_filters as filters
from rest_framework_filters.backends import DjangoFilterBackend


from serializers import ItemSerializer,ListSerializer,LocationSerializer,EnvSerializer,VersionSerializer
from models import Item,Location,List,Env,Version

# class BaseViewSet(viewsets.ModelViewSet):

class ItemFilter(filters.FilterSet):
    name = filters.CharFilter(name="alias")
    class Meta:
        model = Item
        fields = ['name']

class EnvFilter(filters.FilterSet):
    name = filters.CharFilter(name="alias")
    class Meta:
        model = Env
        fields = ['name']

class ListFilter(filters.FilterSet):
    item=filters.RelatedFilter(ItemFilter,name='item')
    host=filters.CharFilter(name='host')
    env=filters.RelatedFilter(EnvFilter,name='env')
    class Meta:
        model = List
        fields = ['item','host','env']

class VersionFilter(filters.FilterSet):
    item=filters.RelatedFilter(ItemFilter,name='item')
    version=filters.CharFilter(name='version')
    mission=filters.CharFilter(name='mission')
    env=filters.RelatedFilter(EnvFilter,name='env')
    class Meta:
        model = Version
        fields = ['item','version','mission','env']


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (DjangoFilterBackend,source_filter.SearchFilter)
    # filter_fields = ('content',)
    search_fields = ('^content',)
    filter_class=ItemFilter

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('content',)

class EnvViewSet(viewsets.ModelViewSet):
    queryset = Env.objects.all()
    serializer_class = EnvSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('content',)

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ListFilter
    # filter_fields = ('item','location',)
    permission_classes = (permissions.DjangoModelPermissions,)


class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
    filter_backends = (DjangoFilterBackend,source_filter.SearchFilter)
    # filter_fields = ('item','version',)
    filter_class=VersionFilter
    search_fields = ('^version',)
    permission_classes = (permissions.DjangoModelPermissions,)