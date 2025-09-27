#!/bin/bash

# 🧪 TESTE RÁPIDO DE TODOS OS TEMAS
# =================================

echo "🧪 TESTANDO TODOS OS TEMAS CORRIGIDOS"
echo "====================================="

# Lista de temas para testar
themes=("batman" "superman" "hulk" "dark-vader" "homem-ferro" "halloween" "natal" "matrix" "original")

# Servidor já deve estar rodando
echo "💡 Certifique-se de que o servidor está rodando em http://localhost:5000"
echo ""

for i in "${!themes[@]}"; do
    theme=${themes[$i]}
    number=$((i + 1))
    
    echo "🎨 Testando tema $number: ${theme}"
    
    # Aplicar tema
    python3 admin_themes.py change "$theme" > /dev/null 2>&1
    
    if [ $? -eq 0 ]; then
        echo "   ✅ Tema $theme aplicado com sucesso!"
        echo "   🌐 Acesse: http://localhost:5000 para visualizar"
        echo "   ⏱️  Aguardando 3 segundos..."
        sleep 3
    else
        echo "   ❌ Erro ao aplicar tema $theme"
    fi
    
    echo ""
done

echo "🎉 Teste de todos os temas concluído!"
echo "💡 Todos os temas devem estar com layout de duas colunas e cards de 450px de altura."
