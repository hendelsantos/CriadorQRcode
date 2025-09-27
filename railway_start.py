#!/usr/bin/env python3
import subprocess
import sys

# Instalar dependências
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Iniciar a aplicação
if __name__ == "__main__":
    from app import app
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
