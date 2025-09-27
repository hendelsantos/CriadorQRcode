#!/bin/bash

# 🎨 SELETOR RÁPIDO DE TEMAS QR CODE
# ===================================

# Cores para o terminal
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# Limpar tela
clear

# Cabeçalho
echo -e "${CYAN}🎨========================================🎨${NC}"
echo -e "${WHITE}      SELETOR RÁPIDO DE TEMAS QR CODE    ${NC}"
echo -e "${CYAN}🎨========================================🎨${NC}"
echo ""

# Verificar se estamos no diretório correto
if [ ! -f "themes_config.json" ]; then
    echo -e "${RED}❌ Arquivo themes_config.json não encontrado!${NC}"
    echo -e "${YELLOW}💡 Certifique-se de estar no diretório do projeto.${NC}"
    exit 1
fi

# Verificar se Python está disponível
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 não encontrado!${NC}"
    exit 1
fi

# Menu de temas
echo -e "${BLUE}🎯 TEMAS DISPONÍVEIS:${NC}"
echo "─────────────────────────────────────"
echo -e "${WHITE} 1.${NC} 🦇 Batman          - O Cavaleiro das Trevas"
echo -e "${WHITE} 2.${NC} 🔵 Superman        - O Homem de Aço"  
echo -e "${WHITE} 3.${NC} 💚 Hulk            - O Gigante Verde"
echo -e "${WHITE} 4.${NC} 🖤 Dark Vader      - O Lado Sombrio da Força"
echo -e "${WHITE} 5.${NC} ❤️ Homem de Ferro   - Tecnologia Stark"
echo -e "${WHITE} 6.${NC} 🎃 Halloween       - Noite Assombrada"
echo -e "${WHITE} 7.${NC} 🎄 Natal           - Magia Natalina"
echo -e "${WHITE} 8.${NC} 💊 Matrix          - Código Digital"
echo -e "${WHITE} 9.${NC} 🎨 Original        - Design Clássico"
echo ""
echo -e "${WHITE}10.${NC} 📋 Ver tema atual"
echo -e "${WHITE}11.${NC} 🔄 Iniciar servidor"
echo -e "${WHITE} 0.${NC} ❌ Sair"

echo "─────────────────────────────────────"
echo -e -n "${CYAN}🎯 Escolha uma opção (0-11): ${NC}"
read choice

case $choice in
    1)
        echo -e "${YELLOW}🔄 Aplicando tema Batman...${NC}"
        python3 admin_themes.py change batman
        ;;
    2)
        echo -e "${YELLOW}🔄 Aplicando tema Superman...${NC}"
        python3 admin_themes.py change superman
        ;;
    3)
        echo -e "${YELLOW}🔄 Aplicando tema Hulk...${NC}"
        python3 admin_themes.py change hulk
        ;;
    4)
        echo -e "${YELLOW}🔄 Aplicando tema Dark Vader...${NC}"
        python3 admin_themes.py change dark-vader
        ;;
    5)
        echo -e "${YELLOW}🔄 Aplicando tema Homem de Ferro...${NC}"
        python3 admin_themes.py change homem-ferro
        ;;
    6)
        echo -e "${YELLOW}🔄 Aplicando tema Halloween...${NC}"
        python3 admin_themes.py change halloween
        ;;
    7)
        echo -e "${YELLOW}🔄 Aplicando tema Natal...${NC}"
        python3 admin_themes.py change natal
        ;;
    8)
        echo -e "${YELLOW}🔄 Aplicando tema Matrix...${NC}"
        python3 admin_themes.py change matrix
        ;;
    9)
        echo -e "${YELLOW}🔄 Aplicando tema Original...${NC}"
        python3 admin_themes.py change original
        ;;
    10)
        echo -e "${BLUE}📋 Tema atual:${NC}"
        python3 admin_themes.py current
        ;;
    11)
        echo -e "${GREEN}🚀 Iniciando servidor Flask...${NC}"
        echo -e "${YELLOW}💡 Acesse: http://localhost:5000${NC}"
        echo ""
        # Verificar se existe ambiente virtual
        if [ -f ".venv/bin/python" ]; then
            .venv/bin/python app.py
        else
            python3 app.py
        fi
        ;;
    0)
        echo -e "${GREEN}👋 Até logo!${NC}"
        exit 0
        ;;
    *)
        echo -e "${RED}❌ Opção inválida! Escolha um número de 0 a 11.${NC}"
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}✅ Operação concluída!${NC}"

# Se foi mudança de tema, perguntar se quer iniciar servidor
if [ $choice -ge 1 ] && [ $choice -le 9 ]; then
    echo ""
    echo -e -n "${CYAN}🚀 Deseja iniciar o servidor agora? (s/N): ${NC}"
    read start_server
    
    if [[ $start_server =~ ^[Ss]$ ]]; then
        echo -e "${GREEN}🚀 Iniciando servidor Flask...${NC}"
        echo -e "${YELLOW}💡 Acesse: http://localhost:5000${NC}"
        echo ""
        
        # Verificar se existe ambiente virtual
        if [ -f ".venv/bin/python" ]; then
            .venv/bin/python app.py
        else
            python3 app.py
        fi
    fi
fi
