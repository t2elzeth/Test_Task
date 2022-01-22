from django.shortcuts import render
from .models import Post, Comment, Upvote
from .serializers import PostSerializer, CommentSerializer, UpvoteSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)


class CommentListView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostListView(ListCreateAPIView):
    queryset = Post.objects.all().order_by("-creation_date")
    serializer_class = PostSerializer


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UpvoteAPIView(CreateAPIView):
    queryset = Upvote.objects.all()
    serializer_class = UpvoteSerializer

