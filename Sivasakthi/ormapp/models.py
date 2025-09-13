from django.db import models
from django.contrib import admin
class Car_DB(models.Model):
	Car_name=models.CharField(max_length=20)
	Fuel_efficient=models.FloatField()
	Color=models.CharField(max_length=10)
	Prize=models.IntegerField()
	CarID=models.IntegerField(primary_key=True)
class Car_DBAdmin(admin.ModelAdmin):
	list_display=["Car_name","Fuel_efficient","Color","Prize","CarID"]
