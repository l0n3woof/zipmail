from django.urls import path
from .views import *

urlpatterns = [
    path('sendemail/', SendZipEmail.as_view(), name='sendemail'),
]
