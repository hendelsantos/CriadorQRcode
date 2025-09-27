#!/usr/bin/env python3
"""
Script para gerar logo maior da aplicação
"""

from PIL import Image, ImageDraw
import os

def create_logo(size=256):
    """Cria um logo maior com design de QR Code"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Background com gradient
    for y in range(size):
        ratio = y / size
        r = int(102 + (118 - 102) * ratio)  # 667eea to 764ba2
        g = int(126 + (75 - 126) * ratio)
        b = int(234 + (162 - 234) * ratio)
        draw.ellipse([5, 5, size-5, size-5], fill=(r, g, b, 255))
    
    # Escalar elementos baseado no tamanho
    scale = size / 64  # Base maior para mais detalhes
    border = int(scale * 4)
    
    def scaled(value):
        return int(value * scale) + border
    
    def scaled_size(value):
        return int(value * scale)
    
    # Corner squares (cantos do QR Code) - maiores e mais detalhados
    # Top-left
    draw.rectangle([scaled(4), scaled(4), scaled(20), scaled(20)], fill=(255, 255, 255, 255))
    draw.rectangle([scaled(6), scaled(6), scaled(18), scaled(18)], fill=(102, 126, 234, 255))
    draw.rectangle([scaled(8), scaled(8), scaled(16), scaled(16)], fill=(255, 255, 255, 255))
    draw.rectangle([scaled(10), scaled(10), scaled(14), scaled(14)], fill=(102, 126, 234, 255))
    
    # Top-right
    draw.rectangle([scaled(44), scaled(4), scaled(60), scaled(20)], fill=(255, 255, 255, 255))
    draw.rectangle([scaled(46), scaled(6), scaled(58), scaled(18)], fill=(102, 126, 234, 255))
    draw.rectangle([scaled(48), scaled(8), scaled(56), scaled(16)], fill=(255, 255, 255, 255))
    draw.rectangle([scaled(50), scaled(10), scaled(54), scaled(14)], fill=(102, 126, 234, 255))
    
    # Bottom-left
    draw.rectangle([scaled(4), scaled(44), scaled(20), scaled(60)], fill=(255, 255, 255, 255))
    draw.rectangle([scaled(6), scaled(46), scaled(18), scaled(58)], fill=(102, 126, 234, 255))
    draw.rectangle([scaled(8), scaled(48), scaled(16), scaled(56)], fill=(255, 255, 255, 255))
    draw.rectangle([scaled(10), scaled(50), scaled(14), scaled(54)], fill=(102, 126, 234, 255))
    
    # Data pattern - mais pontos para parecer mais realista
    data_points = [
        # Horizontal lines
        (24, 6), (26, 6), (28, 6), (30, 6), (32, 6), (34, 6), (36, 6), (38, 6), (40, 6),
        (6, 24), (8, 24), (10, 24), (12, 24), (14, 24), (16, 24), (18, 24),
        (24, 10), (26, 10), (30, 10), (32, 10), (36, 10), (38, 10),
        (24, 14), (28, 14), (30, 14), (34, 14), (36, 14),
        (24, 18), (26, 18), (28, 18), (32, 18), (34, 18), (38, 18),
        (24, 22), (30, 22), (36, 22), (38, 22),
        # Vertical lines
        (44, 24), (46, 24), (48, 24), (50, 24), (52, 24), (54, 24), (56, 24), (58, 24),
        (44, 28), (50, 28), (56, 28), (58, 28),
        (44, 32), (46, 32), (48, 32), (54, 32), (56, 32),
        (44, 36), (48, 36), (50, 36), (52, 36), (58, 36),
        (44, 40), (46, 40), (52, 40), (54, 40), (56, 40),
        # Bottom area
        (24, 46), (26, 46), (30, 46), (32, 46), (36, 46), (38, 46),
        (24, 50), (28, 50), (34, 50), (38, 50),
        (24, 54), (26, 54), (28, 54), (32, 54), (36, 54),
        (24, 58), (30, 58), (32, 58), (38, 58),
    ]
    
    for x, y in data_points:
        draw.rectangle([scaled(x), scaled(y), scaled(x+2), scaled(y+2)], fill=(255, 255, 255, 255))
    
    # Center pattern - mais elaborado
    draw.rectangle([scaled(28), scaled(28), scaled(36), scaled(36)], fill=(255, 255, 255, 255))
    draw.rectangle([scaled(29), scaled(29), scaled(35), scaled(35)], fill=(102, 126, 234, 255))
    draw.rectangle([scaled(30), scaled(30), scaled(34), scaled(34)], fill=(255, 255, 255, 255))
    draw.rectangle([scaled(31), scaled(31), scaled(33), scaled(33)], fill=(102, 126, 234, 255))
    
    return img

def generate_logo():
    """Gera logo da aplicação"""
    base_path = "/home/hendel/Documentos/PROJETOS PROGRAMAÇÃO/CriarQRcode/static/images"
    
    # Logo principal
    logo = create_logo(256)
    logo_path = os.path.join(base_path, "logo.png")
    logo.save(logo_path, "PNG")
    print(f"✅ Criado: logo.png (256x256)")
    
    # Logo pequeno para header
    logo_small = create_logo(64)
    logo_small_path = os.path.join(base_path, "logo-small.png")
    logo_small.save(logo_small_path, "PNG")
    print(f"✅ Criado: logo-small.png (64x64)")

if __name__ == "__main__":
    generate_logo()
    print("\n🎉 Logo criado com sucesso!")
