from django.urls import path
from .views import *

urlpatterns=[
    path('signup/',SignUpCreateView.as_view(),name='signup.html'),
]