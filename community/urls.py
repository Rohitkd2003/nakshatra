from django.urls import path
from .views import PostCreateView, CommentCreateView

urlpatterns = [
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:post_id>/comment/", CommentCreateView.as_view(), name="comment-create"),
]
