echo "Criando Venv..."
python3 -m venv ./teste

echo "Ativando Ambiente"
source ./teste/bin/activate

echo "Instalando Bibliotecas..."
pip install "ultralytics<8.1" "matplotlib==3.7.5" "Pillow==10.4.0" "opencv-contrib-python==4.13.0.92"