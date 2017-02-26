from django.db import models

class SiteUser(models.Model):
    user_name = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    num_points = models.IntegerField(default = 0)
    @classmethod
    def getPoints(self):
    	return self.num_points
    @classmethod
    def addPoints(self):
    	temp = int(self.num_points) + 5
    	self.num_points = temp

class Station(models.Model):
	location = models.CharField(max_length=40)