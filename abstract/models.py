from django.db import models

# Create your models here.

class Base(models.Model):
    content = models.CharField(max_length=100)
    alias = models.CharField(max_length=100,db_index=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
      return self.alias

    class Meta:
        abstract = True

class Common(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True