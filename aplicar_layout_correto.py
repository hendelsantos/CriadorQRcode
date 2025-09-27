#!/usr/bin/env python3
"""
🔧 CORREÇÃO SIMPLES DE LAYOUT
=============================
Aplicar layout correto do Batman a todos os temas
"""

import os
import shutil

# Fazer backup de todos os temas primeiro
themes = ['superman', 'hulk', 'dark-vader', 'homem-ferro', 'halloween', 'natal', 'matrix', 'original']

print("💾 Criando backups...")
for theme in themes:
    theme_file = f"static/css/themes/{theme}.css"
    backup_file = f"static/css/themes/{theme}-backup-original.css"
    
    if os.path.exists(theme_file):
        shutil.copy(theme_file, backup_file)
        print(f"   ✅ Backup: {theme}-backup-original.css")

# Ler o CSS do Batman como template
print("\n📖 Lendo template Batman...")
with open("static/css/themes/batman.css", 'r', encoding='utf-8') as f:
    batman_css = f.read()

print("✅ Template Batman carregado!")

# Configurações específicas de cada tema
theme_configs = {
    'superman': {
        'name': 'SUPERMAN 🔵⭐ - O Homem de Aço',
        'colors': {
            'primary': '#ffd700',  # Dourado
            'secondary': '#dc143c',  # Vermelho
            'bg_primary': '#0c2e5a',  # Azul escuro
            'bg_secondary': '#1e4d73',  # Azul médio
            'text': '#ffd700'
        }
    },
    'hulk': {
        'name': 'HULK 💚💪 - O Gigante Verde',
        'colors': {
            'primary': '#32cd32',  # Verde lime
            'secondary': '#800080',  # Roxo
            'bg_primary': '#0d2818',  # Verde muito escuro
            'bg_secondary': '#228b22',  # Verde escuro
            'text': '#32cd32'
        }
    },
    'dark-vader': {
        'name': 'DARK VADER 🖤⚔️ - O Lado Sombrio',
        'colors': {
            'primary': '#ff0000',  # Vermelho
            'secondary': '#8b0000',  # Vermelho escuro
            'bg_primary': '#000000',  # Preto
            'bg_secondary': '#1a0000',  # Preto avermelhado
            'text': '#ff4444'
        }
    },
    'homem-ferro': {
        'name': 'HOMEM DE FERRO ❤️🤖 - Tony Stark',
        'colors': {
            'primary': '#ffd700',  # Dourado
            'secondary': '#8b0000',  # Vermelho escuro
            'bg_primary': '#1a0f0f',  # Marrom escuro
            'bg_secondary': '#8b0000',  # Vermelho escuro
            'text': '#ffd700'
        }
    },
    'halloween': {
        'name': 'HALLOWEEN 🎃👻 - Noite Assombrada',
        'colors': {
            'primary': '#ff6600',  # Laranja
            'secondary': '#800080',  # Roxo
            'bg_primary': '#000000',  # Preto
            'bg_secondary': '#4a0e4e',  # Roxo escuro
            'text': '#ff6600'
        }
    },
    'natal': {
        'name': 'NATAL 🎄❄️ - Magia Natalina',
        'colors': {
            'primary': '#ff0000',  # Vermelho
            'secondary': '#00ff00',  # Verde
            'bg_primary': '#0f2027',  # Azul escuro
            'bg_secondary': '#203a43',  # Azul acinzentado
            'text': '#ffffff'
        }
    },
    'matrix': {
        'name': 'MATRIX 💊🔢 - Código Digital',
        'colors': {
            'primary': '#00ff00',  # Verde neon
            'secondary': '#003300',  # Verde escuro
            'bg_primary': '#000000',  # Preto
            'bg_secondary': '#001100',  # Verde muito escuro
            'text': '#00ff00'
        }
    },
    'original': {
        'name': 'ORIGINAL 🎨✨ - Design Clássico',
        'colors': {
            'primary': '#667eea',  # Roxo claro
            'secondary': '#764ba2',  # Roxo escuro
            'bg_primary': '#667eea',  # Roxo claro
            'bg_secondary': '#764ba2',  # Roxo escuro
            'text': '#333333'
        }
    }
}

print("\n🎨 Aplicando layout correto a todos os temas...")

for theme_name, config in theme_configs.items():
    print(f"\n🔄 Processando {theme_name}...")
    
    # Substituir configurações no template do Batman
    new_css = batman_css
    
    # Substituir o título do tema
    new_css = new_css.replace('/* TEMA BATMAN', f'/* TEMA {config["name"]}')
    
    # Substituir cores principais (Batman usa #ffd700 para dourado)
    colors = config['colors']
    
    # Substituir gradientes de fundo
    if theme_name == 'superman':
        new_css = new_css.replace(
            'linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 25%, #2a2a1a 50%, #1a1a1a 75%, #0a0a0a 100%)',
            f'linear-gradient(135deg, {colors["bg_primary"]} 0%, {colors["bg_secondary"]} 25%, {colors["secondary"]} 50%, {colors["bg_secondary"]} 75%, {colors["bg_primary"]} 100%)'
        )
    elif theme_name == 'hulk':
        new_css = new_css.replace(
            'linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 25%, #2a2a1a 50%, #1a1a1a 75%, #0a0a0a 100%)',
            f'linear-gradient(135deg, {colors["bg_primary"]} 0%, {colors["bg_secondary"]} 25%, {colors["primary"]} 50%, {colors["bg_secondary"]} 75%, {colors["bg_primary"]} 100%)'
        )
    else:
        new_css = new_css.replace(
            'linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 25%, #2a2a1a 50%, #1a1a1a 75%, #0a0a0a 100%)',
            f'linear-gradient(135deg, {colors["bg_primary"]} 0%, {colors["bg_secondary"]} 25%, {colors["primary"]} 50%, {colors["bg_secondary"]} 75%, {colors["bg_primary"]} 100%)'
        )
    
    # Substituir cor primária (#ffd700 do Batman)
    new_css = new_css.replace('#ffd700', colors['primary'])
    
    # Substituir cores de background dos cards (simplificado)
    if theme_name == 'original':
        # Tema original usa fundo branco
        new_css = new_css.replace('rgba(10, 10, 10, 0.95)', 'rgba(255, 255, 255, 0.95)')
        new_css = new_css.replace('color: #fff;', 'color: #333;')
    else:
        # Outros temas mantêm fundo escuro mas com nuance da cor do tema
        new_css = new_css.replace('rgba(10, 10, 10, 0.95)', 'rgba(15, 15, 25, 0.95)')
    
    # Salvar o arquivo
    output_file = f"static/css/themes/{theme_name}.css"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_css)
    
    print(f"   ✅ {theme_name}.css atualizado!")

print(f"\n🎉 Todos os temas foram atualizados com o layout correto!")
print("📋 Layout aplicado:")
print("   ✅ Grid de duas colunas (1fr 1fr)")
print("   ✅ Cards com altura mínima de 450px") 
print("   ✅ Gap de 30px entre colunas")
print("   ✅ Responsivo para mobile")
print("   ✅ Animações preservadas")

print(f"\n💾 Backups salvos com sufixo '-backup-original.css'")
print("🔄 Reinicie o servidor para ver as mudanças!")
