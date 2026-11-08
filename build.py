"""Génère index.html (version installable hors ligne) à partir de app-claude.html (version claude.ai)."""
from pathlib import Path
here = Path(__file__).parent
src = (here / "app-claude.html").read_text(encoding="utf-8")
head = """<meta name="theme-color" content="#181c25">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon-192.png">
<link rel="apple-touch-icon" href="icon-192.png">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}</style>
"""
marker = '<meta name="claude:viewport-fit-sides" content="cover">'
assert marker in src
out = "<!doctype html>\n<html lang=\"fr\">\n<head>\n" + src.replace(marker, marker + "\n" + head, 1)
(here / "index.html").write_text(out, encoding="utf-8")
print("index.html généré")
