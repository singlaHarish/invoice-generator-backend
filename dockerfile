# Use a lightweight Python image
FROM python:3.12-slim

ENV PYTHONUNBUFFERED True
ENV APP_HOME /app

COPY invoice-generator-backend/requirements.txt ./
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory
WORKDIR $APP_HOME

# Copy all files from the current directory to the container
COPY invoice-generator-backend $APP_HOME/invoice-generator-backend

# Expose the port that the app runs on
EXPOSE 8080

# Command to run the application
CMD ["uvicorn", "invoice-generator-backend.main:app", "--host", "0.0.0.0", "--port", "8080"]

