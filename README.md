# 🎨 Gerador de QR Code com Sistema de Temas

[![GitHub](https://img.shields.io/github/license/hendelsantos/CriadorQRcode)](https://github.com/hendelsantos/CriadorQRcode/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/hendelsantos/CriadorQRcode)](https://github.com/hendelsantos/CriadorQRcode/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/hendelsantos/CriadorQRcode)](https://github.com/hendelsantos/CriadorQRcode/network)

Um gerador de QR Code moderno e elegante com **9 temas únicos** inspirados em super-heróis e ocasiões especiais. Interface responsiva com layout de duas colunas e sistema completo de gerenciamento de temas.

![Preview do Projeto](https://via.placeholder.com/800x400/0a0a0a/ffd700?text=QR+Code+Generator+com+Temas)

## ✨ Características

- 🎨 **9 Temas Únicos**: Batman, Superman, Hulk, Dark Vader, Homem de Ferro, Halloween, Natal, Matrix, Original
- 📱 **Design Responsivo**: Layout adaptável para desktop e mobile
- ⚡ **Troca Rápida de Temas**: Scripts interativos para mudança instantânea
- 🎯 **Interface Moderna**: Layout de duas colunas com cards elegantes
- 🚀 **Deploy Simples**: Suporte Docker e Railway
- 📋 **Múltiplos Formatos**: WhatsApp, URLs, texto personalizado
- **Download**: Baixe os QR codes como PNG
- **Copiar**: Copie a imagem para área de transferência
- **Compartilhar**: Compartilhe facilmente com outros
- **SEO otimizado**: Meta tags para melhor indexação

## 🎭 Temas Disponíveis

| Tema | Descrição | Cores Principais |
|------|-----------|------------------|
| 🦇 **Batman** | O Cavaleiro das Trevas | Preto, Cinza, Dourado |
| 🔵 **Superman** | O Homem de Aço | Azul, Vermelho, Dourado |
| 💚 **Hulk** | O Gigante Verde | Verde, Roxo |
| 🖤 **Dark Vader** | O Lado Sombrio da Força | Preto, Vermelho |
| ❤️ **Homem de Ferro** | Tecnologia Stark | Vermelho, Dourado |
| 🎃 **Halloween** | Noite Assombrada | Laranja, Roxo |
| 🎄 **Natal** | Magia Natalina | Vermelho, Verde |
| 💊 **Matrix** | Código Digital | Verde Neon |
| 🎨 **Original** | Design Clássico | Roxo, Moderno |

## 🚀 Instalação Rápida

### Método 1: Local com Python

```bash
# Clone o repositório
git clone https://github.com/hendelsantos/CriadorQRcode.git
cd CriadorQRcode

# Crie um ambiente virtual (recomendado)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Instale dependências
pip install -r requirements.txt

# Execute o aplicativo
python app.py
```

### Método 2: Docker

```bash
# Clone o repositório
git clone https://github.com/hendelsantos/CriadorQRcode.git
cd CriadorQRcode

# Build e execute
docker build -t qrcode-generator .
docker run -p 5000:5000 qrcode-generator
```

### Método 3: Railway (Deploy em Nuvem)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app)

## 🎮 Como Usar os Temas

### Troca de Temas Rápida

**Script Bash (Recomendado):**
```bash
chmod +x tema.sh
./tema.sh
# Escolha 1-9 para qualquer tema
```

**Script Python Interativo:**
```bash
python selecionar_tema.py
# Interface rica com detalhes de cada tema
```

**Comando Direto:**
```bash
python admin_themes.py change batman
python admin_themes.py change superman
python admin_themes.py change hulk
# ... e assim por diante
```

### Gerenciamento de Temas

```bash
# Ver tema atual
python admin_themes.py current

# Listar todos os temas
python admin_themes.py list

# Mudar tema
python admin_themes.py change [nome-do-tema]
```

## 🎯 Como Usar o Gerador

1. **Acesse** o aplicativo no seu navegador em `http://localhost:5000`
2. **Escolha o tema** usando um dos scripts de tema
3. **Selecione** o tipo de QR code que deseja gerar:
   - 📱 WhatsApp: Digite o número com DDD
   - 🔗 URL/Link: Cole qualquer link  
   - 📝 Texto: Digite qualquer texto
4. **Clique** em "Gerar QR Code"
5. **Baixe**, **copie** ou **compartilhe** seu QR code

## 📱 Exemplos de Uso

### WhatsApp
- Digite: `11999887766`
- Resultado: QR code que abre conversa no WhatsApp

### URL
- Digite: `www.github.com` ou `https://www.github.com`
- Resultado: QR code que abre o site

### Texto
- Digite: `Olá! Este é meu cartão de visitas digital`
- Resultado: QR code com o texto personalizado

## 🔧 Recursos Técnicos

- **Framework**: Flask (Python 3.7+)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **QR Code**: Biblioteca qrcode com PIL
- **Layout**: CSS Grid responsivo de duas colunas
- **Temas**: Sistema dinâmico de troca de temas
- **Ícones**: Favicons múltiplos tamanhos
- **PWA**: Web App Manifest incluído
- **SEO**: Meta tags otimizadas
- **Validações**: Validação de telefone e URL
- **Formatação**: Formatação automática de números

## 📱 Responsividade

- **Desktop**: Layout de duas colunas (1fr 1fr) 
- **Mobile**: Uma coluna adaptável
- **Cards**: Altura mínima de 450px para visual consistente
- **Gap**: 30px entre seções para melhor espaçamento
- **Breakpoint**: 768px para mudança de layout
- **Compatibilidade**: Funciona em Desktop, Smartphones e Tablets

## �️ Estrutura do Projeto

```
CriadorQRcode/
├── app.py                      # Aplicação Flask principal
├── admin_themes.py             # Sistema de gerenciamento de temas
├── tema.sh                     # Script rápido de seleção de temas
├── selecionar_tema.py          # Script interativo de temas
├── themes_config.json          # Configuração dos temas
├── templates/
│   └── index.html              # Template HTML principal
├── static/
│   ├── css/
│   │   ├── style.css           # CSS principal
│   │   └── themes/             # Pasta com todos os temas CSS
│   │       ├── batman.css      # Tema Batman
│   │       ├── superman.css    # Tema Superman
│   │       ├── hulk.css        # Tema Hulk
│   │       ├── dark-vader.css  # Tema Dark Vader
│   │       ├── homem-ferro.css # Tema Homem de Ferro
│   │       ├── halloween.css   # Tema Halloween
│   │       ├── natal.css       # Tema Natal
│   │       ├── matrix.css      # Tema Matrix
│   │       └── original.css    # Tema Original
│   ├── js/
│   │   └── script.js           # JavaScript da aplicação
│   └── images/                 # Favicons e imagens
├── docs/                       # Documentação completa
├── Dockerfile                  # Configuração Docker
├── requirements.txt            # Dependências Python
└── README.md                   # Este arquivo
```

## 🎨 Personalização

### Criar Novo Tema

1. Copie o arquivo `static/css/themes/batman.css` como template
2. Modifique as cores e estilos desejados
3. Adicione o tema em `themes_config.json`
4. Execute `python admin_themes.py change seu-novo-tema`

### Exemplo de Configuração de Tema

```json
{
  "seu-tema": {
    "name": "Seu Tema Personalizado",
    "description": "Descrição do seu tema",
    "css_file": "themes/seu-tema.css",
    "icon": "🎨"
  }
}
```

## 🔧 Recursos Técnicos

- **Framework**: Flask (Python 3.7+)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **QR Code**: Biblioteca qrcode com PIL
- **Layout**: CSS Grid responsivo de duas colunas
- **Temas**: Sistema dinâmico de troca de temas
- **Ícones**: Favicons múltiplos tamanhos
- **PWA**: Web App Manifest incluído
- **SEO**: Meta tags otimizadas
- **Validações**: Validação de telefone e URL

## 🚀 Deploy

### Método 1: Railway (Recomendado)
1. Fork este repositório
2. Conecte com Railway  
3. Deploy automático configurado

### Método 2: Docker
```bash
docker build -t qrcode-generator .
docker run -p 5000:5000 qrcode-generator
```

### Método 3: Heroku
```bash
git push heroku main
```

### Método 4: Outros Serviços
- **Vercel**: Para aplicações web
- **DigitalOcean**: VPS próprio
- **AWS**: EC2 ou Elastic Beanstalk

## 📚 Documentação Adicional

- [📖 Guia Completo de Temas](docs/README_THEMES.md)
- [🚀 Guia de Deploy](docs/DEPLOY_GUIDE.md)
- [🎯 Exemplos Práticos](docs/EXEMPLO_PRATICO.md)
- [📋 Scripts de Temas](docs/SCRIPTS_TEMAS.md)

## 🤝 Contribuição

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add: Amazing Feature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Hendel Santos**
- GitHub: [@hendelsantos](https://github.com/hendelsantos)  
- LinkedIn: [Hendel Santos](https://linkedin.com/in/hendelsantos)

## 🌟 Agradecimentos

- Inspirado nos personagens da DC Comics, Marvel e filmes clássicos
- Comunidade Flask pela excelente documentação
- Todos que contribuíram com feedback e sugestões

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela no repositório!**

Este projeto foi criado para uso pessoal e educacional.

---

**Feito por Hendel** ❤️
