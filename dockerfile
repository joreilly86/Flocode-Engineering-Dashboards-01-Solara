# Use an official Python runtime as a base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available
EXPOSE 8765

# Define environment variable
ENV NAME World

# Run the Solara application
CMD ["solara", "run", "my_dashboard.py", "--host=0.0.0.0"]

# Solara server started. You can access the app at http://localhost:4000