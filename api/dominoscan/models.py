from django.db import models

# Create your models here.
class Domino(models.Model):
    domino_pic = models.FileField(upload_to="dominoscan/images")
    top_half = models.IntegerField(null=True)
    bottom_half = models.IntegerField(null=True)


