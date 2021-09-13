import os
from django.db import models
from django.utils import timezone
from uuid import uuid4
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

# Create your models here.

def path_and_rename_poster_image(instance,filename):
     upload_to = 'uploads/blog/'
     ext = filename.split('.')[-1]
     # get filename
     if instance.pk:
         filename = '{}-{}.{}'.format(instance.pk,'rojcode',ext)
     else:
         # set filename as random string
         filename = '{}.{}'.format(uuid4().hex,ext)
     # return the whole path to the file
     return os.path.join(upload_to,filename)


class Category(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self): 
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=250)
    poster = models.ImageField(upload_to=path_and_rename_poster_image)
    short_description = models.TextField()
    body = RichTextUploadingField()
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = TaggableManager()
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self): 
        return self.title
    
    



 