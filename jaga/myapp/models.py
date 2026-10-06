from django.db import models
from django.contrib import admin
class Service_center_DB(models.Model):
    Name=models.CharField(max_length=20)
    Date_of_service=models.DateField
    Mobile=models.IntegerField()
    Model=models.CharField(max_length=30)
    Address=models.TextField()
    Vehicle_no=models.TextField()
    Problem=models.CharField()
class Service_center_DBAdmin(admin.ModelAdmin):
    list_display=["Name","Mobile","Model","Address","Vehicle_no","Problem"]
 