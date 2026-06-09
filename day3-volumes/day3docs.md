# Docker Volumes, Bind Mounts & Environment Variables

# Why Day 3 Matters

Imagine you have:

```text
model.pkl
10GB dataset
API keys
logs
```

Would you want these permanently baked into your Docker image?

**No.**

Because:

- Models change
- Datasets change
- Secrets should not be in images
- Logs should survive container restarts

That's what Volumes, Bind Mounts and Environment Variables solve.

---

# Part 1: Volumes

## Problem

Suppose a container creates:

```text
/app/output.txt
```

Container stops.

Container deleted.

```text
output.txt
❌ Gone
```

Because containers are ephemeral.

---

## Solution: Volume

Create a volume:

```bash
docker volume create mydata
```

Check:

```bash
docker volume ls
```

You should see:

```text
mydata
```

---

## Use Volume

Run:

```bash
docker run -it \
  -v mydata:/data \
  ubuntu:22.04 bash
```

Inside container:

```bash
echo "hello docker" > /data/test.txt
exit
```

Run another container:

```bash
docker run -it \
  -v mydata:/data \
  ubuntu:22.04 bash
```

Check:

```bash
cat /data/test.txt
```

Output:

```text
hello docker
```

The file survived because it lives in the volume, not the container.

---

# AI Example

Volume stores:

```text
models/
datasets/
checkpoints/
logs/
```

For example:

```bash
-v models:/app/models
```

---

# Part 2: Bind Mounts

This is more important for development.

---

## Problem

Suppose:

```text
host machine
│
└── app.py
```

Every time you edit:

```python
print("hello")
```

you don't want:

```bash
docker build
docker run
```

again and again.

---

## Bind Mount

Run:

```bash
docker run -it \
  -v $(pwd):/app \
  python:3.12-slim bash
```

Explanation:

```text
$(pwd)
```

Current folder on host.

Mounted into:

```text
/app
```

inside container.

---

Now:

Host:

```python
print("version 1")
```

Container sees it immediately.

Change:

```python
print("version 2")
```

Container sees updated file immediately.

No rebuild.

---

## Difference

Volume:

```text
Docker manages storage
```

Bind Mount:

```text
Host folder mapped directly
```

---

# Part 3: Environment Variables

## Bad Practice

```python
API_KEY = "secret123"
```

Never do this.

---

## Better

```python
import os

API_KEY = os.getenv("API_KEY")
```

---

Create:

```python
# app.py

import os

print("Model:", os.getenv("MODEL_NAME"))
print("API Key:", os.getenv("API_KEY"))
```

---

Run:

```bash
docker run \
  -e MODEL_NAME=llama3 \
  -e API_KEY=test123 \
  python:3.12-slim \
  python app.py
```

---

## Example

```bash
docker run \
  -e GOOGLE_API_KEY=xxxx \
  -e HF_TOKEN=xxxx \
  my-ai-service
```

---