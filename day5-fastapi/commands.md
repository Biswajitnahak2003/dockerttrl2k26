# Day 5 Commands

## Build the Docker image

```bash
docker build -t fastapi-trial .
```

## Run the container

```bash
docker run -p 8000:8000 fastapi-trial
```

## Test the app

Open your browser or curl:

```bash
curl http://localhost:8000/
```

```bash
curl http://localhost:8000/health
```

```bash
curl https://localhost:8000/docs
```
