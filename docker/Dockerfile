# Use Ubuntu 18.04 (igual ao Jetson Nano)
FROM ubuntu:18.04

# Configurações de ambiente
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV PYTHONIOENCODING=UTF-8

# Variáveis simulando CUDA do Jetson Nano (sem GPU real)
ENV CUDA_VERSION=10.2
ENV PATH=/usr/local/cuda-10.2/bin:${PATH}
ENV LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64:${LD_LIBRARY_PATH}

# Instala dependências base
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    software-properties-common \
    lsb-release \
    sudo \
    wget \
    build-essential \
    cmake \
    git \
    python3-pip \
    python3-dev \
    python3-venv \
    python3-rosdep \
    python3-rosinstall \
    python3-rosinstall-generator \
    libopenblas-dev \
    liblapack-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    nano \
    vim \
    && rm -rf /var/lib/apt/lists/*

# ===== CONFIGURAÇÃO DO ROS MELODIC =====
# Adiciona repositório ROS
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu bionic main" > /etc/apt/sources.list.d/ros-latest.list'
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -

# Instala ROS Melodic Desktop
RUN apt-get update && apt-get install -y \
    ros-melodic-desktop-full \
    python3-catkin-tools \
    python3-vcstool \
    && rm -rf /var/lib/apt/lists/*

# ===== CONFIGURAÇÃO DO PYTHON 3.11 PARA YOLO26 =====
# Adiciona Dead Snakes PPA
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3.11-dev \
    python3.11-venv \
    && rm -rf /var/lib/apt/lists/*

# Instala pip para Python 3.11
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11

# Cria ambiente virtual para YOLO26
RUN python3.11 -m venv /opt/yolo26_env

# Instala dependências do YOLO26 (simulando Jetson Nano - CPU only)
RUN /opt/yolo26_env/bin/pip install --upgrade pip setuptools wheel && \
    /opt/yolo26_env/bin/pip install \
    numpy==1.24.4 \
    opencv-python==4.8.1.78 \
    matplotlib \
    pillow \
    scipy \
    tqdm \
    seaborn \
    pandas \
    pyyaml \
    easydict \
    torch \
    torchvision \
    ultralytics

# Instala pacotes ROS para Python 3.11 (necessários para interoperabilidade)
RUN /opt/yolo26_env/bin/pip install \
    rospkg \
    catkin-pkg \
    empy \
    pyyaml \
    cv-bridge \
    sensor-msgs \
    geometry-msgs

# ===== CONFIGURAÇÃO DO ENTRYPOINT =====
RUN echo '#!/bin/bash\n\
# Seta ambiente ROS\n\
source /opt/ros/melodic/setup.bash\n\
\n\
# Ativa YOLO26 environment\n\
export PATH="/opt/yolo26_env/bin:$PATH"\n\
export PYTHONPATH="/opt/yolo26_env/lib/python3.11/site-packages:$PYTHONPATH"\n\
\n\
# Simula CUDA do Jetson (sem aceleração real)\n\
export CUDA_VISIBLE_DEVICES=-1  # Força CPU\n\
\n\
exec "$@"\n\
' > /entrypoint.sh && chmod +x /entrypoint.sh

# Configura bashrc
RUN echo "source /opt/ros/melodic/setup.bash" >> /root/.bashrc
RUN echo "export PATH=/opt/yolo26_env/bin:\$PATH" >> /root/.bashrc
RUN echo "export PYTHONPATH=/opt/yolo26_env/lib/python3.11/site-packages:\$PYTHONPATH" >> /root/.bashrc

# Inicializa rosdep
RUN rosdep init && rosdep update

WORKDIR /workspace

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]