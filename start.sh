#!/bin/bash

# Script de inicialização para Railway
echo "🚀 Starting QR Code Generator..."

# Instalar dependências se necessário
echo "📦 Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

# Inicializar aplicação
echo "🔧 Initializing application..."
python init.py

# Iniciar servidor
echo "🌐 Starting server on port $PORT..."
exec gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 30
