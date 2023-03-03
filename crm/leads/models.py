from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class Lead(models.Model):
    SOURCE_CHOICES = (
        # The first element is how the choice gets stored in the db, the second element is the display value
        ("YouTube", "YouTube"),
        ("Google", "Google"),
        ("Newsletter", "Newsletter"),
    )

    # Setting the max_length on CharFields is required
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)

    # If the to argument is a string django knows that the Model being referenced is in the same file
    # otherwise the to arguments Model would need be above the current Model
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE, default=None)

    phoned = models.BooleanField(default=False)
    source = models.CharField(
        choices=SOURCE_CHOICES, max_length=100, default=None, null=True
    )

    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.first_name + self.last_name


class Agent(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    organisation = models.ForeignKey("UserProfile", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()


class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, User)
