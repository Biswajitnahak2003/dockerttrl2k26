# FastAPI + Docker

## Today's Goal

Build:

```
Browser
   ↓
FastAPI
   ↓
Docker Container
```

and access it at:

```
http://localhost:8000
```

---

# Step 1: Create Project

```bash
mkdir ~/docker_tutorial-2026/day5-fastapi
cd ~/docker_tutorial-2026/day5-fastapi
```

Create files:

```bash
touch main.py
touch requirements.txt
touch Dockerfile
```

---

# Step 2: Write FastAPI App

`main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello Docker + FastAPI",
        "author": "Biswajit"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
```

---

# Step 3: Requirements

`requirements.txt`

```
fastapi
uvicorn
```

---

# Step 4: Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Let's understand the new things:

### EXPOSE

```dockerfile
EXPOSE 8000
```

Documents that the container intends to use port 8000.

It does **not** publish the port.

This still won't work:

```bash
docker run fastapi-demo
```

You need:

```bash
docker run -p 8000:8000 fastapi-demo
```

---

### Uvicorn

This is the web server.

Equivalent of:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

### main:app

Means:

```
main.py
   ↓
app variable
```

---

# Step 5: Build Image

```bash
docker build -t fastapi-demo .
```

Check:

```bash
docker images
```

---

# Step 6: Run Container

```bash
docker run -p 8000:8000 fastapi-demo
```

You should see logs similar to:

```
INFO: Uvicorn running on http://0.0.0.0:8000
```

---

# Step 7: Test in Browser

Open:

```
http://localhost:8000
```

Expected:

```json
{
  "message": "Hello Docker + FastAPI",
  "author": "Biswajit"
}
```

---

Also test:

```
http://localhost:8000/health
```

Expected:

```json
{
  "status": "healthy"
}
```

---

# Step 8: Swagger UI

One reason FastAPI is loved.

Open:

```
http://localhost:8000/docs
```

You will see interactive API documentation.

This is something recruiters often recognize immediately.

---

# What We Learned

## Topics

### FastAPI

- Modern Python API framework
- Automatic documentation
- Type hints support

### Uvicorn

- ASGI server
- Runs FastAPI applications

### EXPOSE

- Documents container port

### Port Mapping

```bash
docker run -p 8000:8000 fastapi-demo
```

Maps host port 8000 to container port 8000.

### FastAPI in Docker

Allows APIs and ML models to be packaged and deployed consistently.

---

# Why Use This

Later architecture can be:

```
Client
   ↓
FastAPI
   ↓
PyTorch Model
   ↓
Prediction
```

This only returning JSON.

Later we could load:

```python
model = joblib.load("model.pkl")
```

and serve predictions.
