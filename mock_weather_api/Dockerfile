# ---- Build Stage ----
FROM python:3.12-bookworm AS builder

# Set environment variables
ENV POETRY_VERSION=1.8.1
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_NO_INTERACTION=1
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install Poetry and build dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y curl build-essential && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy only the dependency definitions first to leverage Docker's cache
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --only main --no-root

# Copy the rest of the app
COPY mock_weather_api/mock_weather_api.py .

# Install the app in the virtual environment
RUN poetry install --no-dev

# ---- Run Stage ----
FROM python:3.12-bookworm AS runner

# Set environment variables (same as build stage for Poetry)
ENV PYTHONPATH=/app

WORKDIR /app

# Copy the virtual environment and source code from the build stage
COPY --from=builder /app /app

COPY mock_data /app/mock_data

EXPOSE 5000

# Run the application
CMD ["/app/.venv/bin/python", "mock_weather_api.py"]
