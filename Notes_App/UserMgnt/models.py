from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class notes(models.Model):
    
    n_id = models.AutoField(primary_key=True)
    n_name = models.CharField(max_length=20)
    n_owner = models.CharField(max_length=20)
    owner_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    n_content = models.CharField(max_length=100)
    mark_complete = models.IntegerField(blank=True)