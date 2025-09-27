#!/usr/bin/env python3
"""
Script de administração para gerenciar temas do QR Code Generator
Uso: python admin_themes.py [comando] [argumentos]

Comandos disponíveis:
- list: Lista todos os temas disponíveis
- current: Mostra o tema atual
- change <nome_tema>: Troca para o tema especificado
- add <nome_tema> <nome_exibicao> <arquivo_css> <icone> [descricao]: Adiciona novo tema
"""

import json
import sys
import os

def load_theme_config():
    """Carrega configuração dos temas"""
    try:
        with open('themes_config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Arquivo themes_config.json não encontrado!")
        sys.exit(1)
    except json.JSONDecodeError:
        print("❌ Erro ao ler themes_config.json - arquivo mal formatado!")
        sys.exit(1)

def save_theme_config(config):
    """Salva configuração dos temas"""
    try:
        with open('themes_config.json', 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print("✅ Configuração salva com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao salvar configuração: {e}")
        sys.exit(1)

def list_themes():
    """Lista todos os temas disponíveis"""
    config = load_theme_config()
    current = config.get('current_theme', 'N/A')
    themes = config.get('available_themes', {})
    
    print("\n🎨 TEMAS DISPONÍVEIS:")
    print("=" * 50)
    
    for theme_id, theme_info in themes.items():
        status = "🔥 ATIVO" if theme_id == current else "   "
        print(f"{status} {theme_info['icon']} {theme_info['name']} ({theme_id})")
        print(f"       📁 {theme_info['css_file']}")
        print(f"       📝 {theme_info.get('description', 'Sem descrição')}")
        print()

def show_current():
    """Mostra o tema atual"""
    config = load_theme_config()
    current = config.get('current_theme')
    themes = config.get('available_themes', {})
    
    if current and current in themes:
        theme_info = themes[current]
        print(f"\n🔥 TEMA ATUAL: {theme_info['icon']} {theme_info['name']}")
        print(f"📁 Arquivo CSS: {theme_info['css_file']}")
        print(f"📝 Descrição: {theme_info.get('description', 'Sem descrição')}")
    else:
        print("\n❌ Nenhum tema ativo ou tema inválido!")

def change_theme(theme_name):
    """Troca para o tema especificado"""
    config = load_theme_config()
    themes = config.get('available_themes', {})
    
    if theme_name not in themes:
        print(f"\n❌ Tema '{theme_name}' não encontrado!")
        print("\n📋 Temas disponíveis:")
        for tid in themes.keys():
            print(f"   - {tid}")
        return
    
    config['current_theme'] = theme_name
    save_theme_config(config)
    
    theme_info = themes[theme_name]
    print(f"\n🎉 Tema alterado para: {theme_info['icon']} {theme_info['name']}")
    print("🔄 Reinicie o servidor Flask para aplicar as mudanças!")

def add_theme(args):
    """Adiciona um novo tema"""
    if len(args) < 4:
        print("\n❌ Argumentos insuficientes!")
        print("💡 Uso: python admin_themes.py add <nome_tema> <nome_exibicao> <arquivo_css> <icone> [descricao]")
        return
    
    theme_id = args[0]
    theme_name = args[1]
    css_file = args[2]
    icon = args[3]
    description = args[4] if len(args) > 4 else f"Tema {theme_name}"
    
    config = load_theme_config()
    themes = config.get('available_themes', {})
    
    if theme_id in themes:
        print(f"\n⚠️  Tema '{theme_id}' já existe! Deseja sobrescrever? (s/N): ", end="")
        if input().lower() != 's':
            print("❌ Operação cancelada!")
            return
    
    # Verifica se o arquivo CSS existe
    css_path = f"static/css/{css_file}"
    if not os.path.exists(css_path):
        print(f"\n❌ Arquivo CSS não encontrado: {css_path}")
        print("💡 Certifique-se de criar o arquivo CSS antes de adicionar o tema!")
        return
    
    themes[theme_id] = {
        "name": theme_name,
        "description": description,
        "css_file": css_file,
        "icon": icon
    }
    
    config['available_themes'] = themes
    save_theme_config(config)
    
    print(f"\n✅ Tema '{theme_name}' adicionado com sucesso!")
    print(f"🎨 ID: {theme_id}")
    print(f"📁 CSS: {css_file}")
    print(f"🎯 Para ativar: python admin_themes.py change {theme_id}")

def main():
    """Função principal"""
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    command = sys.argv[1].lower()
    
    if command == 'list':
        list_themes()
    elif command == 'current':
        show_current()
    elif command == 'change':
        if len(sys.argv) < 3:
            print("❌ Especifique o nome do tema!")
            print("💡 Uso: python admin_themes.py change <nome_tema>")
            return
        change_theme(sys.argv[2])
    elif command == 'add':
        add_theme(sys.argv[2:])
    else:
        print(f"❌ Comando desconhecido: {command}")
        print(__doc__)

if __name__ == "__main__":
    main()
