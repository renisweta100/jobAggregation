from django.db import models
from users.models import User


# Create your models here.
class Jobs(models.Model):
    title = models.CharField(max_length=200)
    skill = models.CharField(max_length=200)



class SavedJob(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)




def __str__(self):
    return self.title
