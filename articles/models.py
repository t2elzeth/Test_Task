from django.db import models


class Post(models.Model):
    class Meta:
        ordering = ["-creation_date"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    DEFAULT_AUTHOR_NAME = "anonymous"

    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255, default=DEFAULT_AUTHOR_NAME)
    link = models.SlugField(verbose_name="Link to post", max_length=200)
    creation_date = models.DateField(auto_now=True)
    amount_of_upvotes = models.IntegerField(default=0)

    def upvote(self):
        self.amount_of_upvotes += 1

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        ordering = ["-creation_date"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)
    author_name = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.post.link} - {self.author_name}"


class Upvote(models.Model):
    class Meta:
        ordering = ["-id"]

    post = models.ForeignKey(Post, related_name="upvotes", on_delete=models.CASCADE)

    def save(self, commit=True, *args, **kwargs):
        if commit:
            self.post.upvote()
            self.post.save()

        super(Upvote, self).save(*args, **kwargs)

    def __str__(self):
        return self.post.title
