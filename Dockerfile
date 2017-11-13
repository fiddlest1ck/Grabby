FROM kcrong/python3.6

ADD . /opt/grabby
WORKDIR /opt/grabby/
RUN pip3.6 install -r requirements.txt &&apt-get install -y redis-server rabbitmq-server
EXPOSE 5000
RUN touch docker_entrypoint.sh && echo $'#!/bin/bash\n service rabbitmq-server start \n export LC_ALL=C.UTF-8 \n export LANG=C.UTF-8 \n export GRABBY_HOST="0.0.0.0" \n python3.6 server.py' > docker_entrypoint.sh && chmod 777 docker_entrypoint.sh
ENTRYPOINT ./docker_entrypoint.sh
