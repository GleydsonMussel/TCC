# TCC
Repository for storing my TCC Code:

Collision Avoidance System Using Stereo Cameras

# Dependecies

## Jetson Configuration

### Install NVIDIA Container Toolkit

### Setting Up Docker

For build the image:
```console
docker compose up --build
```

In order to enter in the container to execute things:
```console
docker exec -it ID_CONTAINER bash
```

## Test Outside Jetson

### Getting ARM Architecture in Docker

In order to run the system outside the Jetson, but still having the `ARM` architecture, it's necessary install some things to make
docker able to do so. 

Run:
```console
sudo docker run --privileged --rm tonistiigi/binfmt --install all
```

This will install the ARM support

To build the image and run the container:
```console
docker compose up --build
```

It's recommended to use the dev-container extension to use the deployed container to develop, for that, download the extension and use
`Ctrl` + `Shift` + `p`.

## Setting Python Dependencies

To install all the dependencies needed and setup the venv, run:
```console
chmod +x setup_enviroment.sh
./setup_enviroment.sh
```
## YOLO Models

Get the YOLO 26 Models [here](https://docs.ultralytics.com/pt/tasks/segment/#predict).

Get the YOLO 8 Models [here](https://docs.ultralytics.com/pt/models/yolov8/#yolov8-usage-examples).