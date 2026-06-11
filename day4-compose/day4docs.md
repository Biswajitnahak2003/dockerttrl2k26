# Day 4: Docker Networking & Docker Compose

## Learning Objectives

By the end of today you'll know:

✅ Port Mapping
✅ Docker Networks
✅ Multiple Containers
✅ Docker Compose
✅ Why Compose is used in AI projects

---

## Part 1: Port Mapping

### The Problem

Suppose a Python app runs inside a container on port 8000.

The host machine cannot automatically access it:

```
Container:
  8000

Host:
  ???

No connection.
```

### The Solution

Use the `-p` flag to map ports:

```bash
docker run -p 8000:8000 image_name
```

This means:

```
Host:8000  -->  Container:8000
```

Any traffic on your host's port 8000 goes into the container's port 8000.

---

## Part 2: Network Binding

### Important Interview Question

Why use `0.0.0.0` instead of `127.0.0.1`?

**`127.0.0.1`** = Only accept connections from inside the container (localhost)

**`0.0.0.0`** = Accept connections from anywhere outside the container

```python
# RIGHT: Accept external connections
server = HTTPServer(("0.0.0.0", 8000), Handler)

# WRONG: Only localhost inside container
server = HTTPServer(("127.0.0.1", 8000), Handler)
```

This is a very common interview question!

---

## Part 3: Docker Networks

### List all networks:

```bash
docker network ls
```

You'll see:

```
bridge    (default - containers talk here)
host      (container uses host's network)
none      (no networking)
```

### Inspect the bridge network:

```bash
docker network inspect bridge
```

This shows connected containers and their IP addresses.

---

## Part 4: Two Containers Talking

### The Goal

Make two containers communicate with each other:

```
Container A (box1)
    ↓
Docker Network (mynet)
    ↓
Container B (box2)
```

### Steps

1. Create a custom network:
```bash
docker network create mynet
```

2. Run first container (keep it running):
```bash
docker run -it \
  --name box1 \
  --network mynet \
  ubuntu:22.04 bash
```

3. Open another terminal and run second container:
```bash
docker run -it \
  --name box2 \
  --network mynet \
  ubuntu:22.04 bash
```

4. Inside box2, install ping and test:
```bash
apt update
apt install -y iputils-ping
ping box1
```

5. You should see replies! This proves containers on the same network can communicate by container name.

---

## Part 5: Docker Compose

### Why Compose?

**Before Compose:**

```bash
docker build ...
docker run ...
docker run ...
docker run ...
```

**With Compose:**

```bash
docker compose up
```

Everything builds and runs automatically.

### What Compose Does

```
docker compose up

    ↓

Build images
    ↓
Create network
    ↓
Create containers
    ↓
Start applications
```

All automatically!

### Stopping Compose

```bash
# Stop with Ctrl + C

# Or in another terminal:
docker compose down
```

---

## Part 6: AI Example (Why This Matters)

Later in your Docker journey, you'll deploy entire systems:

```yaml
services:
  api:
    build: .
  
  redis:
    image: redis
  
  postgres:
    image: postgres
```

One command starts everything:

```bash
docker compose up
```

This is how real AI systems are deployed!

---

## Key Concepts

| Concept | Meaning |
|---------|---------|
| Port Mapping | Connect host port to container port using `-p` |
| 0.0.0.0 | Listen on all interfaces (external traffic) |
| 127.0.0.1 | Listen only on localhost (internal only) |
| Docker Network | Virtual network for container-to-container communication |
| Named Network | Custom network (not default bridge) |
| Container Names | Used as DNS inside networks |
| Docker Compose | Declare multi-container apps in YAML |

---
