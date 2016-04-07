# coding= utf-8
from django.db import models
from abstract.models import Base,Common

class Item(Base):
    type=models.CharField(max_length=100)


class Location(Base):
    pass
class Env(Base):
    pass


class List(Common):
    item=models.ForeignKey(Item,related_name='list_name')
    host=models.GenericIPAddressField()
    version=models.CharField(max_length=100,default='no_version')
    location=models.ForeignKey(Location)
    env=models.ForeignKey(Env)
    class Meta:
        ordering=['item']

class Version(Common):
    item=models.ForeignKey(Item,related_name='version_name')
    mission=models.CharField(max_length=100)
    version=models.CharField(max_length=100)
    svn_url=models.URLField()
    env=models.ForeignKey(Env)
    class Meta:
        ordering=['-created_date']