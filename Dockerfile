
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy files and install requirements
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for FastAPI
EXPOSE 8000

# Default command (overridden in docker-compose for workers)
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
