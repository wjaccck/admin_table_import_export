from rest_framework import serializers
from info_api.models import Item, List, Location, Env, Version

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location

class EnvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Env

class ListSerializer(serializers.ModelSerializer):
    item=serializers.SlugRelatedField(queryset=Item.objects.all(),slug_field='alias')
    location=serializers.SlugRelatedField(queryset=Location.objects.all(),slug_field='alias')
    env=serializers.SlugRelatedField(queryset=Env.objects.all(),slug_field='alias')
    class Meta:
        model = List

class VersionSerializer(serializers.ModelSerializer):
    item=serializers.SlugRelatedField(queryset=Item.objects.all(),slug_field='alias')
    env=serializers.SlugRelatedField(queryset=Env.objects.all(),slug_field='alias')
    class Meta:
        model = Version