from django.urls import path
from . import views

urlpatterns = [
    path("", views.TaskList.as_view(), name="home"),
    path("create_task/", views.TaskCreate.as_view(), name="create_task"),
    path("task_update/<int:pk>/", views.TaskUpdate.as_view(), name="update_task"),
    path("task_delete/<int:pk>", views.TaskDelete.as_view(), name="delete_task"),
    path("all/", views.Users.as_view(), name="all"),
    path("all/user_tasks/<str:username>/", views.UserTasks.as_view(), name = "user_tasks"),

]
