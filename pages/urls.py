
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *
urlpatterns = [
 path('', index_view, name='index'),
]