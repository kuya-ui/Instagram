# from django.db import models
# # from vote.models import VoteModel
from django.db import models
from django.contrib.auth.models import User
# from tinymce.models import HTMLField
# from vote.models import VoteModel

#Create your models here.

class Comments(models.Model):
    comment = models.CharField(max_length=100,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)