from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from .models import Post, Comment

# If you want to re-enable, remove these unregister calls and registers below
try:
    admin.site.unregister(Post)
except NotRegistered:
    pass

try:
    admin.site.unregister(Comment)
except NotRegistered:
    pass

# (Optional) keep registrations commented out to hide from admin UI
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ("id", "user", "text", "created_at")
#     search_fields = ("user__email", "text")
#     list_filter = ("created_at",)
#
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ("id", "post", "user", "comment", "created_at")
#     search_fields = ("user__email", "comment")
#     list_filter = ("created_at",)
