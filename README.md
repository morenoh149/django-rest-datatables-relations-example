A minimal example of django-rest-datatables

----

## 📖 Installation
DjangoX can be installed via Pip, Pipenv, or Docker depending upon your setup. To start, clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/wsvincent/djangox.git
$ cd djangox
```

### Pip

```
$ python3 -m venv djangox
$ source djangox/bin/activate
(djangox) $ pip install -r requirements.txt
(djangox) $ python manage.py migrate
(djangox) $ python manage.py createsuperuser
(djangox) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

### Pipenv

```
$ pipenv install
$ pipenv shell
(djangox) $ python manage.py migrate
(djangox) $ python manage.py createsuperuser
(djangox) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

### Docker

```
$ docker build .
$ docker-compose up -d
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py createsuperuser
# Load the site at http://127.0.0.1:8000
```

For Docker, the `INTERNAL_IPS` configuration in `config/settings.py` must be updated to the following:

```python
# config/settings.py
# django-debug-toolbar
import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
```

## Setup

```
# Run Migrations
(djangox) $ python manage.py migrate

# Create a Superuser
(djangox) $ python manage.py createsuperuser

# Confirm everything is working:
(djangox) $ python manage.py runserver

# Load the site at http://127.0.0.1:8000
```

----

## License

[The MIT License](LICENSE)


<!-- ## Docker Usage
```
# Build the Docker Image
$ docker-compose build

# Run Migrations
$ docker-compose run --rm web python manage.py migrate

# Create a Superuser
$ docker-compose run --rm web python manage.py createsuperuser

# Run Django on http://localhost:8000/
$ docker-compose up

# Run Django in background mode
$ docker-compose up -d

# Stop all running containers
$ docker-compose down

# Run Tests
$ docker-compose run --rm web pytest

# Re-build PIP requirements
$ docker-compose run --rm web pip-compile requirements/requirements.in
```-->
