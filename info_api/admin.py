from __future__ import unicode_literals
from django.contrib import admin
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin,ImportExportModelAdmin,ExportMixin
from models import *
from django.core.paginator import Paginator

class ListResource(resources.ModelResource):
    item = fields.Field(column_name='item', attribute='item',
                   widget=ForeignKeyWidget(Item, 'alias'))
    env = fields.Field(column_name='env', attribute='env',
                   widget=ForeignKeyWidget(Env, 'alias'))
    location = fields.Field(column_name='location', attribute='location',
                   widget=ForeignKeyWidget(Location, 'alias'))
    class Meta:
        model = List
        skip_unchanged = True
        fields = ('id','item','host','env','location')

class ListAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ListResource
    list_display=('id','item','location','env','host','version','created_date',)
    search_fields=('host','item__content','location__content','env__content')
    list_filter = ('host','item',)
    list_per_page = 10
    ordering = ('id','item','env','created_date')

class EnvResource(resources.ModelResource):
    class Meta:
        model = Env
        skip_unchanged = True
        fields = ('id','content','alias',)

class EnvAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = EnvResource
    list_display=('id','content','alias','created_date')
    search_fields=('content',)
    list_filter = ('content',)
    list_per_page = 10
    date_hierarchy = 'created_date'
    ordering = ('content','created_date')
    fields = ('content','alias')

class ItemResource(resources.ModelResource):
    class Meta:
        model = Item
        skip_unchanged = True
        fields = ('id','content','alias','type',)

class ItemAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ItemResource
    list_display=('id','content','alias','type','created_date')
    search_fields=('content',)
    list_filter = ('content',)
    list_per_page = 10
    date_hierarchy = 'created_date'
    ordering = ('content','created_date')
    fields = ('content','alias','type')

class LocationResource(resources.ModelResource):
    class Meta:
        model = Location
        skip_unchanged = True
        fields = ('id','content','alias',)

class LocationAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = LocationResource
    list_display=('id','content','alias','created_date')
    search_fields=('content',)
    list_filter = ('content',)
    list_per_page = 10
    date_hierarchy = 'created_date'
    ordering = ('content','created_date')
    fields = ('content','alias')

class VersionResource(resources.ModelResource):
    item = fields.Field(column_name='item', attribute='item',
                   widget=ForeignKeyWidget(Item, 'alias'))
    env = fields.Field(column_name='env', attribute='env',
                   widget=ForeignKeyWidget(Env, 'alias'))
    class Meta:
        model = Version
        skip_unchanged = True
        fields = ('id','item','env','mission','version','svn_url')

class VersionAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = VersionResource
    list_display=('id','item','env','mission','version','svn_url','created_date')
    search_fields=('item__content','version','mission')
    list_filter = ('item',)
    list_per_page = 10
    date_hierarchy = 'created_date'
    ordering = ('item__content','created_date')
    fields = ('item','env','mission','version','svn_url')


admin.site.register(Env,EnvAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(List,ListAdmin)
admin.site.register(Version,VersionAdmin)
admin.site.register(Location,LocationAdmin)