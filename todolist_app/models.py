from django.db import models
from django.contrib.auth.models import User                                           

# Create your models here.

class Tasklist(models.Model) :

    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task + " - " + str(self.done)
    
class Contect(models.Model) :

    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    enquiry = models.CharField(max_length=800)

    def __str__(self):
        return self.first_name + " " + str(self.last_name)
