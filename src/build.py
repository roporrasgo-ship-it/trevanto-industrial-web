#!/usr/bin/env python3
"""
Genera index.html a partir de src/template.html + src/assets/*
Uso: python3 src/build.py   (ejecutar desde la raíz del repo)
"""
import base64
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
ASSETS = os.path.join(SRC, "assets")

categories = [
    {
        "title": "Cintas y Adhesivos",
        "desc": "Cinta canela, cinta de seguridad, doble cara y dispensadores para sellado de cajas y empaques.",
        "items": ["Cinta canela", "Cinta de seguridad", "Doble cara", "Dispensadores"],
        "icon": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3.2"/>'
    },
    {
        "title": "Film Stretch / Emplaye",
        "desc": "Film manual y de máquina para asegurar tarimas y proteger producto durante transporte y almacenaje.",
        "items": ["Film manual", "Film máquina", "Protección de pallets"],
        "icon": '<rect x="4" y="4" width="16" height="16" rx="2"/><path stroke-linecap="round" d="M4 9h16M4 14h16M9 4v16M14 4v16"/>'
    },
    {
        "title": "Flejes y Flejadoras",
        "desc": "Fleje plástico y metálico, hebillas, grapas y equipo flejador manual o neumático.",
        "items": ["Fleje plástico", "Fleje metálico", "Flejadoras", "Hebillas"],
        "icon": '<path stroke-linecap="round" stroke-linejoin="round" d="M6 4h12v6a6 6 0 01-12 0V4z"/><path stroke-linecap="round" d="M9 20h6M12 16v4"/>'
    },
    {
        "title": "Cajas y Cartón",
        "desc": "Cajas estándar y a medida, cartón corrugado y coroplast para empaque secundario.",
        "items": ["Cajas estándar", "Cajas a medida", "Cartón corrugado", "Coroplast"],
        "icon": '<path stroke-linecap="round" stroke-linejoin="round" d="M3 8l9-5 9 5-9 5-9-5z"/><path stroke-linecap="round" stroke-linejoin="round" d="M3 8v8l9 5 9-5V8"/><path stroke-linecap="round" d="M12 13v8"/>'
    },
    {
        "title": "Bolsas Industriales",
        "desc": "Bolsas de polietileno, burbuja y antiestáticas para protección y presentación de producto.",
        "items": ["Polietileno", "Burbuja", "Antiestáticas"],
        "icon": '<path stroke-linecap="round" stroke-linejoin="round" d="M6 8h12l-1 12a2 2 0 01-2 2H9a2 2 0 01-2-2L6 8z"/><path stroke-linecap="round" d="M9 8V6a3 3 0 016 0v2"/>'
    },
    {
        "title": "Grapas y Consumibles",
        "desc": "Grapas industriales, engrapadoras y accesorios de consumo constante para línea de empaque.",
        "items": ["Grapas industriales", "Engrapadoras", "Accesorios"],
        "icon": '<rect x="5" y="10" width="14" height="4" rx="1"/><path stroke-linecap="round" d="M7 10V6a1 1 0 011-1h8a1 1 0 011 1v4M7 14v4a1 1 0 001 1h8a1 1 0 001-1v-4"/>'
    },
    {
        "title": "Protección de Carga",
        "desc": "Esquineros, espuma, separadores y plástico burbuja para evitar daños durante el traslado.",
        "items": ["Esquineros", "Espuma protectora", "Separadores"],
        "icon": '<path stroke-linecap="round" stroke-linejoin="round" d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3z"/>'
    },
    {
        "title": "Seguridad Industrial (EPP)",
        "desc": "Guantes, lentes, mascarillas y protección auditiva para el personal de almacén y línea.",
        "items": ["Guantes", "Lentes de seguridad", "Mascarillas", "Protección auditiva"],
        "icon": '<path stroke-linecap="round" stroke-linejoin="round" d="M12 2a7 7 0 00-7 7v3a2 2 0 00-2 2v2a2 2 0 002 2h1a1 1 0 001-1v-6a5 5 0 0110 0v6a1 1 0 001 1h1a2 2 0 002-2v-2a2 2 0 00-2-2V9a7 7 0 00-7-7z"/>'
    },
]

card_tpl = """      <div class="cat-card" data-search="{search}">
        <div class="cat-icon"><svg viewBox="0 0 24 24" stroke-width="1.6">{icon}</svg></div>
        <h3>{title}</h3>
        <p class="cat-desc">{desc}</p>
        <div class="chip-list">{chips}</div>
        <a href="#contacto" class="quote-link">Solicitar cotización <svg viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      </div>"""

def build():
    cards_html = []
    for c in categories:
        chips = "".join(f'<span class="chip">{i}</span>' for i in c["items"])
        search_text = (c["title"] + " " + c["desc"] + " " + " ".join(c["items"])).lower()
        cards_html.append(card_tpl.format(search=search_text, icon=c["icon"], title=c["title"], desc=c["desc"], chips=chips))
    cards_block = "\n".join(cards_html)

    with open(os.path.join(SRC, "template.html"), "r", encoding="utf-8") as f:
        html = f.read()

    html = html.replace("      <!-- CATALOG_CARDS -->", cards_block)

    def b64(path, mime):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode("ascii")
        return f"data:{mime};base64,{data}"

    html = html.replace("{{LOGO_HORIZONTAL}}", b64(os.path.join(ASSETS, "logo-horizontal.png"), "image/png"))
    html = html.replace("{{LOGO_ICON}}", b64(os.path.join(ASSETS, "logo-icon.png"), "image/png"))
    html = html.replace("{{HERO_BANNER}}", b64(os.path.join(ASSETS, "hero-banner.jpg"), "image/jpeg"))

    out_path = os.path.join(ROOT, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"OK: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    build()
