from django.urls import path

from todo.views import *

urlpatterns = [
    path('', TaskListCreateView.as_view()),
    path('<int:pk>', TaskDeteilUpdateDelete.as_view())


]