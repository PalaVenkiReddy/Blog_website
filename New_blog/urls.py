from django.urls import path
#to import all files from present working app
#from . import views
# to import the Homeview class from views.py 
from .views import HomeView
from .views import ArticleView
from .views import Add_post_View
from .views import EditPostView
from .views import DeletePostView
from .views import Add_Category_View

urlpatterns = [
    #path('', views.home, name="home"),  # it will search for home in views.py
    path('', HomeView.as_view(), name = "home"),
    #to create the url for the articles
    path('Article/<int:pk>', ArticleView.as_view(), name = 'Article-details'), # pk->primary key of the blog created by database
    #to create the url for the Add_post
    path('Add_post', Add_post_View.as_view(), name = 'ADD_NEWPOST'),
    path('Add_Category', Add_Category_View.as_view(), name = 'ADD_NEWCategory'),
    path('article/edit/<int:pk>', EditPostView.as_view(), name = 'Edit_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name = 'Delete_post'),
]
