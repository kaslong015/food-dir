from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    is_user = models.BooleanField('is_user', default=False)
    is_restaurant = models.BooleanField('is_restaurant', default=False)
    is_admin = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True,)
    phone = models.CharField(max_length=100, null=True)

    profile_pic = models.ImageField(default='default.png')
    address = models.CharField(max_length=200, null=True)
    business_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        # print('created')


# post_save.connect(create_profile, sender=User)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('updated')
