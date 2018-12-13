from django.db import models
from django.contrib.auth.models import User,UserManager
MEDIA_CHOICES = (
        ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
         ),
        ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
         ),
        ('unknown', 'Unknown'),
    )

class EmployeeUser(User):
    objects = UserManager()
    #my_name=User.CharField(max_length=15)
    class Meta:
         proxy=True
         #ordering=('name',)
# Create your models here.

class Complain(models.Model):
    name=models.CharField(max_length=15)
    employee_id=models.CharField(max_length=15)
    complain_request=models.TextField(max_length=100)

class AddAccessorie(models.Model):
    name=models.CharField(max_length=15)
    quantity=models.IntegerField(default=0)
    def __str__(self):
        return u'%s' %(self.name)#,self.quantity)
class AccessoryRequest(models.Model):
    name=models.ForeignKey(AddAccessorie,on_delete=models.CASCADE)
    employee_name=models.CharField(max_length=15)
    employee_id=models.CharField(max_length=15)
    quantity=models.IntegerField(default=0)
    def __str__(self):
         return u'%s %s %s' %(self.name,self.employee_name,self.quantity)#,self.quantity)
    # def __init__(self):
    #     print("Accessory requested")

class TestModel(models.Model):
    name=models.CharField(max_length=15,choices=MEDIA_CHOICES)
class MyModel(models.Model):
    name=models.CharField(max_length=15)



# class UserInfoChangeRequests(models.Model):
#     employee_name=models.CharField(max_length=15)
#     employee_id=models.CharField(max_length=12)
#     information_field=models.CharField(help_text='Select your information that has been updated',max_length=20,choices=list(User.objects.))