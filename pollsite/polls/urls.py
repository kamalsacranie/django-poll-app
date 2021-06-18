from django.urls import path
# Importing our views we have created from the same directory
from . import views

urlpatterns = [
    # we observe the path funciton taking nothing as the path, i.e. home
    # and then our uncalled function as the second arg
    # and then we give a name for reversing the URL
    path('', views.index, name='index')
]