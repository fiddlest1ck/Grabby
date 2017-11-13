import os
import threading
from settings import host, port
from routing import *


def start_celery():
    os.system('celery -A grabby worker -l info')


def start_celery_beat():
    os.system('celery beat -A grabby -l info')


def start_application():
    app.run(host=host,
            port=port)


if __name__ == "__main__":
    celery = threading.Thread(target=start_celery)
    celery_beat = threading.Thread(target=start_celery_beat)
    grabby = threading.Thread(target=start_application)
    grabby.start()
    celery.start()
    celery_beat.start()
