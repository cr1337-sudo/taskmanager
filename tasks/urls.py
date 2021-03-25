from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("login/", views.CustomLogin.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.RegisterPage.as_view(), name="register"),
    path("", views.TaskList.as_view(), name="home"),
    path("create_task/", views.TaskCreate.as_view(), name="create_task"),
    path("task_update/<int:pk>/", views.TaskUpdate.as_view(), name="update_task"),
    path("task_delete/<int:pk>", views.TaskDelete.as_view(), name="delete_task"),
    path("all/", views.Users.as_view(), name="all"),
    path("all/user_tasks/<int:id>/", views.UserTasks.as_view(), name = "user_tasks"),

]
