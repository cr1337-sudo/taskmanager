from django import template
from ..models import Group

register = template.Library()


@register.filter(name="is_staff")
def has_group(user, group_id):
    group = Group.objects.get(id = group_id)
    if user in group.group_moderators.all() or user == group.admin.username:
        return True
