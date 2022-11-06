from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 64, blank = True, null = True)
    detail = models.CharField(max_length = 32, blank = True, null = True)
    