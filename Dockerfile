FROM python:3.11-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy requirements.txt to the docker image and install packages
COPY requirements.txt /
RUN pip install -r requirements.txt

# Set the WORKDIR to be the folder
COPY . /app
WORKDIR /app

# Expose port 8080
EXPOSE 8080
ENV PORT 8080

# Use gunicorn as the entrypoint
# CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
