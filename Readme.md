# Grabby

It's simple responses status code checker. You can configure where and when system ping and check
saved responses from json API. Simple and light weight

### Quick Start:
#### Building from source:
System Requirements:
- python3.6 with virtualenv and pip3.6
- redis-server
- rabbitmq-server

#### Install:

```sh
$ virtualenv --python=python3.6 grabbyenv
$ source grabyenv/bin/activate
$ cd grabby
$ pip3 install -r requirements.txt
```
#### Run system by separately tasks:
in project folder:

```sh
$ export FLASK_APP=server.py
$ celery -A grabby worker -l info
$ celery beat -A grabby -l info
$ flask run
```
you can define a host and port by params:

```sh
$ flask run --host <host> --port <port>
```

#### Run system by one command:
in project folder:

```sh
$ python3.6 server.py
```
you can define a host and port in settings.py file

#### Runs as docker container:

```sh
$ docker build -t grabby .
$ docker run -d -p 5000:5000 grabby
```

System runs defaults at 127.0.0.1:5000





