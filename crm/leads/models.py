from django.db import models


class Lead(models.Model):

    SOURCE_CHOICES = (
        # The first element is how the choice gets stored in the db, the second element is the display value
        ('YouTube', 'YouTube'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter'),
    )

    # Setting the max_length on CharFields is required
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)

    # If the to argument is a string django knows that the Model being referenced is in the same file
    # otherwise the to arguments Model would need be above the current Model
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE, default=None)

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100, default=None)

    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)


class Agent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
