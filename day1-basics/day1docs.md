# Docker Basics

This guide explains the core Docker concepts you need to understand before working with containers.

## 1. What is a Container?

A container packages an application with its dependencies and runtime into a single unit.

Example:

- Your project requires:
  - Python 3.12
  - numpy 2.0
  - pandas 2.3
- Another machine has:
  - Python 3.10
  - numpy 1.24

Without containerization, the code may fail because the environment differs.

### Key idea

- Container = portable, isolated box
- Runs the same way everywhere

## 2. Container vs Virtual Machine

### Virtual Machine

A VM includes a full guest operating system.

```
Host OS
│
Hypervisor
│
Guest OS
│
Application
```

- Each VM has its own OS
- Heavy and large
- Slow startup

### Container

Containers share the host kernel and run on the Docker Engine.

```
Host OS
│
Docker Engine
│
Containers
```

- Much lighter than VMs
- Starts in seconds
- Uses less RAM

## 3. Image vs Container

This distinction is extremely important.

### Image

- Blueprint
- Read-only template
- Example: `python:3.12`

Think of an image as a class.

### Container

- Running instance of an image
- Example: `docker run python:3.12`

Think of a container as an object created from the class.

### Analogy

- Image = cake recipe
- Container = actual cake

You can make many cakes from one recipe.

## 4. Docker Engine

Docker Engine is the software that manages containers.

When you run a command like:

```bash
docker run python:3.12
```

Docker Engine will:

- pull the image
- create a container
- start the container
- show the output

## 5. Docker Hub

Docker Hub is like GitHub for Docker images.

Examples of images on Docker Hub:

- `python:3.12`
- `ubuntu`
- `postgres`
- `redis`

Example command:

```bash
docker pull python:3.12
```

This downloads the image from Docker Hub to your local machine.
