echo "Criando Venv..."
python3 -m venv ./venv

echo "Ativando Ambiente"
source ./venv/bin/activate

echo "Instalando Bibliotecas..."
pip install -r ./requirements.txt