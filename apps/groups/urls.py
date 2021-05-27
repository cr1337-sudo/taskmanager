from django.urls import path, include
from apps.groups.views import CreateGroup, GroupIndex, GroupList, GroupTaskEdit, GroupTaskDelete

urlpatterns = [
    path("create_group/", CreateGroup.as_view(), name="create_group"),
    path("list/", GroupList.as_view(), name="group_list"),
    path("<str:pk>/", GroupIndex.as_view(), name="group_index"),
    path("task_edit/<str:pk>/", GroupTaskEdit.as_view(), name="group_task_edit"),
    path("task_delete/<str:pk>/", GroupTaskDelete.as_view(), name="group_task_delete"),
]
