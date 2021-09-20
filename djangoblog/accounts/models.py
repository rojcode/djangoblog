import os
from django.db import models
from uuid import uuid4


# Create your models here.

def path_and_rename_avatar_image(instance,filename):
     upload_to = 'uploads/avatar'
     ext = filename.split('.')[-1]
     # get filename
     if instance.pk:
         filename = '{}-{}.{}'.format(instance.pk,'rojcode',ext)
     else:
         # set filename as random string
         filename = '{}.{}'.format(uuid4().hex,ext)
     # return the whole path to the file
     return os.path.join(upload_to,filename)

class Avatar(models.Model):
    user = models.OneToOneField('auth.User',related_name='avatar_profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=path_and_rename_avatar_image)
    bio = models.TextField()

    def __str__(self): 
        return f'{self.user.username} Avatar'