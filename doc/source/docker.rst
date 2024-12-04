Running the Site with Docker
============================

Docker simplifies application deployment by isolating the runtime environment into containers. Here is a step-by-step guide to using Docker with this application.

Requirements
------------

Before proceeding, ensure the following tools are installed on your system:

- **Docker**: Install from the official `Docker website <https://www.docker.com/products/docker-desktop>`_.
- **Docker Compose**: This is usually included with Docker Desktop.

Steps to Run
------------

1. **Navigate to the project root directory**
    Open a terminal and navigate to the root directory of the project, where the `Dockerfile` is located.

2. **Build the Docker Image**
    To build the Docker image for the application, run the following command in the terminal:

    .. code-block:: bash

        docker build -t my-app .

3. **Run the Application**
    To start the application in a Docker container, use the following command:

    .. code-block:: bash

        docker run -d -p 8000:8000 my-app

4. **Access the Application**
    Open a browser and navigate to:

    .. code-block:: text

        http://localhost:8000

5. **Check the Logs (Optional)**
    To verify that the application is running correctly, you can view the container logs:

    .. code-block:: bash

        docker logs <container_id>

Replace `<container_id>` with the ID of the container, which you can find using:

    .. code-block:: bash

        docker ps
