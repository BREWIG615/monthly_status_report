# Use official TeX Live image with Python installed
FROM debian:bullseye

# Set non-interactive mode for APT
ENV DEBIAN_FRONTEND=noninteractive

# Install basic packages, Python, pip, and LaTeX
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    texlive-full \
    git \
    make \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy only requirements first to enable Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the project into the container
COPY . .

# Default command to run the script
CMD ["python3", "main.py"]