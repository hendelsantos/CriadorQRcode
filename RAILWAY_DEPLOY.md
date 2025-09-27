# Deploy no Railway 🚂

Este guia explica como fazer deploy da aplicação QR Code Generator no Railway.

## 🚀 Deploy Automático

### Método 1: Via GitHub (Recomendado)

1. **Conectar ao Railway:**
   - Acesse [railway.app](https://railway.app)
   - Faça login com sua conta GitHub
   - Clique em "New Project"
   - Selecione "Deploy from GitHub repo"
   - Escolha o repositório `hendelsantos/CriadorQRcode`

2. **Configuração Automática:**
   - O Railway detectará automaticamente que é uma aplicação Python
   - Usará os arquivos de configuração criados:
     - `requirements.txt` - Dependências Python
     - `Procfile` - Comando de inicialização
     - `runtime.txt` - Versão do Python
     - `railway.json` - Configurações específicas
     - `nixpacks.toml` - Build configuration

3. **Deploy:**
   - O Railway iniciará o build automaticamente
   - Aguarde a conclusão (geralmente 2-3 minutos)
   - Sua aplicação estará disponível em uma URL gerada automaticamente

### Método 2: Via Railway CLI

1. **Instalar Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login:**
   ```bash
   railway login
   ```

3. **Deploy:**
   ```bash
   cd CriarQRcode
   railway init
   railway up
   ```

## ⚙️ Configurações

### Variáveis de Ambiente (Opcional)

No painel do Railway, você pode configurar:

- `FLASK_ENV=production` - Ambiente de produção
- `WEB_CONCURRENCY=2` - Número de workers Gunicorn

### Arquivos de Configuração Incluídos

- **`Procfile`** - Define como iniciar a aplicação
- **`requirements.txt`** - Lista todas as dependências Python
- **`runtime.txt`** - Especifica a versão do Python
- **`railway.json`** - Configurações específicas do Railway
- **`nixpacks.toml`** - Configurações de build
- **`gunicorn.conf.py`** - Configurações do servidor Gunicorn

## 🔍 Monitoramento

### Health Check
A aplicação inclui um endpoint de saúde em `/health` que retorna:
```json
{
  "status": "healthy",
  "service": "QR Code Generator",
  "version": "1.0.0"
}
```

### Logs
Acesse os logs em tempo real no painel do Railway para monitorar a aplicação.

## 🌐 Domínio Personalizado

1. No painel do Railway, vá para Settings
2. Clique em "Domains"
3. Adicione seu domínio personalizado
4. Configure os registros DNS conforme instruído

## 💰 Custos

- **Hobby Plan**: Gratuito com limitações
- **Pro Plan**: $5/mês por projeto com recursos ilimitados

## 🆘 Troubleshooting

### Build Falha
- Verifique se todas as dependências estão no `requirements.txt`
- Confirme que o `runtime.txt` tem uma versão válida do Python

### Aplicação não Inicia
- Verifique o `Procfile` e `gunicorn.conf.py`
- Confirme que a variável `PORT` está sendo usada corretamente

### Erro 503
- Verifique os logs para erros de importação
- Confirme que todas as rotas estão funcionando localmente

## 📞 Suporte

- [Documentação Railway](https://docs.railway.app)
- [Discord Railway](https://railway.app/discord)
- [GitHub Issues](https://github.com/hendelsantos/CriadorQRcode/issues)
