# It is created by me and using preivious urls

from django.urls import path
from . import views

# localhost:8000/project
# localhost:8000/project/update
urlpatterns = [
    path('', views.all_project, name='All_project'),
    # path('update/', views.update, name='Update'),
      
]