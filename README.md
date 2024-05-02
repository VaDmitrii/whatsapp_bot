# WhatsApp bot with FastAPI and Twilio

<a href="https://github.com/tiangolo/full-stack-fastapi-template/actions?query=workflow%3ATest" target="_blank"><img src="https://github.com/tiangolo/full-stack-fastapi-template/workflows/Test/badge.svg" alt="Test"></a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/tiangolo/full-stack-fastapi-template" target="_blank"><img src="https://coverage-badge.samuelcolvin.workers.dev/tiangolo/full-stack-fastapi-template.svg" alt="Coverage"></a>

## Technology Stack and Features

- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) for the Python backend API.
    - 🧰 [SQLModel](https://sqlmodel.tiangolo.com) for the Python SQL database interactions (ORM);
    - 💾 [PostgreSQL](https://www.postgresql.org) as the SQL database.
- 🐋 [Docker Compose](https://www.docker.com) for development and production.


## How To Use It

You can **just fork or clone** this repository and use it as is.

- Clone a repository to you local machine

```
git clone https://github.com/VaDmitrii/whatsapp_bot.git
```
- Register a free account on [Twilio](https://www.twilio.com/);
- Save you `AUTH_TOKEN` and `ACCOUNT_SID` and save it to `.env` file;

- Set the new origin to your new repository, copy it from the GitHub interface, for example:

```bash
git remote set-url origin git@github.com:octocat/my-full-stack.git
```

- Add this repo as another "remote" to allow you to get updates later:

```bash
git remote add upstream git@github.com:tiangolo/full-stack-fastapi-template.git
```

- Push the code to your new repository:

```bash
git push -u origin master
```

- Install requirements
```
pip install -r requirements.txt
```
  
- Run `docker-compose.yml` file.
  
```
docker compose up -d
```

- Redirect POST requests from Twilio to your `localhost:8000`:

```bash
ngrok http http://localhost:8000
```

- Add the redirect ip to your Twilio console for POST method -> Messaging -> Send a Whatsapp message -> Sandbox settings. For a expample:

```
https://your-redirect-ip.ngrok-free.app/whatsapp
```
- Now you can send audio messages and photos to Twilio number
### Configure

Before running docker-compose localy, make sure you change at least the values for:

- `TWILIO_AUTH_TOKEN`
- `TWILIO_ACCOUNT_SID`
- `POSTGRES_PASSWORD`
