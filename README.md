# TCC
Repository for storing my TCC Code:

Collision Avoidance System Using Stereo Cameras

# Dependecies

## Jetson Configuration

### CUDA
Check if CUDA is fine:
```console
nvcc --version
```

If the command is found, and it returns something, then CUDA is ready to go !

If it does not, try setting CUDA in in bashrc:

```console
sudo nano ~/.bashrc
```

Copy and paste the following in the end of the file:

```console
export PATH=/usr/local/cuda-10.2/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64:$LD_LIBRARY_PATH
```

Reload the `~/.bashrc`:

```console
source ~/.bashrc
```

### Install ZED SDK

In order to make things easier, in the `/ZED_SDK/` I already put the the `.run` file needed.

You can get the ZED SDK for Ubuntu 18.04 for Jetson Nano [here](https://www.stereolabs.com/en-br/developers/release/3.8). Download 
the `ZED SDK for L4T 32.7 (JetPack 4.6.X) 3.8.2 (Jetson Nano, TX2/TX2 NX, Xavier AGX/NX, CUDA 10.2)` version.

You can also install via terminal, which is recommended instead of getting via web browser:
```console
cd ~/Downloads
wget https://stereolabs.sfo2.cdn.digitaloceanspaces.com/zedsdk/3.8/ZED_SDK_Tegra_L4T32.7_v3.8.2.zstd.run
```

After getting the .run file:
```console
# Instalar o zstd (necessário para descompactar)
sudo apt update
sudo apt install zstd

# Dar permissão de execução
chmod +x ZED_SDK_Tegra_L4T32.7_v3.8.2.zstd.run

# Executar o instalador
./ZED_SDK_Tegra_L4T32.7_v3.8.2.zstd.run
```

### ZED ROS Wrapper

The last ZED ROS Wrapper with compatibility for `ROS Melodic` is the 3.8.x. It's already present in the `/src/` folder and was got from 
[here](https://github.com/stereolabs/zed-ros-wrapper/releases).

### Install ROS Melodic

Setup your computer to accept software from packages.ros.org.

```console
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

Set up your keys

```console
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

Update the repositories
```console
sudo apt update
```

Get the full `ROS Melodic`
```console
sudo apt install ros-melodic-desktop-full
```

After the `ROS Melodic` is installed, put it on the ~/.bashrc:
```console
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
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