from __future__ import absolute_import
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Develops_Test_Task.settings')


app = Celery('Develops_Test_Task', broker='redis://localhost')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks('settings.INSTALLED_APPS', related_name='tasks')


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


if __name__ == '__main__':
    app.start()