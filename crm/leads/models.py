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

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)
