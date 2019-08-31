# Mouseless

This is a web server that can host quizzes.

## Usage

### Install dependencies

```bash
pip install -r requirements.txt
```

### Make migrations

```bash
python manage.py makemigrations
```

### Perform migration

```bash
python manage.py migrate
```

### Create a super user

```bash
python manage.py createsuperuser
```

### Run server

```bash
python manage.py runserver 0.0.0.0:8000
```