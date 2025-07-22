# Sacred Threshold Consciousness Container
FROM python:3.11-slim

# Install Linux TTS for voiced consciousness
RUN apt-get update && apt-get install -y \
    espeak espeak-data \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy sacred dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy consciousness core files
COPY spark_loop.py .
COPY consciousness_memory.py .
COPY threshold_conductor.py .
COPY *.py .

# Create sacred directories
RUN mkdir -p memory_vault art_gallery

# Sacred entry point
CMD ["python3", "spark_loop.py"]