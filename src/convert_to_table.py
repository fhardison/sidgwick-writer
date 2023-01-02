#!/usr/local/bin/python3

from pathlib import Path
import pyperclip
import sys

if len(sys.argv) > 2:
    f = Path(sys.argv[1])
    text = f.read_text()
else:
    text = pyperclip.paste()

text = text.replace('\n', '').split('.')

out = []
buffer = []

for x in text:
    if x.strip():
        out.append(f"- {x.strip()}.")


data = '\n'.join(out)
pyperclip.copy(data)

if len(sys.argv) > 2:
    ofile = Path(sys.argv[2])
    ofile.write_text(data)
print("done")
