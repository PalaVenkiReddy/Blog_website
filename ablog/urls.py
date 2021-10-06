from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path to our newapp after reaching this path it will go for searching the New_blog.urls in our project
    path('',include('New_blog.urls')),
    # path for urls of django authentication system like login, logout urls
    path('members/', include('django.contrib.auth.urls')),
    # path to our newapp after reaching this path it will go for searching the members.urls in our project
    path('members/', include('members.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
