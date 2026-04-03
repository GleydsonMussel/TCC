# TCC
Repository for storing my TCC Code:

Collision Avoidance System Using Stereo Cameras

# Dependecies

## Jetson Configuration

### Install NVIDIA Container Toolkit

```console
sudo apt-get update && sudo apt-get install -y --no-install-recommends \
   ca-certificates \
   curl \
   gnupg2
```

```console
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

```console
sudo sed -i -e '/experimental/ s/^#//g' /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

```console
sudo apt-get update 
```

```console
export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.19.0-1
  sudo apt-get install -y \
      nvidia-container-toolkit=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      nvidia-container-toolkit-base=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      libnvidia-container-tools=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      libnvidia-container1=${NVIDIA_CONTAINER_TOOLKIT_VERSION}
```

```console
sudo nvidia-ctk runtime configure --runtime=docker
```

```console
sudo systemctl restart docker
```

```console
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

Run the container:

```console
sudo docker run --rm -it --runtime=nvidia \
  nvcr.io/nvidia/l4t-pytorch:r32.7.1
```

### Setting Up Docker

For build the image:
```console
docker compose up --build
```

In order to enter in the container to execute things:
```console
docker exec -it ID_CONTAINER bash
```

```console
pip3 install pycuda
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