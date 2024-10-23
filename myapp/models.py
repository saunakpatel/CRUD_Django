from django.db import models

# Create your models here.


class Contact(models.Model):
    name=models.CharField(max_length=40,blank=True,null=True)
    email=models.EmailField(max_length=40,unique=True,blank=True,null=True)
    address=models.TextField()
    phone=models.IntegerField( )
    
    def __str__(self):
        return self.name