# CRUD-Flask-MongoDB
## Overview
Flask Application for CRUD operations on MongoDB database for a User resource using a REST API.


## Setup
### Prerequisites
Make sure you have installed the following on your machine:
- [Git](https://git-scm.com/downloads)
- [Docker](https://docs.docker.com/engine/install/)

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/yorozuya-2003/CRUD-Flask-MongoDB.git
    ```

2. Run the Docker container using docker-compose:
    ```sh
    docker compose up
    ```

3. Access the application at http://localhost:5000/.

4. To close the application, press `Ctrl + C` in the terminal where the application is running.


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
  Utilized [Gunicorn](https://gunicorn.org/) to serve the Flask application, providing a robust and efficient WSGI HTTP server for production use.

- **Flask-RESTx for Swagger Documentation:**  
  Implemented [Flask-RESTx](https://flask-restx.readthedocs.io/en/latest/) to create RESTful APIs with built-in [Swagger](https://swagger.io/) documentation, making it easy to document and test the API.

![swagger_1](https://github.com/user-attachments/assets/08baab64-af32-476c-8425-da7cefac8ecc)
![swagger_2](https://github.com/user-attachments/assets/ed2d2885-4762-4240-9741-42b51c66bba4)

- **Docker for Containerization:**  
  Used Docker to containerize the application, running both the Flask app and MongoDB in a single container. This simplifies deployment and ensures consistency across different environments.

- **Handled User Input Edge Cases:**  
  Implemented validation checks to handle edge cases such as invalid email address format and missing user data.

- **Persistent Data Storage:**  
  Used volume to store MongoDB data, ensuring that the data persists even after the container is stopped or restarted.

## Accessing the MongoDB Shell
1. Find the container ID of the MongoDB container:
    ```sh
    docker ps
    ```
2. Use the container id of `mongo:latest` from the output of the previous command. Run the following command to access the MongoDB shell:
    ```sh
    docker exec -it {docker-container-id-of-mongo:latest} mongosh --authenticationDatabase "admin" -u {username} -p {password}
    ```


## Modifying MongoDB Credentials
### Before initializing the database
If you want to modify the MongoDB credentials before initializing the database (starting the application container), you can do so by modifying the following environment variables in the `.env` file:
- `MONGO_INITDB_ROOT_USERNAME`
- `MONGO_INITDB_ROOT_PASSWORD`
- `MONGO_INITDB_DATABASE`

### After initializing the database
If you want to modify the MongoDB credentials after initializing the database, you can do so by following these steps:
1. Access the MongoDB shell in the running container:
    ```sh
    docker exec -it {docker-container-id-of-mongo:latest} mongosh -port 27017 -authenticationDatabase "admin" -u "old-username" -p "old-password"
    ```
2. To change the root user password, run the following commands:
    ```sh
    use admin
    ```
    
    ```sh
    db.changeUserPassword('old-username', 'new-password')
    ```
    **OR**  


    To add a new user, run the following commands (modify permissions and database names according to requirements):
    ```sh
    use admin
    ```

    ```sh
    db.createUser({user: "new-username", pwd: "new-password", roles: [{role: "readWrite", db: "database-name (users_db)"}]});
    ```
3. Exit the MongoDB shell by running the command:
    ```sh
    exit
    ```

4. Update the following environment variables in the `.env` file:
  - `MONGO_INITDB_ROOT_USERNAME` = (new-username)
  - `MONGO_INITDB_ROOT_PASSWORD` = (new-password)
  - `MONGO_INITDB_DATABASE` = (database-name)

5. Stop the running application container by `Ctrl + C` and run the following command to restart the app:
    ```sh
    docker compose up --build
    ```


## Author
[Tanish Pagaria](https://github.com/yorozuya-2003)  
*(IIT Jodhpur Undergraduate)*
