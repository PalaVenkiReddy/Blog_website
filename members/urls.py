from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'Register'),
    # no need to create the url for login page because django authentication take care of it as we included its package
]
