from django.db import models
from django.contrib.auth.models import User
# if you need to use something similar to the url template tag in your code, then we can use reverse function by having used URL:
from django.urls import reverse
from datetime import datetime, date

# to create the category class 
class Category(models.Model):
	name = models.CharField(max_length = 250)


	def __str__(self):
		return str(self.name)


	def get_absolute_url(self):
	    return reverse('home')

# to create a models 
class Post(models.Model):
	# creating the title field
	place = models.CharField(max_length = 250)
	# creating the author field
	author = models.ForeignKey(User, on_delete = models.CASCADE) # to delete all the blogs of user when he removed as user
	# to have a image in our blog post and when we are creating the image field we have mention where these files should be present (i.e in which directory)
	post_image = models.ImageField(null = True, blank = True, upload_to="images/")
	# creating a Description field
	Description = models.TextField()
	# creating a category field
	category = models.CharField(max_length=250, default='coding')
	# to have the date automaticaaly when we created a new post
	post_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return str(self.place) + ' | ' + str(self.author)


	def get_absolute_url(self):
	    return reverse('home')

	    			