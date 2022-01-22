from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    UpvoteAPIView,
    CommentListView,
    CommentDetailView,
)

urlpatterns = [
    path("posts/", PostListView.as_view(), name="list-of-posts"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("comments/", CommentListView.as_view(), name="list-of-comments"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
    path("likes/", UpvoteAPIView.as_view(), name="upvote-endpoint"),
]
