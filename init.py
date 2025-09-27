#!/usr/bin/env python3
"""
Script de inicialização para garantir que as pastas necessárias existam
e que a aplicação seja iniciada corretamente no Railway
"""

import os
import sys
from pathlib import Path

def ensure_directories():
    """Garante que os diretórios necessários existam"""
    base_dir = Path(__file__).parent
    
    directories = [
        base_dir / 'static' / 'images',
        base_dir / 'templates',
        base_dir / 'static' / 'css',
        base_dir / 'static' / 'js'
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"✅ Directory ensured: {directory}")

def check_required_files():
    """Verifica se os arquivos necessários existem"""
    base_dir = Path(__file__).parent
    
    required_files = [
        'app.py',
        'requirements.txt',
        'static/css/style.css',
        'static/js/script.js',
        'templates/index.html'
    ]
    
    missing_files = []
    for file_path in required_files:
        full_path = base_dir / file_path
        if not full_path.exists():
            missing_files.append(file_path)
        else:
            print(f"✅ Required file found: {file_path}")
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    
    return True

def setup_environment():
    """Configura variáveis de ambiente se necessário"""
    if not os.environ.get('PORT'):
        os.environ['PORT'] = '5000'
        print("🔧 Set default PORT=5000")
    
    if not os.environ.get('FLASK_ENV'):
        os.environ['FLASK_ENV'] = 'production'
        print("🔧 Set FLASK_ENV=production")

def main():
    print("🚀 Starting QR Code Generator initialization...")
    
    # Garantir diretórios
    ensure_directories()
    
    # Verificar arquivos necessários
    if not check_required_files():
        print("❌ Initialization failed - missing required files")
        sys.exit(1)
    
    # Configurar ambiente
    setup_environment()
    
    print("✅ Initialization completed successfully!")
    print(f"🌐 App will run on port: {os.environ.get('PORT')}")
    
    return True

if __name__ == "__main__":
    main()
