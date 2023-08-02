# Use a base Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the backend code and requirements.txt into the container
COPY wednesday /app/wednesday
COPY app.py /app
COPY requirements.txt /app
COPY setup.py /app

# Install backend dependencies
RUN pip install -r requirements.txt

RUN python setup.py install

EXPOSE 8080

# Command to start the Flask app
CMD ["python", "app.py"]