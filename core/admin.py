from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from community.models import Post, Comment
import types


def safe_unregister(model):
    try:
        admin.site.unregister(model)
    except NotRegistered:
        pass


# Unregister unwanted models
for mdl in (Token, Group, Post, Comment):
    safe_unregister(mdl)


# Additionally hide them from app list/navigation
HIDDEN_MODELS = {
    "authtoken.token",
    "auth.group",
    "community.post",
    "community.comment",
}

_orig_get_app_list = admin.site.get_app_list


def _filtered_app_list(self, request):
    app_list = _orig_get_app_list(request)
    filtered_apps = []
    for app in app_list:
        models = []
        for m in app["models"]:
            key = f"{m.get('app_label')}.{m.get('object_name').lower()}"
            if key not in HIDDEN_MODELS:
                models.append(m)
        if models:
            app["models"] = models
            filtered_apps.append(app)
    return filtered_apps


admin.site.get_app_list = types.MethodType(_filtered_app_list, admin.site)
