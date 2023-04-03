# Registration telegram bot

## About The Project
Simple project that helps to handle with registration procedure on your website.
If a user wants to register, it will be redirected to Telegram for the registration procedure.
After registration will be completed, the user will be allowed to log in on its account profile page with the user's data from Telegram.

The project uses Django as a backend and Aiogram based bot as a service.
Also, Docker and Nginx support added..


## Prerequisites

Docker, Docker Compose must be installed.
If not, please see:

[Docker](https://docs.docker.com/engine/install/) and
[Docker compose](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-22-04)
for installation instructions.


## Installation

1. Clone the repo:
```sh
git clone https://github.com/OleksandrZhydyk/RegistrationBot.git
```

## Usage
1. Add .env files for configuration:
* Django .env
```sh
LOCAL_PORT=YOUR_LOCAL_PORT
WSGI_PORT=YOUR_WSGI_PORT
BOT_URL=YOUR_TELEGRAM_BOT_URL
HOST=YOUR_HOSTED_DOMAIN
DJANGO_KEY=YOUR_DJANGO_SECRET_KEY
DEBUG=False
```

* Bot .env
```sh
BOT_ACCESS_TOKEN=YOUR_BOT_ACCESS_TOKEN
BACKEND_HOST=http://backend:YOUR_WSGI_PORT
HOST=YOUR_HOSTED_DOMAIN
```
2. Run the command for building and running the images:
```sh
docker compose up -d --build