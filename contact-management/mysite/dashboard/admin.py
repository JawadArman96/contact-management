from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import EmployeeUser,Complain,AddAccessorie,AccessoryRequest,TestModel
from django.utils.safestring import mark_safe
from django.contrib.admin import AdminSite
from .models import MyModel,AccessoryRequest

# class MyAdminSite(AdminSite):
#     site_header = 'Monty Python administration'

import smtplib
@receiver(post_save, sender=AccessoryRequest)
def accessory_request(sender, **kwargs):
    """A signal generated after each accessory is created"""
    user, created = kwargs["instance"], kwargs["created"]
    if created:
        print(str(user.name) + " Accessory is requested")
        password="DiscretePencil13"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Next, log in to the server
        server.login("ahmedadnan1396", "DiscretePencil13")

        # Send the mail
        msg = "Hello I am from NSL admin!"  # The /n separates the message from the headers
        msg="Employee name: "+str(user.employee_name)+",Employee Id :"+str(user.employee_id)+" requested,  Accessory name: "+str(user.name)
        msg=msg+", Quantity: "+str(user.quantity)
        print(msg)
        msg = "NSL admin!"+" Accessory name, "+str(user.name)+", Accessory quantity "+str(user.quantity)+", Employee Id,"+str(user.employee_id)
        # The /n separates the message from the headers
        # msg=msg+" Accessory name :"+str(user.name)+" "
        # msg=msg+" Accessory quantity :"+str(user.quantity)+" "
        # # msg=msg+" Requested employee name: "+str(user.employee_name)+" "
        # # msg=msg+" Requested employee ID: "+str(user.employee_id)

        server.sendmail("ahmedadnan1396@gmail.com", "jawadarman738@gmail.com", msg)
        server.quit()


        # fromaddr = "ahmedadnan1396@gmail.com"
        # toaddr = "jawadarman738@gmail.com"
        # msg = MIMEMultipart()
        # msg['From'] = fromaddr
        # msg['To'] = toaddr
        # msg['Subject'] = "Accessory Request"
        #
        # body = msg#"YOUR MESSAGE HERE"
        # msg.attach(MIMEText(body, 'plain'))
        #
        # server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.starttls()
        # server.login(fromaddr, password)
        # text = msg.as_string()
        # server.sendmail(fromaddr, toaddr, text)
        # server.quit()



class EmployeeUserAdmin(admin.ModelAdmin):
    def profile_picture(self, obj):
        if obj.profile_image:

            return mark_safe('<img src="{url}" width=70 height=70 />'.format(
                    url=obj.profile_image.url,
                    width=obj.profile_image.width,
                    height=obj.profile_image.height,
                )
            )
        else:
            return "Not uploaded"

    # readonly_fields = ["profile_picture", ]
    # list_display = ('profile_picture', 'name', 'mobileNumber', 'email', 'designation', 'department', 'bloddGroup')
    # fields = ('name','email','profile_picture','employeeId',
    #           'designation','department','lead',
    #           'reportingSupervisor','presentAddress','bloddGroup',
    #         'joiningDate')


class AddAccessorieAdmin(admin.ModelAdmin):
    list_display = ('name','quantity')

class AddAccessoryRequestAdmin(admin.ModelAdmin):
    list_display = ('name','employee_name','quantity')
    fields = ('name','employee_name','employee_id','quantity')

#admin.site.register(EmployeeUser,EmployeeUserAdmin)
#admin.site.register(Complain)
admin.site.register(AddAccessorie,AddAccessorieAdmin)
admin.site.register(AccessoryRequest,AddAccessoryRequestAdmin)
#admin.site.register(MyModel)
#admin.site.register(TestModel)
# Register your models here.
