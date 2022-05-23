# ubuntu-psql-docker
Docker container with Ubuntu and PostgreSQL for interactive SQL shell practice.

# Building the image

- create Dockerfile
- run docker build (e.g. `docker build --tag=ngeorge/ubuntu-psql-interactive .`)
- push to docker hub `docker push ngeorge/ubuntu-psql-interactive`
- run the container: `docker run -it ngeorge/ubuntu-psql-interactive`
