#!/usr/bin/env python3
"""
🔧 CORRETOR DE LAYOUT DOS TEMAS
===============================
Script para aplicar o layout correto de duas colunas em todos os temas,
seguindo exatamente o padrão do tema Batman.
"""

import os
import re

def get_batman_structure():
    """Extrai a estrutura CSS do Batman como template."""
    batman_file = "static/css/themes/batman.css"
    
    with open(batman_file, 'r', encoding='utf-8') as f:
        batman_css = f.read()
    
    # Extrair seções principais
    container_section = re.search(r'\.container\s*\{[^}]*\}', batman_css, re.DOTALL)
    main_content_section = re.search(r'/\* Layout de duas colunas \*/.*?\.main-content\s*\{[^}]*\}', batman_css, re.DOTALL)
    form_section = re.search(r'\.form-section\s*\{[^}]*\}', batman_css, re.DOTALL)
    result_section = re.search(r'\.result-section\s*\{[^}]*\}', batman_css, re.DOTALL)
    
    return {
        'container': container_section.group() if container_section else '',
        'main_content': main_content_section.group() if main_content_section else '',
        'form_section': form_section.group() if form_section else '',
        'result_section': result_section.group() if result_section else ''
    }

def create_corrected_theme_css(theme_name, original_css, batman_structure, theme_colors):
    """Cria CSS corrigido para um tema específico."""
    
    # Template base com estrutura correta
    template = f'''/* TEMA {theme_name.upper()} - Layout Corrigido de Duas Colunas */
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: 'Arial Black', Arial, sans-serif;
    background: {theme_colors['bg_gradient']};
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    color: #fff;
    position: relative;
}}

body::before {{
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: {theme_colors['bg_effects']};
    pointer-events: none;
    z-index: -1;
    animation: {theme_colors['animation']} 4s ease-in-out infinite alternate;
}}

@keyframes {theme_colors['animation']} {{
    0% {{ opacity: 0.7; }}
    100% {{ opacity: 1; }}
}}

.container {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 20px;
    max-width: 1000px;
    margin: 0 auto;
}}

/* Layout de duas colunas */
.main-content {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    width: 100%;
    align-items: stretch; /* Cards com mesma altura */
}}

.form-section {{
    background: {theme_colors['card_bg']};
    padding: 30px;
    border-radius: 15px;
    box-shadow: {theme_colors['card_shadow']};
    border: 2px solid {theme_colors['border_color']};
    display: flex;
    flex-direction: column;
    min-height: 450px; /* Altura menor */
    animation: {theme_colors['card_animation']} 0.8s ease-out;
}}

.result-section {{
    background: {theme_colors['card_bg']};
    padding: 30px;
    border-radius: 15px;
    box-shadow: {theme_colors['card_shadow']};
    border: 2px solid {theme_colors['border_color']};
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 450px; /* Altura menor */
    animation: {theme_colors['card_animation']} 1s ease-out;
}}

@keyframes {theme_colors['card_animation']} {{
    0% {{ transform: scale(0.9); opacity: 0; }}
    100% {{ transform: scale(1); opacity: 1; }}
}}

h1 {{
    color: {theme_colors['primary']};
    text-align: center;
    margin-bottom: 25px;
    font-size: 2.2rem;
    text-shadow: {theme_colors['title_shadow']};
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 2px;
    animation: {theme_colors['title_animation']} 2s ease-in-out infinite alternate;
}}

@keyframes {theme_colors['title_animation']} {{
    from {{ text-shadow: {theme_colors['title_shadow']}; }}
    to {{ text-shadow: {theme_colors['title_shadow_glow']}; }}
}}

.form-group {{
    margin-bottom: 20px;
}}

.type-selector {{
    display: flex;
    gap: 10px;
    margin-bottom: 25px;
}}

.type-btn {{
    flex: 1;
    padding: 12px 20px;
    background: {theme_colors['secondary_bg']};
    color: {theme_colors['text_color']};
    border: 2px solid {theme_colors['secondary_border']};
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: bold;
    text-align: center;
}}

.type-btn.active,
.type-btn:hover {{
    background: {theme_colors['primary']};
    color: #000;
    border-color: {theme_colors['primary']};
    transform: translateY(-2px);
    box-shadow: {theme_colors['button_hover_shadow']};
}}

.form-group label {{
    display: block;
    margin-bottom: 8px;
    color: {theme_colors['label_color']};
    font-weight: bold;
    font-size: 1.1rem;
    text-shadow: 0 0 5px {theme_colors['primary']};
}}

.form-control {{
    width: 100%;
    padding: 15px;
    border: 2px solid {theme_colors['input_border']};
    border-radius: 8px;
    background: {theme_colors['input_bg']};
    color: {theme_colors['input_color']};
    font-size: 1rem;
    transition: all 0.3s ease;
}}

.form-control:focus {{
    outline: none;
    border-color: {theme_colors['primary']};
    background: {theme_colors['input_focus_bg']};
    box-shadow: 0 0 15px {theme_colors['focus_shadow']};
    transform: scale(1.02);
}}

.form-control::placeholder {{
    color: {theme_colors['placeholder_color']};
    opacity: 0.7;
}}

.btn {{
    background: linear-gradient(45deg, {theme_colors['btn_gradient']});
    color: #fff;
    border: none;
    padding: 15px 30px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1.1rem;
    font-weight: bold;
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
    box-shadow: {theme_colors['button_shadow']};
    position: relative;
    overflow: hidden;
}}

.btn::before {{
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.5s;
}}

.btn:hover {{
    background: linear-gradient(45deg, {theme_colors['btn_hover_gradient']});
    box-shadow: {theme_colors['button_hover_shadow']};
    transform: translateY(-2px);
}}

.btn:hover::before {{
    left: 100%;
}}

.btn:active {{
    transform: translateY(0px) scale(0.95);
}}

.btn-secondary {{
    background: linear-gradient(45deg, {theme_colors['btn_secondary']});
    margin-top: 10px;
}}

.btn-secondary:hover {{
    background: linear-gradient(45deg, {theme_colors['btn_secondary_hover']});
}}

.qr-container {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    width: 100%;
    flex: 1;
    justify-content: center;
}}

#qr-code {{
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: {theme_colors['qr_shadow']};
    animation: {theme_colors['qr_animation']} 0.8s ease-out;
}}

@keyframes {theme_colors['qr_animation']} {{
    0% {{ opacity: 0; transform: scale(0.5) rotate(-180deg); }}
    100% {{ opacity: 1; transform: scale(1) rotate(0deg); }}
}}

#qr-code img {{
    display: block;
    margin: 0 auto;
    border-radius: 5px;
}}

.qr-actions {{
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 20px;
}}

.qr-actions .btn {{
    flex: 1;
    min-width: 120px;
}}

/* Responsive Design */
@media (max-width: 768px) {{
    .main-content {{
        grid-template-columns: 1fr;
        gap: 20px;
    }}
    
    .container {{
        padding: 15px;
    }}
    
    h1 {{
        font-size: 1.8rem;
        margin-bottom: 20px;
    }}
    
    .form-section,
    .result-section {{
        min-height: auto;
        padding: 20px;
    }}
    
    .type-selector {{
        flex-direction: column;
    }}
    
    .btn {{
        padding: 12px 24px;
        font-size: 1rem;
    }}
    
    .qr-actions {{
        flex-direction: column;
    }}
    
    .qr-actions .btn {{
        min-width: auto;
    }}
}}

{theme_colors.get('extra_css', '')}
'''
    return template

def get_theme_colors(theme_name):
    """Define cores e estilos específicos para cada tema."""
    themes = {
        'superman': {
            'bg_gradient': 'linear-gradient(135deg, #0c2e5a 0%, #1e4d73 25%, #dc143c 50%, #1e4d73 75%, #0c2e5a 100%)',
            'bg_effects': '''
        radial-gradient(circle at 30% 30%, rgba(220, 20, 60, 0.15) 0%, transparent 60%),
        radial-gradient(circle at 70% 20%, rgba(255, 215, 0, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 20% 80%, rgba(30, 77, 115, 0.2) 0%, transparent 50%)''',
            'animation': 'hero-aura',
            'card_bg': 'rgba(12, 46, 90, 0.95)',
            'card_shadow': '''
        0 15px 35px rgba(220, 20, 60, 0.4),
        inset 0 1px 0 rgba(255, 215, 0, 0.2)''',
            'border_color': 'rgba(220, 20, 60, 0.6)',
            'card_animation': 'hero-rise',
            'primary': '#ffd700',
            'title_shadow': '3px 3px 6px rgba(0,0,0,0.7), 0 0 15px rgba(220, 20, 60, 0.5)',
            'title_shadow_glow': '3px 3px 6px rgba(0,0,0,0.9), 0 0 25px rgba(255, 215, 0, 0.6)',
            'title_animation': 'superman-glow',
            'secondary_bg': 'rgba(30, 77, 115, 0.8)',
            'text_color': '#ffd700',
            'secondary_border': 'rgba(220, 20, 60, 0.5)',
            'button_hover_shadow': '0 6px 25px rgba(255, 215, 0, 0.5)',
            'label_color': '#ffd700',
            'input_border': '#1e4d73',
            'input_bg': 'rgba(0, 0, 0, 0.6)',
            'input_color': '#ffd700',
            'input_focus_bg': 'rgba(0, 0, 0, 0.8)',
            'focus_shadow': 'rgba(255, 215, 0, 0.4)',
            'placeholder_color': '#daa520',
            'btn_gradient': '#dc143c, #ffd700',
            'btn_hover_gradient': '#ffd700, #ffff00',
            'button_shadow': '0 4px 15px rgba(255, 215, 0, 0.4)',
            'btn_secondary': '#1e4d73, #2e6b99',
            'btn_secondary_hover': '#2e6b99, #4a8bc2',
            'qr_shadow': '0 8px 30px rgba(255, 215, 0, 0.3)',
            'qr_animation': 'cape-flutter'
        },
        'hulk': {
            'bg_gradient': 'linear-gradient(135deg, #0d2818 0%, #228b22 25%, #32cd32 50%, #228b22 75%, #0d2818 100%)',
            'bg_effects': '''
        radial-gradient(circle at 30% 30%, rgba(50, 205, 50, 0.2) 0%, transparent 60%),
        radial-gradient(circle at 70% 20%, rgba(128, 0, 128, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 20% 80%, rgba(34, 139, 34, 0.15) 0%, transparent 50%)''',
            'animation': 'hulk-rage',
            'card_bg': 'rgba(13, 40, 24, 0.95)',
            'card_shadow': '''
        0 15px 35px rgba(50, 205, 50, 0.4),
        inset 0 1px 0 rgba(128, 0, 128, 0.2)''',
            'border_color': 'rgba(50, 205, 50, 0.6)',
            'card_animation': 'hulk-smash',
            'primary': '#32cd32',
            'title_shadow': '3px 3px 6px rgba(0,0,0,0.7), 0 0 15px rgba(50, 205, 50, 0.5)',
            'title_shadow_glow': '3px 3px 6px rgba(0,0,0,0.9), 0 0 25px rgba(50, 205, 50, 0.6)',
            'title_animation': 'hulk-glow',
            'secondary_bg': 'rgba(34, 139, 34, 0.8)',
            'text_color': '#32cd32',
            'secondary_border': 'rgba(128, 0, 128, 0.5)',
            'button_hover_shadow': '0 6px 25px rgba(50, 205, 50, 0.5)',
            'label_color': '#32cd32',
            'input_border': '#228b22',
            'input_bg': 'rgba(0, 0, 0, 0.6)',
            'input_color': '#32cd32',
            'input_focus_bg': 'rgba(0, 0, 0, 0.8)',
            'focus_shadow': 'rgba(50, 205, 50, 0.4)',
            'placeholder_color': '#90ee90',
            'btn_gradient': '#228b22, #32cd32',
            'btn_hover_gradient': '#32cd32, #00ff00',
            'button_shadow': '0 4px 15px rgba(50, 205, 50, 0.4)',
            'btn_secondary': '#800080, #9932cc',
            'btn_secondary_hover': '#9932cc, #ba55d3',
            'qr_shadow': '0 8px 30px rgba(50, 205, 50, 0.3)',
            'qr_animation': 'hulk-appear'
        }
    }
    
    return themes.get(theme_name, themes['superman'])  # Default para superman se não encontrar

# Lista de temas para corrigir
themes_to_fix = ['superman', 'hulk', 'dark-vader', 'homem-ferro', 'halloween', 'natal', 'matrix', 'original']

print("🔧 Corrigindo layout de todos os temas...")
print("=" * 50)

for theme in themes_to_fix:
    theme_file = f"static/css/themes/{theme}.css"
    
    if os.path.exists(theme_file):
        print(f"🔄 Corrigindo {theme}...")
        
        # Ler CSS original
        with open(theme_file, 'r', encoding='utf-8') as f:
            original_css = f.read()
        
        # Fazer backup
        backup_file = f"{theme_file}.backup"
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(original_css)
        
        # Obter cores do tema
        theme_colors = get_theme_colors(theme)
        
        # Criar CSS corrigido
        corrected_css = create_corrected_theme_css(theme, original_css, None, theme_colors)
        
        # Salvar CSS corrigido
        with open(theme_file, 'w', encoding='utf-8') as f:
            f.write(corrected_css)
        
        print(f"   ✅ {theme} corrigido!")
        print(f"   💾 Backup salvo: {backup_file}")
    else:
        print(f"   ❌ Arquivo não encontrado: {theme_file}")

print("\n🎉 Correção de layout concluída!")
print("🔄 Reinicie o servidor para ver as mudanças.")
