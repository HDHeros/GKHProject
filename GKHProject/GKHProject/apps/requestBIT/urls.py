from django.urls import path
from requestBIT.views import *

urlpatterns = [
     path('requests/', BIT_requests.as_view()),
]