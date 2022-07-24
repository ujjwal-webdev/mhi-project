from django.db import models

class product(models.Model):
    id = models.IntegerField(primary_key = True)
    pid = models.IntegerField()
    name = models.TextField()
    description = models.TextField()
    source_url = models.TextField()

class application(models.Model):
    id = models.IntegerField(primary_key = True)
    aid = models.IntegerField()
    name = models.TextField()
    description = models.TextField()
    source_url = models.TextField()

class connecting(models.Model):
    product_id = models.IntegerField(null = True)
    application_id = models.IntegerField(null = True)