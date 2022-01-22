from articles.models import Post
import celery
import datetime


@celery.task.periodic_task(run_every=datetime.timedelta(days=1))
def set_default(self):
    votes_count = Post.objects.all().update(amounts_of_upvotes=0)
    return votes_count
