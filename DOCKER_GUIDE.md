# Docker Deploy Guide 🐳

Este guia explica como usar Docker para deploy no Railway e desenvolvimento local.

## 🚀 Deploy no Railway com Docker

### Configuração Automática

O Railway detecta automaticamente o `Dockerfile` e faz o build usando Docker.

**Passos:**
1. Push do código para GitHub (já feito)
2. Railway detecta o `Dockerfile`
3. Build automático do container
4. Deploy automático

### Arquivos Docker Incluídos

- **`Dockerfile`** - Configuração principal do container
- **`.dockerignore`** - Arquivos ignorados no build
- **`docker-compose.yml`** - Para desenvolvimento local

## 🖥️ Desenvolvimento Local com Docker

### Opção 1: Docker Build Manual

```bash
# Build da imagem
docker build -t qrcode-generator .

# Executar container
docker run -p 5000:5000 -e PORT=5000 qrcode-generator
```

### Opção 2: Docker Compose (Recomendado)

```bash
# Iniciar aplicação
docker-compose up --build

# Executar em background
docker-compose up -d --build

# Ver logs
docker-compose logs -f

# Parar aplicação
docker-compose down
```

## 🔧 Características do Docker

### Dockerfile Features

- **Base**: Python 3.11 slim (menor tamanho)
- **Security**: Usuario não-root
- **Performance**: Multi-stage para otimização
- **Health Check**: Endpoint `/health`
- **Production Ready**: Gunicorn como servidor

### Otimizações Incluídas

- ✅ **Layer caching** - requirements.txt copiado primeiro
- ✅ **Security** - usuário não-root
- ✅ **Health checks** - monitoramento automático
- ✅ **Small image** - apenas dependências necessárias
- ✅ **Production server** - Gunicorn configurado

## 🌐 URLs de Acesso

### Local (Docker)
- http://localhost:5000
- http://127.0.0.1:5000

### Railway (Automático)
- Será fornecido após deploy

## 🔍 Monitoramento

### Health Check
O container inclui health check automático:
- **Endpoint**: `/health`
- **Intervalo**: 30s
- **Timeout**: 30s
- **Retries**: 3

### Logs
```bash
# Ver logs do container
docker logs <container_id>

# Ver logs em tempo real
docker logs -f <container_id>
```

## 🛠️ Comandos Úteis

### Build e Test Local
```bash
# Build da imagem
docker build -t qrcode-generator .

# Test da imagem
docker run --rm -p 5000:5000 qrcode-generator

# Shell no container
docker run -it --rm qrcode-generator /bin/bash
```

### Debugging
```bash
# Executar container em modo interativo
docker run -it --rm -p 5000:5000 qrcode-generator

# Ver informações da imagem
docker inspect qrcode-generator

# Ver layers da imagem
docker history qrcode-generator
```

## 📦 Tamanho da Imagem

A imagem Docker é otimizada para ser pequena:
- **Base**: python:3.11-slim (~45MB)
- **Dependencies**: ~50MB
- **Total estimado**: ~100MB

## 🔒 Segurança

- ✅ Usuario não-root
- ✅ Dependências mínimas
- ✅ Base image oficial Python
- ✅ Sem secrets no Dockerfile
- ✅ Health checks configurados

## 🆘 Troubleshooting

### Container não inicia
```bash
# Ver logs detalhados
docker logs <container_id>

# Executar em modo debug
docker run -it --rm qrcode-generator /bin/bash
```

### Port binding error
```bash
# Verificar porta em uso
netstat -tulpn | grep :5000

# Usar porta diferente
docker run -p 8000:5000 qrcode-generator
```

### Build falha
```bash
# Build com logs detalhados
docker build --no-cache -t qrcode-generator .

# Verificar .dockerignore
cat .dockerignore
```
