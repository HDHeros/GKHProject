from django.urls import path
from fixed_assets.views import *

urlpatterns = [
     path('fixed_assets/', PC_C.as_view()),
]