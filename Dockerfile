# Use lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /home

# Copy data folder
COPY data /home/data

# Copy script
COPY script.py /home/script.py

# Create output folder
RUN mkdir -p /home/data/output

# Run script automatically
CMD ["python", "/home/script.py"]
