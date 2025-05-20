
# Demo Custom Agent

This repository provides Docker-based setup for building and running the **Demo Custom Agent** application.

---

## Initial Setup (Manual Run)

Before using Docker, you can run the application locally for development or testing:

1.1 Create and activate a Conda environment:

   ```bash
   conda create --name demo-agent-env python=3.11 -y
   conda activate '<path>\demo-agent-env'   
   ```

1.2 Create and activate through pipenv:

   a. Install Pipenv (if not already installed)
   ```bash
   pip install --user pipenv   
   ```
   b. Initialize a Pipenv Environment:

   1. Start with a Python version: >> This creates a virtual environment and a `Pipfile`.
   
         ```bash
         pipenv --python 3.11         
         ```

   2. Or just install your first package:

         ```bash
         pipenv install <package-name>      
         ```

      This auto-creates the virtual environment using your system’s default Python, and adds flask to the Pipfile.

   3. Activate the Virtual Environment: >> `(myproject-abc123) PS C:\path\to\myproject>`

         ```bash
         pipenv shell
         ```
   4. Exit the Shell

         ```bash
         exit
         ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit application in local:

   ```bash
   streamlit run app.py
   ```

> Make sure your environment variables are set correctly, either via `.env` or export commands.

---

## Overview

You can run this project using either:

- **Docker CLI** (manual build and run of container)  
- **Docker Compose** (automated multi-container orchestration)

---

## Quick Start

### Using Docker CLI

1. **Build the image:**

   ```bash
   docker build -t demo-custom-agent .
   ```

2. **Run the container:**  ## --env-file .env 

   ```bash
   docker run -p 8501:8501 -e GROQ_API_KEY='<GROQ_API_KEY>'  -it demo-custom-agent:latest_build
   ```
   Let's say port `8501`, as it is the default port used by Streamlit
### Using Docker Compose

   1. Build and start the service with:
      ```bash
      docker-compose up --build
      ```
   2. To View the app in browser:
      ```bash
      http://0.0.0.0:8501 or http://localhost:8501
      ```
   3. Stop and clean up with:
      ```bash
      docker-compose down -v
      ```
---

## Notes

- Environment variables are managed via a `.env` file (ensure it is listed in `.gitignore`).
- Port `8501` is exposed for application access.
- Use `--build` flag with Docker Compose to rebuild images after changes.

---

## Cleanup Commands

- List containers:
  ```bash
  docker ps -a
  ```

- Remove containers and images as needed using Docker CLI commands.

---

## Reference: Docker Commands Used for Practice

Here are some of the key Docker commands used during development and practice:

```bash
docker build demo-custom-agent .
docker build -t demo-custom-agent .

docker images

docker run -p 8501:8501 --env-file .env -it demo-custom-agent

docker ps -a

docker stop demo-custom-agent && docker rm demo-custom-agent
docker stop <container_id> && docker rm <container_id>

docker rmi <image_id>

docker-compose up --build
docker-compose down -v

echo ".env" >> .gitignore
```


For detailed instructions, please refer to the full documentation in this repo.
