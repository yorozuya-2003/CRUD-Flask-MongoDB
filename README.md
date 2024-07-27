# CRUD-Flask-MongoDB
## Overview
Flask Application for CRUD operations on MongoDB database for a User resource using a REST API.


## Setup
### Prerequisites
Make sure you have installed the following prerequisites on your machine:
- [Git](https://git-scm.com/downloads)
- [Docker](https://docs.docker.com/engine/install/)

### Steps
1. **Clone the repository:**
    ```sh
    https://github.com/yorozuya-2003/CRUD-Flask-MongoDB.git
    ```

2. **Run the Docker container using docker-compose:**
    ```sh
    docker-compose up
    ```

3. Access the application at http://localhost:5000/.


## File Structure

| File/Directory       | Description                                |
|----------------------|--------------------------------------------|
| `.env`               | Environment variables                      |
| `app.py`             | Main flask application python script       |
| `docker-compose.yml` | Docker Compose configuration file          |
| `Dockerfile`         | Dockerfile for flask app                   |
| `mongo_handler.py`   | MongoDB python client script               |
| `requirements.txt`   | Python dependencies                        |
| `utils.py`           | Helper functions python script             |


## REST API Endpoints

| Method | Endpoint        | Description                                      |
|--------|-----------------|--------------------------------------------------|
| GET    | /users          | Returns a list of all users                      |
| GET    | /users/\<id\>   | Returns the user with the specified ID           |
| POST   | /users          | Creates a new user with the specified data       |
| PUT    | /users/\<id\>   | Updates the user with the specified ID with the new data |
| DELETE | /users/\<id\>   | Deletes the user with the specified ID           |


## Features
- **Gunicorn Integration:**  
  Utilizes [Gunicorn](https://gunicorn.org/) to serve the Flask application, providing a robust and efficient WSGI HTTP server for production use.

- **Flask-RESTx for Swagger Documentation:**  
  Implements [Flask-RESTx](https://flask-restx.readthedocs.io/en/latest/) to create RESTful APIs with built-in [Swagger](https://swagger.io/) documentation, making it easy to document and test the API.

![swagger_1](https://github.com/user-attachments/assets/08baab64-af32-476c-8425-da7cefac8ecc)
![swagger_2](https://github.com/user-attachments/assets/ed2d2885-4762-4240-9741-42b51c66bba4)

- **Docker for Containerization:**  
  Uses Docker to containerize the application, running both the Flask app and MongoDB in a single container. This simplifies deployment and ensures consistency across different environments.

- **Handled User Input Edge Cases:**  
  Implemented validation checks to handle edge cases such as invalid email address format and missing user data.


## Author
[Tanish Pagaria](https://github.com/yorozuya-2003)  
*(IIT Jodhpur Undergraduate)*
