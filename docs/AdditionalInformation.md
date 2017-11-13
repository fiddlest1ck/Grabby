# Grabby Additioial info

This simple and lightweight application uses great components for scaling and optimizing data flow. This application based on Celery distribution tasks queue. This component provides easy but powerfull methods for parsing yaml configuration files and creating periodic tasks based on schedule from yaml files for each url. Every response that you got is saved in local sqlite database. System uses SQLAlchemy who provides ORM, serialization and database connection for REST API Flask routines.

#### Dockerizing

Docker containers are good for deploy, scale and fast run applications.
It's much better for wider applications than "Grabby". The main con of dockerizing this application is sqlite database engine who don't provide server whose can separate from application container, so each "docker run", application is create new clear database file. Especially for this state I created endpoint /api/v1/backup/ for get database before changing something with container.
