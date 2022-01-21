from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    link = models.URLField(verbose_name="Link to post")
    creation_date = models.DateField(auto_now=True)
    amount_of_upvotes = models.IntegerField(verbose_name="upvotes count")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.link


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.post.link} - {self.author_name}"
