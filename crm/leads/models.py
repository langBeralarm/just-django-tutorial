from django.db import models


class Lead(models.Model):
    # Setting the max_length on CharFields is required
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
