from django.db import models
from django.contrib.auth.models import User
from UserMgnt.models import notes

# Create your models here.
class shared_notes(models.Model):
    
    sid = models.AutoField(primary_key=True)
    n_id = models.ForeignKey(notes,on_delete=models.CASCADE,null=True)
    n_shrd_name = models.CharField(max_length=20)
    n_shrd_owner =  models.CharField(max_length=20)
    n_shrd_with = models.CharField(max_length=20)
    owner_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mark_complete = models.IntegerField(blank=True,null=True)