# Airflow-docker-project-setup
This repository uses docker to run airflow as a service. It is recommended to use Linux for easier docker setup.

> Requirements:
> - Installed Docker Engine for Linux with latest docker compose version <b>Or</b> Docker Desktop for Windows. Run `docker compose` to check availability
> - 4GB of memory
> - Up to 5GB storage

### Project initiation
1. First, please clone the repository
```
git clone git@github.com:PetrusAriaa/Airflow-docker-project-setup.git yg-stock
```
2. Create a new `.env` file and specify the environment variables based on the example file.
3. Specify your used Python package inside `requirements.txt` file.
4. You can update the installation procedure inside `Dockerfile` to line up your requirements.
5. Start with building the docker base image from `Dockerfile`
```
docker build . --tag <your_image_name:latest>
```
6. Edit the default base image inside `docker-compose.yaml`.
7. Create airflow images and containers using `docker-compose.yaml`
```
docker compose up -d
```
8. Wait until all container building is done. Then, open `http://localhost:8080/` to access airflow-webapp view. Use username `airflow` and password `airflow` to log into the airflow-webapp view.


### Some useful command
- To inspect environment variables inside a running airflow-worker, use:
```
docker exec <container_id> env
```
- To access a running airflow-worker CLI, use:
```
docker exec <continer_id> bash
```
- To stop more than one container at once, use:
```
docker stop $(docker ps -q)
```
