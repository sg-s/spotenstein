# Use a lightweight Python image
FROM python:3.12-slim

# Install ffmpeg and other dependencies
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Install yt-dlp and FastAPI with Uvicorn
RUN pip install yt-dlp fastapi uvicorn

# Set the working directory
WORKDIR /app

# Copy the app files
COPY app.py .

# copy cert files for HTTPS
COPY  mydomain* /etc/ssl/certs/

# Expose port for FastAPI
EXPOSE 5566

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5566","--ssl-keyfile","/etc/ssl/certs/mydomain.key","--ssl-certfile","/etc/ssl/certs/mydomain.crt"]

