// Elementos DOM
const form = document.getElementById('qrForm');
const typeButtons = document.querySelectorAll('.type-btn');
const inputSections = document.querySelectorAll('.input-section');
const resultSection = document.getElementById('result-section');
const loading = document.getElementById('loading');
const alert = document.getElementById('alert');
const alertMessage = document.getElementById('alert-message');
const alertClose = document.getElementById('alert-close');

// Inputs
const phoneInput = document.getElementById('phone');
const urlInput = document.getElementById('url');
const textInput = document.getElementById('text');

// Botões de ação
const downloadBtn = document.getElementById('download-btn');
const copyBtn = document.getElementById('copy-btn');
const shareBtn = document.getElementById('share-btn');

// Variáveis globais
let currentType = 'whatsapp';
let currentContent = '';
let currentQRData = '';

// Inicialização
document.addEventListener('DOMContentLoaded', function() {
    initializeEventListeners();
    formatPhoneInput();
});

// Inicializa todos os event listeners
function initializeEventListeners() {
    // Seletor de tipo
    typeButtons.forEach(button => {
        button.addEventListener('click', () => switchType(button.dataset.type));
    });

    // Formulário
    form.addEventListener('submit', handleFormSubmit);

    // Botões de ação
    downloadBtn.addEventListener('click', downloadQRCode);
    copyBtn.addEventListener('click', copyQRCode);
    shareBtn.addEventListener('click', shareQRCode);

    // Alert close
    alertClose.addEventListener('click', hideAlert);

    // Auto-hide alert após 5 segundos
    setTimeout(hideAlert, 5000);
}

// Formatar input de telefone
function formatPhoneInput() {
    phoneInput.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');
        let formattedValue = '';
        
        if (value.length > 0) {
            if (value.length <= 2) {
                formattedValue = `(${value}`;
            } else if (value.length <= 7) {
                formattedValue = `(${value.slice(0, 2)}) ${value.slice(2)}`;
            } else if (value.length <= 11) {
                formattedValue = `(${value.slice(0, 2)}) ${value.slice(2, 7)}-${value.slice(7)}`;
            } else {
                formattedValue = `(${value.slice(0, 2)}) ${value.slice(2, 7)}-${value.slice(7, 11)}`;
            }
        }
        
        e.target.value = formattedValue;
    });
}

// Trocar tipo de QR Code
function switchType(type) {
    currentType = type;
    
    // Atualizar botões
    typeButtons.forEach(btn => {
        btn.classList.toggle('active', btn.dataset.type === type);
    });
    
    // Atualizar seções de input
    inputSections.forEach(section => {
        section.classList.remove('active');
    });
    
    document.getElementById(`${type}-input`).classList.add('active');
    
    // Limpar resultado anterior
    clearResult();
}

// Processar envio do formulário
async function handleFormSubmit(e) {
    e.preventDefault();
    
    const content = getCurrentContent();
    if (!content.trim()) {
        showAlert('Por favor, preencha o campo obrigatório.', 'error');
        return;
    }
    
    currentContent = content;
    await generateQRCode();
}

// Obter conteúdo atual baseado no tipo selecionado
function getCurrentContent() {
    switch (currentType) {
        case 'whatsapp':
            return phoneInput.value.replace(/\D/g, '');
        case 'url':
            return urlInput.value.trim();
        case 'text':
            return textInput.value.trim();
        default:
            return '';
    }
}

// Gerar QR Code
async function generateQRCode() {
    showLoading(true);
    
    try {
        const response = await fetch('/generate_qr', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                type: currentType,
                content: currentContent
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            displayQRCode(data.image, data.data);
            showAlert('QR Code gerado com sucesso!', 'success');
        } else {
            throw new Error(data.error);
        }
        
    } catch (error) {
        console.error('Erro:', error);
        showAlert(error.message || 'Erro ao gerar QR Code. Tente novamente.', 'error');
    } finally {
        showLoading(false);
    }
}

// Exibir QR Code gerado
function displayQRCode(imageData, qrData) {
    currentQRData = qrData;
    
    const qrContainer = document.querySelector('.qr-container');
    const qrActions = document.querySelector('.qr-actions');
    const qrInfo = document.querySelector('.qr-info');
    const qrDataElement = document.getElementById('qr-data');
    
    // Criar elemento de imagem
    qrContainer.innerHTML = `<img src="${imageData}" alt="QR Code" class="qr-image" id="qr-image">`;
    
    // Mostrar ações e informações
    qrActions.style.display = 'flex';
    qrInfo.style.display = 'block';
    qrDataElement.textContent = qrData;
    
    // Scroll suave para o resultado
    resultSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Limpar resultado
function clearResult() {
    const qrContainer = document.querySelector('.qr-container');
    const qrActions = document.querySelector('.qr-actions');
    const qrInfo = document.querySelector('.qr-info');
    
    qrContainer.innerHTML = `
        <div class="qr-placeholder">
            <i class="fas fa-qrcode"></i>
            <p>Seu QR Code aparecerá aqui</p>
        </div>
    `;
    
    qrActions.style.display = 'none';
    qrInfo.style.display = 'none';
    currentQRData = '';
}

// Baixar QR Code
async function downloadQRCode() {
    if (!currentContent) {
        showAlert('Nenhum QR Code para baixar.', 'error');
        return;
    }
    
    try {
        const response = await fetch('/download_qr', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                type: currentType,
                content: currentContent
            })
        });
        
        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            
            // Nome do arquivo baseado no tipo
            let filename = 'qrcode.png';
            if (currentType === 'whatsapp') {
                filename = 'whatsapp-qrcode.png';
            } else if (currentType === 'url') {
                filename = 'url-qrcode.png';
            } else {
                filename = 'texto-qrcode.png';
            }
            
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
            
            showAlert('QR Code baixado com sucesso!', 'success');
        } else {
            throw new Error('Erro ao baixar o arquivo');
        }
    } catch (error) {
        console.error('Erro no download:', error);
        showAlert('Erro ao baixar QR Code. Tente novamente.', 'error');
    }
}

// Copiar QR Code para área de transferência
async function copyQRCode() {
    const qrImage = document.getElementById('qr-image');
    if (!qrImage) {
        showAlert('Nenhum QR Code para copiar.', 'error');
        return;
    }
    
    try {
        // Converter imagem para canvas
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        
        canvas.width = qrImage.naturalWidth;
        canvas.height = qrImage.naturalHeight;
        
        ctx.drawImage(qrImage, 0, 0);
        
        // Converter canvas para blob
        canvas.toBlob(async (blob) => {
            try {
                const item = new ClipboardItem({ 'image/png': blob });
                await navigator.clipboard.write([item]);
                showAlert('QR Code copiado para área de transferência!', 'success');
            } catch (error) {
                console.error('Erro ao copiar:', error);
                // Fallback: copiar texto
                await copyTextFallback();
            }
        });
        
    } catch (error) {
        console.error('Erro ao copiar imagem:', error);
        // Fallback: copiar texto
        await copyTextFallback();
    }
}

// Fallback para copiar texto
async function copyTextFallback() {
    try {
        await navigator.clipboard.writeText(currentQRData);
        showAlert('Dados do QR Code copiados como texto!', 'success');
    } catch (error) {
        console.error('Erro ao copiar texto:', error);
        showAlert('Erro ao copiar. Tente novamente.', 'error');
    }
}

// Compartilhar QR Code
async function shareQRCode() {
    if (!currentQRData) {
        showAlert('Nenhum QR Code para compartilhar.', 'error');
        return;
    }
    
    try {
        if (navigator.share) {
            // API Web Share (mobile/alguns browsers)
            await navigator.share({
                title: 'QR Code',
                text: `Confira este QR Code: ${currentQRData}`,
                url: currentQRData.startsWith('http') ? currentQRData : undefined
            });
        } else {
            // Fallback: copiar link
            await navigator.clipboard.writeText(currentQRData);
            showAlert('Link copiado para compartilhamento!', 'success');
        }
    } catch (error) {
        console.error('Erro ao compartilhar:', error);
        if (error.name !== 'AbortError') {
            showAlert('Erro ao compartilhar. Tente novamente.', 'error');
        }
    }
}

// Mostrar/ocultar loading
function showLoading(show) {
    loading.style.display = show ? 'flex' : 'none';
}

// Mostrar alerta
function showAlert(message, type = 'error') {
    alertMessage.textContent = message;
    alert.className = `alert ${type === 'success' ? 'success' : ''}`;
    alert.style.display = 'flex';
    
    // Auto-hide após 4 segundos
    setTimeout(hideAlert, 4000);
}

// Ocultar alerta
function hideAlert() {
    alert.style.display = 'none';
}

// Validações adicionais
function validatePhone(phone) {
    const cleanPhone = phone.replace(/\D/g, '');
    return cleanPhone.length >= 10 && cleanPhone.length <= 11;
}

function validateURL(url) {
    try {
        new URL(url.startsWith('http') ? url : 'https://' + url);
        return true;
    } catch {
        return false;
    }
}

// Atalhos de teclado
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + Enter para gerar QR Code
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        e.preventDefault();
        form.dispatchEvent(new Event('submit'));
    }
    
    // ESC para fechar alert
    if (e.key === 'Escape') {
        hideAlert();
    }
});

// Melhorar UX com animações
function addRippleEffect(button) {
    button.addEventListener('click', function(e) {
        const ripple = document.createElement('span');
        const rect = button.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;
        
        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.classList.add('ripple');
        
        button.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    });
}

// Aplicar efeito ripple nos botões
document.querySelectorAll('button').forEach(addRippleEffect);

// CSS para efeito ripple (adicionado dinamicamente)
const rippleStyle = document.createElement('style');
rippleStyle.textContent = `
    button {
        position: relative;
        overflow: hidden;
    }
    
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.6);
        transform: scale(0);
        animation: ripple-animation 0.6s ease-out;
        pointer-events: none;
    }
    
    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(rippleStyle);

// ================================
// EASTER EGG DISCRETO - FRASES NERDS
// ================================

// Frases nerds por tema
const nerdPhrases = {
    'batman': [
        "I'm Batman. 🦇",
        "Why do we fall? So we can learn to pick ourselves up.",
        "It's not who I am underneath, but what I do that defines me.",
        "I have one rule: I don't kill.",
        "The night is darkest just before the dawn."
    ],
    'superman': [
        "Truth, Justice, and the American Way! 🔵",
        "Sometimes you have to take a leap of faith first.",
        "You're much stronger than you think you are.",
        "There's always a way to fight back.",
        "Hope. That's what the S stands for."
    ],
    'hulk': [
        "Hulk Smash! 💚",
        "That's my secret, Cap. I'm always angry.",
        "Don't make me angry. You wouldn't like me when I'm angry.",
        "Hulk is strongest there is!",
        "Hulk protect!"
    ],
    'dark-vader': [
        "I find your lack of faith disturbing. 🌑",
        "The Force is strong with this one.",
        "You underestimate the power of the Dark Side.",
        "I am your father.",
        "Search your feelings, you know it to be true."
    ],
    'homem-ferro': [
        "I am Iron Man. ❤️",
        "Sometimes you gotta run before you can walk.",
        "Genius, billionaire, playboy, philanthropist.",
        "I love you 3000.",
        "Part of the journey is the end."
    ],
    'halloween': [
        "Boo! Did I scare you? 🎃",
        "Every day is Halloween, isn't it?",
        "We all go a little mad sometimes.",
        "Be afraid. Be very afraid.",
        "It's alive! IT'S ALIVE!"
    ],
    'natal': [
        "Ho ho ho! Merry Christmas! 🎄",
        "The best way to spread Christmas cheer is singing loud for all to hear.",
        "Every time a bell rings, an angel gets his wings.",
        "It's beginning to look a lot like Christmas!",
        "Peace on Earth, goodwill to men."
    ],
    'matrix': [
        "Welcome to the real world. 💊",
        "There is no spoon.",
        "Follow the white rabbit.",
        "The Matrix has you...",
        "Red pill or blue pill?"
    ],
    'original': [
        "Keep it simple, keep it classy. 💜",
        "Less is more.",
        "Simplicity is the ultimate sophistication.",
        "Good design is obvious. Great design is transparent.",
        "Design is thinking made visual."
    ]
};

// Easter Egg Trigger
const easterEggTrigger = document.getElementById('easter-egg-trigger');
const nerdPhraseDiv = document.getElementById('nerd-phrase');

if (easterEggTrigger && nerdPhraseDiv) {
    let clickCount = 0;
    let currentTheme = 'dark-vader'; // Default, será atualizado pelo Flask
    
    // Detectar tema atual do CSS
    const themeCSS = document.getElementById('theme-css');
    if (themeCSS) {
        const cssPath = themeCSS.getAttribute('href');
        const themeMatch = cssPath.match(/themes\/([^.]+)\.css/);
        if (themeMatch) {
            currentTheme = themeMatch[1];
        }
    }
    
    easterEggTrigger.addEventListener('click', function(event) {
        event.preventDefault();
        clickCount++;
        
        // Pequena animação no ícone
        this.style.transform = 'scale(1.3) rotate(20deg)';
        setTimeout(() => {
            this.style.transform = '';
        }, 200);
        
        // Mostrar frase nerd
        const phrases = nerdPhrases[currentTheme] || nerdPhrases['original'];
        const randomPhrase = phrases[Math.floor(Math.random() * phrases.length)];
        
        nerdPhraseDiv.textContent = randomPhrase;
        nerdPhraseDiv.style.display = 'block';
        
        // Esconder frase após 4 segundos
        setTimeout(() => {
            nerdPhraseDiv.style.display = 'none';
        }, 4000);
        
        // Easter egg especial após 5 cliques
        if (clickCount >= 5) {
            nerdPhraseDiv.textContent = "🤓 Nerd level unlocked! You found the secret!";
            clickCount = 0; // Reset
        }
    });
}
