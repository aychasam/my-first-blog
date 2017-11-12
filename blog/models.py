from django.db import models #Import all packages you need
from django.utils import timezone

class Post(models.Model): #permet de définir notre modèle. C'est un object
	author = models.ForeignKey('auth.User') #the author as the user
	title = models.CharField(max_length=200) #the title is a character
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self): #function which says that the things you publish will be published now and saved
		self.published_date = timezone.now()
		self.save()

	def __str__(self): #return it at the top
		return self.title
# Create your models here.
