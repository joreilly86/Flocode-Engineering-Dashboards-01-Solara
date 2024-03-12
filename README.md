# Concrete Slab Weight Calculator using Solara ☀️

A simple, illustrative Python application showcasing [Solara's](https://solara.dev) dashboard capabilities. This project, while functional, serves primarily as a learning tool to create and format a UI and is not intended for serious engineering use. 🚀

## Features
- Interactive UI for calculating the weight of a slab based on geometry and density. 📐
- Dynamic updates with Solara's reactive state management. 🌐

## Further Learning
- For an in-depth exploration, visit my [Flocode Substack newsletter](https://flocode.substack.com). 📘
- Check out [Flocode.dev](https://flocode.dev) for more coding resources for engineers. 💡

*Note: This project is an example and should not replace professional engineering tools.* 🛠️🚧

## Installation and Running the Application

### Dependencies Installation
To install the necessary dependencies, run the following command in your terminal:

```
pip install -r requirements.txt
```

This command will install all the packages listed in the requirements.txt file, ensuring your application has all it needs to run properly.

### Starting the Solara Server
Once you have dependencies installed, to start the Solara server and run the application, use:
```
solara run my_dashboard.py
```

This command will start a local server, typically accessible via a web browser at http://localhost:8765. Open this URL to interact with the application.

### Optional: Running with Docker (Containerized Version) 🐳
For those preferring a containerized environment, you can run the application using Docker. This is particularly useful for ensuring a consistent environment or when preparing for deployment.

#### Building the Docker Image
First, build the Docker image for the application. In the root directory of the project, run:

```bash
docker build -t my_dashboard .
```

This command creates a Docker image named my_dashboard based on the instructions in the Dockerfile.

Running the Application in a Docker Container
To run the application inside a Docker container, use:

```bash
docker run -p 4000:8765 my_dashboard
```
This command starts a Docker container from the my_dashboard image and maps port 8765 inside the container to port 4000 on your host machine.

### Accessing the Application
Once the Docker container is running, access the Solara server by navigating to http://localhost:4000 in your web browser.

Please note that when running locally without Docker, the application is accessible at http://localhost:8765, while the Dockerized version is available at http://localhost:4000.