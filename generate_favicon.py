#!/usr/bin/env python3
"""
Script para gerar favicons em diferentes tamanhos
"""

from PIL import Image, ImageDraw
import os

def create_qr_favicon(size=32):
    """Cria um favicon com design de QR Code"""
    # Criar imagem com fundo dark
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Background dark gradient
    for y in range(size):
        ratio = y / size
        # Gradiente do preto ao cinza escuro
        gray_value = int(10 + (45 - 10) * ratio)  # De #0a0a0a para #2d2d2d
        draw.line([(0, y), (size-1, y)], fill=(gray_value, gray_value, gray_value, 255))
    
    # Escalar elementos baseado no tamanho
    scale = size / 32
    
    def scaled(value):
        return int(value * scale)
    
    # Corner squares (cantos do QR Code) - dourados
    gold_color = (255, 215, 0, 255)  # #FFD700
    dark_color = (26, 26, 26, 255)   # #1a1a1a
    
    # Top-left
    draw.rectangle([scaled(3), scaled(3), scaled(9), scaled(9)], fill=gold_color)
    draw.rectangle([scaled(4), scaled(4), scaled(8), scaled(8)], fill=dark_color)
    draw.rectangle([scaled(5), scaled(5), scaled(7), scaled(7)], fill=gold_color)
    
    # Top-right
    draw.rectangle([scaled(22), scaled(3), scaled(28), scaled(9)], fill=gold_color)
    draw.rectangle([scaled(23), scaled(4), scaled(27), scaled(8)], fill=dark_color)
    draw.rectangle([scaled(24), scaled(5), scaled(26), scaled(7)], fill=gold_color)
    
    # Bottom-left
    draw.rectangle([scaled(3), scaled(22), scaled(9), scaled(28)], fill=gold_color)
    draw.rectangle([scaled(4), scaled(23), scaled(8), scaled(27)], fill=dark_color)
    draw.rectangle([scaled(5), scaled(24), scaled(7), scaled(26)], fill=gold_color)
    
    # Data pattern (pontos do QR Code) - dourados
    data_points = [
        (12, 4), (15, 4), (18, 4),
        (4, 12), (7, 12),
        (12, 8), (15, 8), (18, 8),
        (12, 12), (18, 12),
        (12, 16), (15, 16), (18, 16),
        (12, 20), (18, 20),
        (15, 24), (18, 24),
        (22, 12), (25, 12),
        (22, 16), (27, 16)
    ]
    
    for x, y in data_points:
        draw.rectangle([scaled(x), scaled(y), scaled(x+1), scaled(y+1)], fill=gold_color)
    
    # Center pattern - dourado
    draw.rectangle([scaled(14), scaled(14), scaled(17), scaled(17)], fill=gold_color)
    draw.rectangle([scaled(15), scaled(15), scaled(16), scaled(16)], fill=dark_color)
    
    return img

def generate_favicons():
    """Gera favicons em diferentes tamanhos"""
    sizes = [16, 32, 48, 64, 128, 152, 167, 180, 192, 512]
    base_path = "/home/hendel/Documentos/PROJETOS PROGRAMAÇÃO/CriarQRcode/static/images"
    
    for size in sizes:
        img = create_qr_favicon(size)
        filename = f"favicon-{size}x{size}.png"
        filepath = os.path.join(base_path, filename)
        img.save(filepath, "PNG")
        print(f"✅ Criado: {filename}")
    
    # Criar favicon.ico (múltiplos tamanhos em um arquivo)
    favicon_sizes = [16, 32, 48]
    favicon_images = [create_qr_favicon(size) for size in favicon_sizes]
    favicon_path = os.path.join(base_path, "favicon.ico")
    favicon_images[0].save(favicon_path, format='ICO', sizes=[(size, size) for size in favicon_sizes])
    print(f"✅ Criado: favicon.ico")

if __name__ == "__main__":
    generate_favicons()
    print("\n🎉 Todos os favicons foram gerados com sucesso!")
