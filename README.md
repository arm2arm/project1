# Car Plates Detection Project

This repository contains a project template for students' assignments focused on car plate detection.

## Getting Started

### Clone the Repository
To start working with this project, first clone the repository using the following command:

```bash
git clone https://github.com/arm2arm/project1.git
cd project1
```

### Build the Docker Image
Before running the project, you need to build the Docker image. Use the following command:

```bash
docker build --pull --rm -f "Dockerfile" -t "carplatedetection:latest" "."
```

## Running the Application

### For Debugging
If you want to run the application in a debugging environment, use the following command:

```bash
docker run -it carplatedetection:latest /bin/bash
```

### For Production
To deploy the application in a production environment, execute the following command:

```bash
docker run -p 8508:8501 -d --name project1 carplatedetection:latest
```

## Stopping and Cleaning Up

### Stopping the Container
To stop the running container, use the following command:

```bash
docker stop project1
```

### Removing the Container
After stopping the container, you can clean up by removing it with this command:

```bash
docker rm project1
```

---

Feel free to reach out if you have any questions or need further assistance!
