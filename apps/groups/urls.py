from django.urls import path, include
from apps.groups.views import CreateGroup, GroupIndex, GroupList

urlpatterns = [
    path("create_group/", CreateGroup.as_view(), name="create_group"),
    path("grupo/<int:pk>/", GroupIndex.as_view(), name="group_index"),
    path("group_list/", GroupList.as_view(), name="group_list"),
]
