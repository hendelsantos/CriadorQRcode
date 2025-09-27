#!/usr/bin/env python3
import os

# Configurações dos temas
themes_config = {
    "homem-ferro": {
        "colors": {"primary": "#ffd700", "secondary": "#8b0000", "text": "#ffd700"},
        "name": "HOMEM DE FERRO ❤️🤖 - Tony Stark Technology",
        "bg_gradient": "linear-gradient(135deg, #1a0f0f 0%, #8b0000 25%, #ffd700 50%, #8b0000 75%, #1a0f0f 100%)"
    },
    "halloween": {
        "colors": {"primary": "#ff6600", "secondary": "#800080", "text": "#ff6600"},
        "name": "HALLOWEEN 🎃👻 - Noite Assombrada",
        "bg_gradient": "linear-gradient(135deg, #000000 0%, #4a0e4e 25%, #ff6600 50%, #4a0e4e 75%, #000000 100%)"
    },
    "matrix": {
        "colors": {"primary": "#00ff00", "secondary": "#003300", "text": "#00ff00"},
        "name": "MATRIX 💊🔢 - O Código da Matrix",
        "bg_gradient": "linear-gradient(135deg, #000000 0%, #001100 25%, #003300 50%, #001100 75%, #000000 100%)"
    }
}

# Template CSS base
css_template = '''/* TEMA {name} - Layout Atualizado */
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: 'Arial Black', Arial, sans-serif;
    background: {bg_gradient};
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    color: #fff;
    position: relative;
}}

.container {{
    flex: 1;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    align-items: stretch;
    padding: 20px;
    max-width: 1000px;
    margin: 0 auto;
}}

h1 {{
    text-align: center;
    color: {primary};
    margin-bottom: 30px;
    font-size: 2.8rem;
    text-shadow: 
        0 0 10px {primary},
        0 0 20px {primary},
        0 0 30px {primary};
    animation: theme-glow 2s ease-in-out infinite alternate;
    grid-column: 1 / -1;
}}

@keyframes theme-glow {{
    from {{ text-shadow: 0 0 10px {primary}, 0 0 20px {primary}; }}
    to {{ text-shadow: 0 0 20px {primary}, 0 0 30px {primary}, 0 0 40px {primary}; }}
}}

.form-section {{
    background: rgba(26, 15, 15, 0.95);
    padding: 30px;
    border-radius: 15px;
    border: 2px solid {primary};
    box-shadow: 
        0 0 30px rgba{primary_rgba},
        inset 0 0 20px rgba{secondary_rgba};
    backdrop-filter: blur(10px);
    min-height: 450px;
    display: flex;
    flex-direction: column;
    animation: card-appear 0.8s ease-out;
}}

.result-section {{
    background: rgba(26, 15, 15, 0.95);
    padding: 30px;
    border-radius: 15px;
    border: 2px solid {primary};
    box-shadow: 
        0 0 30px rgba{primary_rgba},
        inset 0 0 20px rgba{secondary_rgba};
    backdrop-filter: blur(10px);
    min-height: 450px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    animation: card-appear 1s ease-out;
}}

@keyframes card-appear {{
    0% {{ transform: scale(0.9); opacity: 0; }}
    100% {{ transform: scale(1); opacity: 1; }}
}}

.form-group {{
    margin-bottom: 20px;
}}

.form-group label {{
    display: block;
    margin-bottom: 8px;
    color: {text};
    font-weight: bold;
    font-size: 1.1rem;
    text-shadow: 0 0 5px {primary};
}}

.form-control {{
    width: 100%;
    padding: 15px;
    border: 2px solid {secondary};
    border-radius: 8px;
    background: rgba(0, 0, 0, 0.6);
    color: {text};
    font-size: 1rem;
    transition: all 0.3s ease;
}}

.form-control:focus {{
    outline: none;
    border-color: {primary};
    background: rgba(0, 0, 0, 0.8);
    box-shadow: 0 0 15px rgba{primary_rgba};
    transform: scale(1.02);
}}

.btn {{
    background: linear-gradient(45deg, {secondary}, {primary});
    color: white;
    border: none;
    padding: 15px 30px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1.1rem;
    font-weight: bold;
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
    box-shadow: 0 4px 15px rgba{primary_rgba};
    position: relative;
    overflow: hidden;
}}

.btn:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 25px rgba{primary_rgba};
}}

.btn:active {{
    transform: translateY(0px) scale(0.95);
}}

.btn-secondary {{
    background: linear-gradient(45deg, #333, #666);
    margin-top: 10px;
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
    box-shadow: 0 8px 30px rgba{primary_rgba};
    animation: qr-appear 0.8s ease-out;
}}

@keyframes qr-appear {{
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
}}

.qr-actions .btn {{
    flex: 1;
    min-width: 120px;
}}

/* Responsive Design */
@media (max-width: 768px) {{
    .container {{
        grid-template-columns: 1fr;
        gap: 20px;
        padding: 15px;
    }}
    
    h1 {{
        font-size: 2.2rem;
        margin-bottom: 20px;
    }}
    
    .form-section,
    .result-section {{
        min-height: auto;
        padding: 20px;
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
'''

# Função para converter cor hex para rgba
def hex_to_rgba(hex_color, alpha=0.3):
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"({r}, {g}, {b}, {alpha})"

# Gerar temas
for theme_key, config in themes_config.items():
    colors = config["colors"]
    primary_rgba = hex_to_rgba(colors["primary"])
    secondary_rgba = hex_to_rgba(colors["secondary"], 0.2)
    
    css_content = css_template.format(
        name=config["name"],
        bg_gradient=config["bg_gradient"],
        primary=colors["primary"],
        secondary=colors["secondary"],
        text=colors["text"],
        primary_rgba=primary_rgba,
        secondary_rgba=secondary_rgba
    )
    
    with open(f"static/css/themes/{theme_key}.css", "w") as f:
        f.write(css_content)
    
    print(f"✅ Tema {theme_key} atualizado!")

print("\n🎉 Atualização completa!")
