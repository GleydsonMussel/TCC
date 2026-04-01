# TCC
Repository for storing my TCC Code:

Collision Avoidance System Using Stereo Cameras

# Dependecies

## Get UV
```console
curl -LsSf https://astral.sh/uv/install.sh | sh
```
# Jetson Configuration

## Setting Up Docker

For build the image:
```console
docker compose up --build
```

After the image is built, to initialize the container:
```console
docker compose up
```

In order to enter in the container to execute things:
```console
docker exec -it ID_CONTAINER bash
```

# Test Outside Jetson

## Getting Python Version
```console
uv python install 3.8.10
```

## Creating Venv
```console
uv venv --python 3.8.10
```

## Initializing Venv
```console
source .venv/bin/activate
```

## Getting YOLO Ultralytics
```console
uv pip install ultralytics
```

## YOLO Models
Get the YOLO 26 Models [here](https://docs.ultralytics.com/pt/tasks/segment/#predict).