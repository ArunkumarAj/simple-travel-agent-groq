# Use official Python image
FROM python:3.12-slim

# Install pipenv and system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    pip install --no-cache-dir pipenv && \
    apt-get clean

# Set work directory
WORKDIR /app

# Copy Pipenv files first (to leverage Docker cache)
COPY Pipfile Pipfile.lock ./

# Install dependencies using pipenv (system-level, not in shell)
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of your project
COPY . .

EXPOSE 8501

# Run the app (adjust based on your script)
CMD ["pipenv", "run", "streamlit", "run", "app.py"]
