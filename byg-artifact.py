#!/usr/bin/env python3
"""Laver en artifact-udgave af spil.html (uden <html>/<head>/<body>)."""
import re, sys, pathlib

kilde = pathlib.Path(__file__).parent / 'spil.html'
mål = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path('byg-burgeren.html')

s = kilde.read_text(encoding='utf-8')
s = re.sub(r'^<!DOCTYPE html>\s*', '', s)
s = re.sub(r'<!--.*?-->\s*', '', s, count=1, flags=re.S)
for tag in ['<html lang="da">', '<head>', '</head>', '<body>', '</body>', '</html>']:
    s = s.replace(tag + '\n', '').replace(tag, '')
s = re.sub(r'<meta[^>]*>\n?', '', s)
titel = re.search(r'<title>.*?</title>', s, re.S).group(0)
s = s.replace(titel + '\n', '').replace(titel, '')
s = '<title>Byg Burgeren</title>\n' + s.lstrip()
mål.write_text(s, encoding='utf-8')
print('skrev', mål, len(s), 'tegn')
