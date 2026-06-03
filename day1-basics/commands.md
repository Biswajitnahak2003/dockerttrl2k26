# Docker Basic Commands 

## Commands

1. Pull the Python 3.12 image from Docker Hub

```bash
docker pull python:3.12
```

2. Run the Python 3.12 image and print the Python version

```bash
docker run python:3.12 python --version
```

3. List local Docker images

```bash
docker images
```

4. Check running containers

```bash
docker ps
```

5. Check all containers, including stopped ones

```bash
docker ps -a
```

6. Stop a running container

```bash
docker stop <container-id>
```

7. Remove a stopped container

```bash
docker rm <container-id>
```

8. Remove a local Docker image

```bash
docker rmi <image-name>
```
