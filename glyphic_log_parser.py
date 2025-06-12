# glyphic_log_parser.py
# Parses resonance_log.txt for glyphic trends

import re

log_path = './logs/resonance_log.txt'

glyph_pattern = re.compile(r'→ (\w+): \u27f2=(\d+\.\d+) \| \u223f=(\d+\.\d+) \| \u29eb=(\d+\.\d+) \| \u27e1=(\d+\.\d+) \| \u03de=(\d+\.\d+)')

tokens = []
glyphics = []

with open(log_path, 'r') as f:
    for line in f:
        match = glyph_pattern.search(line)
        if match:
            token, circ, echo, dens, cont, affect = match.groups()
            tokens.append(token)
            glyphics.append((float(circ), float(echo), float(dens), float(cont), float(affect)))

print("\nGlyphic Trends:")
print("Token\t⟲\t∿\t⧫\t⟡\tϞ")
for token, (circ, echo, dens, cont, affect) in zip(tokens, glyphics):
    print(f"{token}\t{circ:.2f}\t{echo:.2f}\t{dens:.2f}\t{cont:.2f}\t{affect:.2f}")
