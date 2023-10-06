from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'todo-view-set',TodoViewSet,basename='user')
from rest_framework.authtoken import views

urlpatterns = [
  path('',home, name="home"),
  path('get_todo',get_todo,name="get_todo"),
  path('post_todo',create_todo,name="create_todo"),
  path('update_todo',update_todo,name="update_todo"),
  path('delete',delete_all_timing_todos,name="delete_all_timing_todos"),

  path('todo/',TodoView.as_view()),
]

urlpatterns +=router.urls