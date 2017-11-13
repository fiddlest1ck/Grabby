from settings import db


class Record(db.Model):
    __tablename__ = 'records'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    status_code = db.Column(db.Integer)
    response_date = db.Column(db.DateTime)

    def __repr__(self):
        return '{} {} {}'.format(self.url, self.status_code, self.response_date)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'url': self.url,
            'status_code': self.status_code,
            'response_date': self.response_date
        }


db.create_all()
