from articles.models import Post
import schedule
import time


def set_default():
    votes_count = Post.objects.all().update(amounts_of_upvotes=0)
    return votes_count


# schedule.every(23).hours.do(set_default)
schedule.every().minute.do(set_default)
while True:
    schedule.run_pending()
    time.sleep(36000)