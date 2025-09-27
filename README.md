# 🔲 Gerador de QR Code

Um serviço web moderno e intuitivo para gerar QR codes para WhatsApp, URLs e texto personalizado.

## ✨ Funcionalidades

- **WhatsApp**: Gere QR codes que abrem uma conversa no WhatsApp
- **URLs**: Crie QR codes para qualquer link ou website  
- **Texto**: Transforme qualquer texto em QR code
- **Interface moderna**: Design responsivo e bonito
- **Favicon personalizado**: Logo com QR Code em vários tamanhos
- **PWA Ready**: Pode ser instalado como aplicativo web
- **Download**: Baixe os QR codes como PNG
- **Copiar**: Copie a imagem para área de transferência
- **Compartilhar**: Compartilhe facilmente com outros
- **SEO otimizado**: Meta tags para melhor indexação

## 🚀 Como executar

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone ou baixe este projeto
2. Navegue até a pasta do projeto:
```bash
cd CriarQRcode
```

3. Crie um ambiente virtual (recomendado):
```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executar o aplicativo

```bash
python app.py
```

O aplicativo será executado em `http://localhost:5000`

## 🎯 Como usar

1. **Acesse** o aplicativo no seu navegador
2. **Escolha** o tipo de QR code que deseja gerar:
   - 📱 WhatsApp: Digite o número com DDD
   - 🔗 URL/Link: Cole qualquer link
   - 📝 Texto: Digite qualquer texto
3. **Clique** em "Gerar QR Code"
4. **Baixe**, **copie** ou **compartilhe** seu QR code

## 📱 Exemplos de uso

### WhatsApp
- Digite: `11999887766`
- Resultado: QR code que abre conversa no WhatsApp

### URL
- Digite: `www.github.com` ou `https://www.github.com`
- Resultado: QR code que abre o site

### Texto
- Digite: `Olá! Este é meu cartão de visitas digital`
- Resultado: QR code com o texto personalizado

## 🎨 Características técnicas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **QR Code**: Biblioteca qrcode com PIL
- **Design**: Interface moderna e responsiva
- **Validações**: Validação de telefone e URL
- **Formatação**: Formatação automática de números

## 📱 Responsividade

O aplicativo funciona perfeitamente em:
- 💻 Desktop
- 📱 Smartphones
- 📱 Tablets

## 🔧 Estrutura do projeto

```
CriarQRcode/
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências Python
├── README.md             # Este arquivo
├── generate_favicon.py   # Script para gerar favicons
├── generate_logo.py      # Script para gerar logos
├── Procfile              # Configuração Heroku
├── .gitignore            # Arquivos ignorados pelo Git
├── templates/
│   └── index.html        # Template principal
└── static/
    ├── css/
    │   └── style.css     # Estilos CSS
    ├── js/
    │   └── script.js     # JavaScript interativo
    ├── images/           # Logos e favicons
    │   ├── favicon.ico   # Favicon principal
    │   ├── favicon.svg   # Favicon vetorial
    │   ├── favicon-*.png # Favicons em vários tamanhos
    │   ├── logo.png      # Logo da aplicação
    │   └── logo-small.png # Logo pequeno
    └── manifest.json     # Manifesto PWA
```

## 🚀 Deploy

Para fazer deploy em produção, considere usar:
- **Heroku**: Platform as a Service
- **Vercel**: Para aplicações web
- **DigitalOcean**: VPS próprio
- **AWS**: EC2 ou Elastic Beanstalk

## 📝 Licença

Este projeto foi criado para uso pessoal e educacional.

---

**Feito por Hendel** ❤️
