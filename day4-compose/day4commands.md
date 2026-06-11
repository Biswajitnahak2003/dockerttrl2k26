# Day 4 Commands

## Part 1: Setup and Port Mapping

Navigate to the folder:

```bash
cd ~/docker_tutorial-2026/day4-compose
```

Build the Docker image:

```bash
docker build -t network-demo .
```

Run with port mapping (host:container):

```bash
docker run -p 8000:8000 network-demo
```

The server will start. Open your browser and go to:

```
http://localhost:8000
```

You should see: `Hello Docker Networking!`

Stop the container: `CTRL + C`

---

## Part 2: Docker Networks

List all networks:

```bash
docker network ls
```

Inspect the default bridge network:

```bash
docker network inspect bridge
```

Create a custom network:

```bash
docker network create mynet
```

List networks again to see your new network:

```bash
docker network ls
```

---

## Part 3: Two Containers Talking

### Terminal 1: Run first container

```bash
docker run -it \
  --name box1 \
  --network mynet \
  ubuntu:22.04 bash
```

Keep this terminal open (container running).

### Terminal 2: Run second container

Open a new terminal and run:

```bash
docker run -it \
  --name box2 \
  --network mynet \
  ubuntu:22.04 bash
```

### Inside box2: Test network communication

Install ping utility:

```bash
apt update
apt install -y iputils-ping
```

Ping the first container by name:

```bash
ping box1
```

You should see replies with IP addresses. This proves container-to-container communication works!

Exit box2:

```bash
exit
```

Exit box1 (in Terminal 1):

```bash
exit
```

Clean up the network:

```bash
docker network rm mynet
```

---

## Part 4: Docker Compose

Run the entire application with one command:

```bash
docker compose up
```

Docker will:
1. Build the image
2. Create a network
3. Start the container
4. Bind port 8000

Open browser: `http://localhost:8000`

Stop compose:

```bash
CTRL + C
```

Or in another terminal:

```bash
docker compose down
```

View logs:

```bash
docker compose logs
```

---

## Quick Reference

| Command | Purpose |
|---------|---------|
| `docker build -t name .` | Build image |
| `docker run -p 8000:8000 image` | Run with port mapping |
| `docker network ls` | List networks |
| `docker network create name` | Create network |
| `docker run --network name image` | Run on custom network |
| `docker compose up` | Start all services |
| `docker compose down` | Stop all services |
| `docker compose logs` | View logs |
