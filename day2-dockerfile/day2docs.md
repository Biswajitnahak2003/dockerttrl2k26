# Dockerfiles and Image Layers

A Dockerfile defines how Docker builds a custom image.
It specifies the base image, working directory, which files to copy, build commands, and the default startup command.

## Key Dockerfile instructions

### FROM

Sets the base image.

Example:

```dockerfile
FROM python:3.12-slim
```

### WORKDIR

Sets the working directory inside the image.

Example:

```dockerfile
WORKDIR /app
```

### COPY

Copies files from the host into the image.

Example:

```dockerfile
COPY . .
```

### RUN

Runs a command during build.

Example:

```dockerfile
RUN pip install numpy
```

### CMD and ENTRYPOINT

CMD defines the default command when the container starts.
ENTRYPOINT defines the executable.

Example:

```dockerfile
ENTRYPOINT ["python"]
CMD ["app.py"]
```

## Image layers

Each Dockerfile instruction creates an image layer.
Docker reuses cached layers when nothing changes.
If a file changes, only the affected layer and later layers are rebuilt.