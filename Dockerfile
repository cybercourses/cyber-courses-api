# Courses API (Flask) — generic Dockerfile for Docker-based free hosts
# (Back4App Containers, Northflank, any Docker host).
# Render ignores this file (it uses render.yaml). PythonAnywhere does not use it.
# No secrets in this file: API_HOSTED_MODE and INTERNAL_SECRET are set
# in the host's dashboard at deploy time, never here.
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Back4App serves the container on port 8080; most other hosts set $PORT.
# Bind $PORT when present, else 8080.
CMD ["sh", "-c", "gunicorn --chdir server app:app --bind 0.0.0.0:${PORT:-8080} --workers 1 --threads 4 --timeout 120"]
