# 
FROM tiangolo/uvicorn-gunicorn:python3.9-slim 


# Set the working directory to /app

WORKDIR /app


RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
#COPY requirements.txt .
RUN pip install -r requirements.txt
#requirements.txt
#COPY ./app /app
# Make port 80 available to the world outside this container

# Copy the current directory contents into the container at /app
COPY ./app /app/

EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80","--forwarded-allow-ips","'*'"]