from django.db import models

class Job(models.Model):
	image = models.ImageField(upload_to='images/') #whenever someone uploads an image it will be saved in 'images/'
	summary = models.CharField(max_length=200)
