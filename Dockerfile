FROM python:3.9-slim

# Install Flask and Kubernetes client
RUN pip install Flask kubernetes

# Copy the webhook server code
COPY webhook.py /app/webhook.py

# Expose port 443 (for HTTPS)
EXPOSE 443

# Run the Flask application
CMD ["python", "/app/webhook.py"]

