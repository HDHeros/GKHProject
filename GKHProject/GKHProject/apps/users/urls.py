from django.urls import path
from users.views import *

urlpatterns = [
     path('user/', Users.as_view()),
]