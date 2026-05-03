# Base system: slim Linux with Python 3.11 installed
FROM python:3.11.13-slim

# Create a working directory inside the container
WORKDIR /app

# Copy dependency list first (so Docker caches installs)
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the project
COPY . .

# Command to run when container starts
CMD ["python", "train.py"]
