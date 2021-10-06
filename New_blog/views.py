from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# ListView-Lists all the records on the web page from the database
# DeatailView - Lists all the detailed records of one model on the web page from the database
# create View - just to create the forms on our web page to add a new post 

# to import the Post models 
from .models import Post, Category

from .forms import PostForm, EditForm
from django.urls import reverse_lazy


#def home(request):
#	return render(request, 'home.html', {})

class HomeView(ListView):
	# to have what model is using
	model = Post
	# to call the template file into here
	template_name =  'home.html'
	# to have recent posts first 
	ordering = ['-id']


class ArticleView(DetailView):
	# to have what model is using
	model = Post
	# to call the template file into here
	template_name = 'articles.html'


class Add_post_View(CreateView):
	# to have what model is using 
	model = Post
	form_class = PostForm
	# to call the template file into here
	template_name = 'Add_post.html'
	# to have selected fields from chosen model
	#fields = '__all__' # to select all the fields
	# to have some selected fields create a list of fields of that model

class Add_Category_View(CreateView):
	# to have what model is using 
	model = Category
	# to call the template file into here
	template_name = 'Add_category.html'
	# to have selected fields from chosen model
	fields = '__all__' # to select all the fields
	# to have some selected fields create a list of fields of that model


class EditPostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'Edit_post.html'


class DeletePostView(DeleteView):
	model = Post
	template_name = 'Delete_post.html'
	# to have success url after deleting post
	success_url = reverse_lazy('home')


