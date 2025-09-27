#!/usr/bin/env python3
"""
🎨 SELETOR INTERATIVO DE TEMAS QR CODE
=====================================
Script para selecionar e aplicar temas de forma visual e interativa.
"""

import json
import os
import sys
from typing import Dict, Any

def load_themes_config() -> Dict[str, Any]:
    """Carrega a configuração dos temas."""
    config_path = "themes_config.json"
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Arquivo themes_config.json não encontrado!")
        sys.exit(1)
    except json.JSONDecodeError:
        print("❌ Erro ao decodificar themes_config.json!")
        sys.exit(1)

def save_themes_config(config: Dict[str, Any]) -> None:
    """Salva a configuração dos temas."""
    config_path = "themes_config.json"
    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print("✅ Configuração salva com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao salvar configuração: {e}")
        sys.exit(1)

def clear_screen():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header():
    """Exibe o cabeçalho do aplicativo."""
    print("🎨" + "=" * 60 + "🎨")
    print("           SELETOR INTERATIVO DE TEMAS QR CODE")
    print("🎨" + "=" * 60 + "🎨")
    print()

def show_themes_menu(config: Dict[str, Any]) -> None:
    """Exibe o menu de temas disponíveis."""
    current_theme = config.get("current_theme", "")
    available_themes = config.get("available_themes", {})
    
    print("🎯 TEMAS DISPONÍVEIS:")
    print("─" * 50)
    
    theme_list = []
    for i, (theme_id, theme_data) in enumerate(available_themes.items(), 1):
        icon = theme_data.get("icon", "🎨")
        name = theme_data.get("name", theme_id)
        description = theme_data.get("description", "")
        
        # Marcar o tema atual
        status = "🔥 ATIVO" if theme_id == current_theme else f" {i:2d}."
        
        print(f"{status} {icon} {name}")
        print(f"    📝 {description}")
        print()
        
        theme_list.append((theme_id, theme_data))
    
    return theme_list

def get_user_choice(max_options: int) -> int:
    """Obtém a escolha do usuário."""
    print("─" * 50)
    print("💡 OPÇÕES:")
    print("   • Digite o número do tema (1-{})".format(max_options))
    print("   • Digite 'q' para sair")
    print("   • Digite 'r' para atualizar a lista")
    print()
    
    while True:
        choice = input("🎯 Sua escolha: ").strip().lower()
        
        if choice == 'q':
            print("\n👋 Até logo!")
            sys.exit(0)
        elif choice == 'r':
            return 0  # Código especial para refresh
        else:
            try:
                num = int(choice)
                if 1 <= num <= max_options:
                    return num
                else:
                    print(f"❌ Por favor, digite um número entre 1 e {max_options}")
            except ValueError:
                print("❌ Entrada inválida! Digite um número, 'q' ou 'r'")

def apply_theme(theme_id: str, theme_data: Dict[str, Any], config: Dict[str, Any]) -> None:
    """Aplica o tema selecionado."""
    print(f"\n🔄 Aplicando tema: {theme_data.get('icon', '🎨')} {theme_data.get('name', theme_id)}")
    
    # Verificar se o arquivo CSS existe
    css_file = theme_data.get('css_file', '')
    if css_file.startswith('themes/'):
        css_path = os.path.join('static', 'css', css_file)
    else:
        css_path = os.path.join('static', 'css', css_file)
    
    if not os.path.exists(css_path):
        print(f"❌ Arquivo CSS não encontrado: {css_path}")
        input("\n⏎ Pressione Enter para continuar...")
        return
    
    # Atualizar configuração
    config["current_theme"] = theme_id
    save_themes_config(config)
    
    print(f"✅ Tema '{theme_data.get('name', theme_id)}' aplicado com sucesso!")
    print(f"📁 Arquivo: {css_path}")
    
    # Mostrar instruções para reiniciar o servidor
    print("\n🔄 PRÓXIMOS PASSOS:")
    print("   1. Reinicie o servidor Flask para aplicar as mudanças:")
    print("      python app.py")
    print("   2. Ou execute o servidor com ambiente virtual:")
    print("      .venv/bin/python app.py")
    print()
    
    input("⏎ Pressione Enter para continuar...")

def show_current_theme_info(config: Dict[str, Any]) -> None:
    """Exibe informações sobre o tema atual."""
    current_theme = config.get("current_theme", "")
    available_themes = config.get("available_themes", {})
    
    if current_theme and current_theme in available_themes:
        theme_data = available_themes[current_theme]
        icon = theme_data.get("icon", "🎨")
        name = theme_data.get("name", current_theme)
        description = theme_data.get("description", "")
        css_file = theme_data.get("css_file", "")
        
        print(f"🔥 TEMA ATUAL: {icon} {name}")
        print(f"📝 {description}")
        print(f"📁 {css_file}")
        print()

def main():
    """Função principal do aplicativo."""
    while True:
        try:
            # Limpar tela e mostrar cabeçalho
            clear_screen()
            show_header()
            
            # Carregar configuração
            config = load_themes_config()
            
            # Mostrar tema atual
            show_current_theme_info(config)
            
            # Mostrar menu de temas
            theme_list = show_themes_menu(config)
            
            if not theme_list:
                print("❌ Nenhum tema encontrado!")
                break
            
            # Obter escolha do usuário
            choice = get_user_choice(len(theme_list))
            
            if choice == 0:  # Refresh
                continue
            
            # Aplicar tema escolhido
            theme_id, theme_data = theme_list[choice - 1]
            
            # Verificar se já é o tema atual
            if theme_id == config.get("current_theme", ""):
                print(f"\n💡 O tema '{theme_data.get('name', theme_id)}' já está ativo!")
                input("\n⏎ Pressione Enter para continuar...")
                continue
            
            apply_theme(theme_id, theme_data, config)
            
        except KeyboardInterrupt:
            print("\n\n👋 Saída solicitada pelo usuário. Até logo!")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            input("\n⏎ Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
