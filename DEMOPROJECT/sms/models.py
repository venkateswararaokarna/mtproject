from django.db import models

# Create your models here.

class ReceivedMessages(models.Model):

    id = models.AutoField(primary_key=True)

    phonenumber = models.CharField(max_length = 50)

    body = models.CharField(max_length=200)

    received_date = models.DateField()
