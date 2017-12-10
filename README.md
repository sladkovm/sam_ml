# sam_ml
Machine learning module for Strava Activity Map

# Makefile and Docker

- `make build` - build docker jupyther/scipy-notebook container and installs your requirements.txt to it. 

   (for more details, check: https://github.com/jupyter/docker-stacks)

- `make server` - starts jupyther from within docker container, by default on port 8888 and proxies your project root to it

- `make stop_server` - stops the server
