#!/bin/bash

# Script para alterar tema e fazer deploy automático
# Uso: ./deploy_theme.sh nome-do-tema

THEME=$1

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${BLUE}🎨 QR Code Generator - Deploy de Tema${NC}"
echo -e "${BLUE}======================================${NC}"

if [ -z "$THEME" ]; then
    echo -e "${RED}❌ Erro: Especifique um tema!${NC}"
    echo -e "${YELLOW}💡 Uso: ./deploy_theme.sh nome-do-tema${NC}"
    echo -e "${CYAN}📋 Temas disponíveis:${NC}"
    python admin_themes.py list
    exit 1
fi

echo -e "${PURPLE}🎯 Alterando tema para: $THEME${NC}"

# 1. Alterar tema
python admin_themes.py change $THEME

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Erro ao alterar tema!${NC}"
    exit 1
fi

# 2. Verificar se quer testar localmente
echo -e "${YELLOW}🧪 Deseja testar localmente antes do deploy? (s/N):${NC}"
read -r test_local

if [[ $test_local =~ ^[Ss]$ ]]; then
    echo -e "${CYAN}🌐 Iniciando servidor local...${NC}"
    echo -e "${CYAN}📍 URL: http://localhost:5000${NC}"
    echo -e "${YELLOW}⏸️  Pressione Ctrl+C para parar e continuar com deploy${NC}"
    
    # Ativar ambiente virtual e rodar servidor
    source .venv/bin/activate && python app.py
fi

# 3. Deploy para produção
echo -e "${PURPLE}🚀 Fazendo deploy para Railway...${NC}"

# Verificar se há mudanças para commit
if git diff-index --quiet HEAD --; then
    echo -e "${YELLOW}⚠️  Nenhuma mudança detectada, forçando redeploy...${NC}"
    git commit --allow-empty -m "chore: força redeploy tema $THEME"
else
    git add .
    git commit -m "feat: alterado tema para $THEME 🎨"
fi

echo -e "${CYAN}📤 Enviando para GitHub...${NC}"
git push origin main

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Deploy enviado com sucesso!${NC}"
    echo -e "${CYAN}🌐 Railway URL: https://criarqrcode-production.up.railway.app${NC}"
    echo -e "${YELLOW}⏳ Aguarde ~2-3 minutos para aplicar as mudanças${NC}"
    echo -e "${PURPLE}📊 Monitorar deploy: railway logs${NC}"
else
    echo -e "${RED}❌ Erro no push para GitHub!${NC}"
    exit 1
fi

echo -e "${GREEN}🎉 Processo concluído!${NC}"
