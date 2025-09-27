# 🎨 SCRIPTS DE SELEÇÃO DE TEMAS

Foram criados **2 scripts** para facilitar a seleção e aplicação de temas no seu sistema QR Code:

## 🚀 OPÇÕES DISPONÍVEIS

### 1. **Script Bash Rápido** (`tema.sh`)
```bash
./tema.sh
```
- ✅ **Interface simples e colorida**
- ✅ **Menu numerado de 1-9** para os temas
- ✅ **Opção para ver tema atual**
- ✅ **Inicia servidor automaticamente** após mudança
- ✅ **Funciona sem Python** (usa admin_themes.py internamente)

### 2. **Script Python Interativo** (`selecionar_tema.py`)
```bash
python selecionar_tema.py
# ou
.venv/bin/python selecionar_tema.py
```
- ✅ **Interface rica e elegante**
- ✅ **Mostra tema atual** em destaque
- ✅ **Descrições completas** de cada tema
- ✅ **Verificação de arquivos CSS**
- ✅ **Opções: números, 'q' para sair, 'r' para refresh**
- ✅ **Tratamento completo de erros**

## 🎯 TEMAS DISPONÍVEIS

| Nº | Tema | Ícone | Descrição |
|---|---|---|---|
| 1 | Batman | 🦇 | O Cavaleiro das Trevas |
| 2 | Superman | 🔵 | O Homem de Aço |
| 3 | Hulk | 💚 | O Gigante Verde |
| 4 | Dark Vader | 🖤 | O Lado Sombrio da Força |
| 5 | Homem de Ferro | ❤️ | Tecnologia Stark |
| 6 | Halloween | 🎃 | Noite Assombrada |
| 7 | Natal | 🎄 | Magia Natalina |
| 8 | Matrix | 💊 | Código Digital |
| 9 | Original | 🎨 | Design Clássico |

## 🔧 COMO USAR

### Script Bash (`tema.sh`):
```bash
# Executar script
./tema.sh

# Escolher tema (1-9)
🎯 Escolha uma opção (0-11): 2

# Aceitar iniciar servidor
🚀 Deseja iniciar o servidor agora? (s/N): s
```

### Script Python (`selecionar_tema.py`):
```bash
# Executar script
python selecionar_tema.py

# Navegar no menu
🎯 Sua escolha: 3
# ou
🎯 Sua escolha: q  # para sair
# ou
🎯 Sua escolha: r  # para refresh
```

## 💡 RECURSOS ESPECIAIS

### Script Bash:
- **Opção 10**: Ver tema atual
- **Opção 11**: Iniciar servidor diretamente
- **Opção 0**: Sair
- **Auto-detecção**: Usa ambiente virtual se disponível

### Script Python:
- **Tema atual destacado**: Mostra qual está ativo
- **Verificação de arquivos**: Confirma se CSS existe
- **Instruções claras**: Mostra como reiniciar servidor
- **Interface limpa**: Limpa tela a cada operação

## 🎨 EXEMPLOS DE USO

### Mudança Rápida (Bash):
```bash
./tema.sh
# Escolher: 1 (Batman)
# Responder: s (iniciar servidor)
# Resultado: Tema aplicado + servidor rodando
```

### Exploração Interativa (Python):
```bash
python selecionar_tema.py
# Ver tema atual
# Explorar opções
# Aplicar tema
# Pressionar Enter para continuar
# Escolher outro tema
# Digite 'q' para sair
```

## 🔄 FLUXO COMPLETO

1. **Executar script** de sua preferência
2. **Ver tema atual** (se necessário)
3. **Escolher novo tema** (1-9)
4. **Confirmar aplicação** ✅
5. **Iniciar servidor** (opcional no bash)
6. **Acessar** `http://localhost:5000`
7. **Verificar** mudança visual aplicada

## 📋 COMPARAÇÃO DOS SCRIPTS

| Recurso | Bash Script | Python Script |
|---------|-------------|---------------|
| Velocidade | ⚡ Muito rápido | 🐌 Mais lento |
| Interface | 🎨 Simples e colorida | 💎 Rica e elegante |
| Automação | 🚀 Inicia servidor auto | 📋 Instruções manuais |
| Recursos | 🔧 Básico funcional | 🛠️ Completo avançado |
| Dependências | 📦 Só bash | 🐍 Python + libraries |
| Uso recomendado | ⚡ Mudanças rápidas | 🔍 Exploração detalhada |

## ✨ DICA FINAL

- **Para uso diário**: Use `./tema.sh` (mais rápido)
- **Para explorar temas**: Use `python selecionar_tema.py` (mais detalhado)
- **Ambos são funcionais** e complementares!

---
**Status**: ✅ Ambos os scripts testados e funcionando perfeitamente!
