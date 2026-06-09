# Day 3 Commands

Create a named volume:

```bash
docker volume create mydata
```

List volumes:

```bash
docker volume ls
```

Run a container with the volume mounted at `/data`:

```bash
docker run -it \
  -v mydata:/data \
  ubuntu:22.04 bash
```

Inside the container:

```bash
echo "hello docker" > /data/test.txt
exit
```

Run another container with the same volume:

```bash
docker run -it \
  -v mydata:/data \
  ubuntu:22.04 bash
```

Inside the second container:

```bash
cat /data/test.txt
```

Run a container with a bind mount from the current project folder:

```bash
docker run -it \
  -v $(pwd):/app \
  -w /app \
  python:3.12-slim bash
```

This maps your host project folder into the container so code changes appear immediately.

Run the Day 3 app with environment variables:

```bash
docker run --rm \
  -v $(pwd):/app \
  -w /app \
  -e MODEL_NAME=llama3 \
  -e API_KEY=test123 \
  -e DATA_DIR=/data \
  python:3.12-slim \
  python app.py
```

If you want to mount a local `data` folder instead of a Docker volume:

```bash
docker run --rm \
  -v $(pwd)/data:/data \
  -v $(pwd):/app \
  -w /app \
  -e MODEL_NAME=llama3 \
  -e API_KEY=test123 \
  -e DATA_DIR=/data \
  python:3.12-slim \
  python app.py
```
