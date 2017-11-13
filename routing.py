from flask import jsonify, send_from_directory
from models import Record
from settings import app, db


@app.route('/api/v1/records/', methods=['GET'])
def get_records():
    return jsonify(records=[x.serialize for x in Record.query.all()])


@app.route('/api/v1/backup/')
def download_database():
    return send_from_directory(app.static_folder, 'grabby.db', as_attachment=True)


@app.route('/api/v1/records/<int:record_id>/', methods=['GET'])
def get_record(record_id):
    record = Record.query.get(record_id)
    if record:
        return jsonify(record.serialize)


@app.route('/api/v1/records/<int:record_id>/', methods=['DELETE'])
def delete_record(record_id):
    record = Record.query.get(record_id)
    db.session.delete(record)
    db.session.commit()
    return jsonify('Record {} id {} deleted'.format(record.url, record.id))
