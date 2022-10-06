from django.urls import path
from todolist.views import change_status, delete_task, register, show_todolist
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
    path('change/<int:id>', change_status, name='change_status'),
    path('delete/<int:id>', delete_task, name='delete_task'),
]