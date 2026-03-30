from django.db import models

class Cattle(models.Model):
    cow_id = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cattle_images/')
    image_hash = models.CharField(max_length=100)