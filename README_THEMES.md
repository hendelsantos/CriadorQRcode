# 🎨 Sistema de Temas - QR Code Generator

## 📋 Comandos de Administração

### Ver todos os temas:
```bash
python admin_themes.py list
```

### Ver tema atual:
```bash
python admin_themes.py current
```

### Trocar tema:
```bash
python admin_themes.py change nome_do_tema
```

### Adicionar novo tema:
```bash
python admin_themes.py add id_tema "Nome do Tema" "caminho/arquivo.css" "🎨" "Descrição opcional"
```

## 🗓️ Ideias de Temas por Época do Ano

### 🎃 Outubro - Halloween
- **Cores**: Laranja, preto, marrom
- **Tema**: `halloween`
- **Comando**: `python admin_themes.py change halloween`

### 🎄 Dezembro - Natal
- **Cores**: Verde, vermelho, dourado
- **Tema**: `natal`
- **Comando**: `python admin_themes.py change natal`

### 💝 Fevereiro - Dia dos Namorados
- **Cores**: Rosa, vermelho, dourado
- **Sugestão**: Criar tema romântico

### 🌸 Primavera/Setembro
- **Cores**: Verde claro, rosa, amarelo
- **Sugestão**: Tema floral

### ☀️ Verão/Janeiro
- **Cores**: Azul, amarelo, laranja
- **Sugestão**: Tema praia/sol

### 🍂 Outono/Março-Maio
- **Cores**: Marrom, laranja, amarelo
- **Sugestão**: Tema folhas secas

## 🤓 Temas Nerds Disponíveis

### 🔴 Matrix Hacker
- **Cores**: Verde neon, preto
- **Tema**: `matrix`
- **Comando**: `python admin_themes.py change matrix`

### 🌑 Dark Vader (Star Wars)
- **Cores**: Preto, dourado
- **Tema**: `dark-vader`
- **Comando**: `python admin_themes.py change dark-vader`

## 🎮 Ideias para Futuros Temas Nerds

### 🦸‍♂️ Super Heróis
- **Batman**: Preto, amarelo, azul escuro
- **Homem de Ferro**: Vermelho, dourado
- **Hulk**: Verde, roxo

### 🎮 Games
- **Retro Arcade**: Neon, pixels
- **Minecraft**: Verde, marrom, azul
- **Cyberpunk**: Rosa neon, azul elétrico

### 📺 Séries/Filmes
- **Breaking Bad**: Verde químico, amarelo
- **Stranger Things**: Vermelho, preto, neon
- **Game of Thrones**: Dourado, vermelho, preto

## 🔧 Como Criar um Novo Tema

1. **Copie um tema existente:**
   ```bash
   cp static/css/themes/dark-vader.css static/css/themes/meu-tema.css
   ```

2. **Edite as cores no arquivo CSS**

3. **Adicione o tema:**
   ```bash
   python admin_themes.py add meu-tema "Meu Tema" "themes/meu-tema.css" "🎨" "Descrição do tema"
   ```

4. **Ative o tema:**
   ```bash
   python admin_themes.py change meu-tema
   ```

5. **Reinicie o servidor Flask para aplicar**

## 📁 Estrutura de Arquivos

```
static/css/
├── style-original.css          # Tema roxo original
└── themes/
    ├── dark-vader.css         # Tema Dark Vader
    ├── halloween.css          # Tema Halloween
    ├── natal.css             # Tema Natal
    └── matrix.css            # Tema Matrix
```

## 🎯 Dicas para Temas Sazonais

- **Janeiro**: Ano novo (dourado, branco)
- **Março/Abril**: Páscoa (pastel, coelho)
- **Junho**: Festa Junina (laranja, vermelho)
- **Julho**: Férias (azul, amarelo)
- **Setembro**: Primavera (verde, rosa)
- **Outubro**: Halloween (laranja, preto)
- **Dezembro**: Natal (verde, vermelho)

## 🚀 Automação Futura

Você pode criar um script para trocar temas automaticamente por data:

```python
import datetime

def auto_theme():
    month = datetime.now().month
    if month == 10:
        return "halloween"
    elif month == 12:
        return "natal"
    # ... outros meses
    else:
        return "dark-vader"
```

---

**💡 Lembre-se**: Após trocar o tema, sempre reinicie o servidor Flask para aplicar as mudanças!
