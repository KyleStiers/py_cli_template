# Build the base image with uv
FROM ghcr.io/astral-sh/uv:debian-slim AS builder

# Set the working directory
WORKDIR /app

# Copy your application code if needed
COPY . /app

# Download the dependencies into the container
RUN uv sync

# Set the entry point so that we can use the tool seamlessly
ENTRYPOINT ["uv", "run"]