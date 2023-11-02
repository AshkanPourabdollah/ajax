from django.db import models

# Create your models here.
class SignIn(models.Model):
    name=models.CharField(max_length=20,default="")
    lastName=models.CharField(max_length=25,default="")

    def __str__(self):
        return self.name +" "+ self.lastName