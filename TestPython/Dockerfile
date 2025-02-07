# Use Python 3.13.2 official image as the base
FROM python:3.13.2-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY ./requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY ./main.py .

# Expose the port that the app will run on
EXPOSE 8000

# Start the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]