# from django.db import models
# # from vote.models import VoteModel
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from vote.models import VoteModel

#Create your models here.
class Image(VoteModel,models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=50)
    image_caption = models.CharField(max_length=50)
    likes = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images')
    bio = HTMLField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    