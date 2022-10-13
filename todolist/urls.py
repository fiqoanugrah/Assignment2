from django.urls import path
from todolist.views import  add_task, delete_task, register,  show_todolist, show_todolist_json, update_task
from todolist.views import login_user
from todolist.views import logout_user  
from todolist.views import new_task



app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', new_task, name='new_task'),
     path('delete/<int:id>', delete_task, name="delete_task"),
    path('update/<int:id>', update_task, name="update_task"),
    path('json/', show_todolist_json, name="show_todolist_json"),
    path('add/', add_task, name="add_task"),
]