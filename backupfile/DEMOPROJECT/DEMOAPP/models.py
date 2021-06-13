from django.db import models

# Create your models here.

class Messages(models.Model):
    id = models.AutoField(primary_key=True)

    phonenumber = models.CharField(max_length=100)

    body = models.CharField(max_length=200)

    sent_date = models.DateField()





