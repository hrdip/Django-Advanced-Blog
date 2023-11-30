from django.db import models  
from django.db.models.signals import post_save
from django.dispatch import receiver
from .users import User
# Create your models here.




class Profile (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(blank=True,null=True)
    description = models.TextField()
    bio = models.TextField()
    facebook_profile = models.URLField(blank=True,null=True)
    instagram_profile = models.URLField(blank=True,null=True)
    linkedin_profile = models.URLField(blank=True,null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.email


@receiver(post_save,sender=User)
def save_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        