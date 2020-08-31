from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=250) 
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/') #whenever someone uploads an image it will be saved in 'images/'

