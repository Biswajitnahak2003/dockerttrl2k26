import os

model_name = os.getenv("MODEL_NAME", "not set")
api_key = os.getenv("API_KEY", "not set")
data_dir = os.getenv("DATA_DIR", "/data")

print("Model:", model_name)
print("API Key:", api_key)
print("Data directory:", data_dir)
print("Data directory exists:", os.path.isdir(data_dir))

if os.path.isdir(data_dir):
    print("Files in data directory:")
    for path in sorted(os.listdir(data_dir)):
        print("-", path)
