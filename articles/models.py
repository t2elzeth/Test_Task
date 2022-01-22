from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255, default="anonymous")
    link = models.SlugField(verbose_name="Link to post", max_length=200)
    creation_date = models.DateField(auto_now=True)
    amount_of_upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-creation_date"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)
    author_name = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-creation_date"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.post.link} - {self.author_name}"


class Upvote(models.Model):
    post = models.ForeignKey(Post, related_name="upvotes", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-id"]

    def save(self, commit=True, *args, **kwargs):
        if commit:
            try:
                self.post.amount_of_upvotes += 1
                self.post.save()
                super(Upvote, self).save(*args, **kwargs)
            except:
                pass
        else:
            pass

    def __str__(self):
        return self.post.title
