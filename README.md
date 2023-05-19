# DailyPlate
Meal plan generator with nutritional and budgeting information

# RUN WITH DOCKER

```
docker compose up
```

# Image on docker hub

https://hub.docker.com/repository/docker/alwaysfr3sh/django-docker/general

# SEED DATABASE
Model architecture has changed. If already seeded before may 13, flush and migrate before re-seeding:
```
./manage.py flush
```

```
./manage.py makemigrations
```

```
./manage.py migrate
```

```
./manage.py seed
```

# SET UP ADMIN
```
./manage.py createsuperuser
```

```
./manage.py seed

