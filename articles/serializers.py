from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Post, Comment, Upvote


# Author name also can be in readonly but when auth is implemented
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "author_name", "content", "creation_date")
        read_only_fields = ("creation_date",)


# Author name also can be in readonly but when auth is implemented
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(source="comment", many=True)

    class Meta:
        model = Post
        fields = (
            "title",
            "author_name",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "comments",
        )
        read_only_fields = ("link", "creation_date", "amount_of_upvotes", "comments")


class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = "__all__"
