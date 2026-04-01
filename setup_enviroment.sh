echo "Criando Venv..."
python3 -m venv ./teste

echo "Ativando Ambiente"
source ./teste/bin/activate

echo "Instalando Bibliotecas..."
pip install "ultralytics<8.1" matplotlib Pillow opencv-contrib-python