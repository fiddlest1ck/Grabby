import datetime
from models import Record
from settings import celery, db
from utils import get_response_status, parse_yml_files


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    for parsed_data in parse_yml_files()['urls']:
        sender.add_periodic_task(parsed_data['delay'],
                                 save_response_status.s(parsed_data['url']))


@celery.task
def save_response_status(url):
    record = Record(url=url, status_code=get_response_status(url),
                    response_date=datetime.datetime.now())
    db.session.add(record)
    db.session.commit()
