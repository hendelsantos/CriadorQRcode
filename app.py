from flask import Flask, render_template, request, jsonify, send_file
import qrcode
from io import BytesIO
import base64
import re

app = Flask(__name__)

def is_valid_phone(phone):
    """Valida se o número de telefone está em formato válido"""
    # Remove todos os caracteres não numéricos
    clean_phone = re.sub(r'\D', '', phone)
    # Verifica se tem entre 10 e 15 dígitos (padrão internacional)
    return len(clean_phone) >= 10 and len(clean_phone) <= 15

def format_whatsapp_url(phone):
    """Formata o número para URL do WhatsApp"""
    # Remove todos os caracteres não numéricos
    clean_phone = re.sub(r'\D', '', phone)
    
    # Se não começar com código do país, assume Brasil (+55)
    if not clean_phone.startswith('55') and len(clean_phone) == 11:
        clean_phone = '55' + clean_phone
    
    return f"https://wa.me/{clean_phone}"

def is_valid_url(url):
    """Valida se é uma URL válida"""
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url_pattern.match(url) is not None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/manifest.json')
def manifest():
    return send_file('static/manifest.json', mimetype='application/json')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    try:
        data = request.get_json()
        content_type = data.get('type')
        content = data.get('content', '').strip()
        
        if not content:
            return jsonify({'error': 'Conteúdo não pode estar vazio'}), 400
        
        # Processa o conteúdo baseado no tipo
        if content_type == 'whatsapp':
            if not is_valid_phone(content):
                return jsonify({'error': 'Número de telefone inválido'}), 400
            qr_data = format_whatsapp_url(content)
        elif content_type == 'url':
            if not content.startswith(('http://', 'https://')):
                content = 'https://' + content
            if not is_valid_url(content):
                return jsonify({'error': 'URL inválida'}), 400
            qr_data = content
        else:  # text
            qr_data = content
        
        # Gera o QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        
        # Cria a imagem
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Converte para base64
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        
        img_str = base64.b64encode(buffer.getvalue()).decode()
        
        return jsonify({
            'success': True,
            'image': f"data:image/png;base64,{img_str}",
            'data': qr_data
        })
        
    except Exception as e:
        return jsonify({'error': f'Erro ao gerar QR Code: {str(e)}'}), 500

@app.route('/download_qr', methods=['POST'])
def download_qr():
    try:
        data = request.get_json()
        content_type = data.get('type')
        content = data.get('content', '').strip()
        
        if content_type == 'whatsapp':
            qr_data = format_whatsapp_url(content)
        elif content_type == 'url':
            if not content.startswith(('http://', 'https://')):
                content = 'https://' + content
            qr_data = content
        else:
            qr_data = content
        
        # Gera o QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        
        # Cria a imagem
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Salva em buffer
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        
        return send_file(
            buffer,
            mimetype='image/png',
            as_attachment=True,
            download_name='qrcode.png'
        )
        
    except Exception as e:
        return jsonify({'error': f'Erro ao baixar QR Code: {str(e)}'}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
