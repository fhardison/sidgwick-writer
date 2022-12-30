from pathlib import Path
import pyperclip
import sys

f = Path(sys.argv[1])

text = f.read_text().replace('\n', '').split('.')

out = []
buffer = []

for x in text:
    if x.strip():
        out.append(f"- {x.strip()}.")
    # if len(buffer) < 2:
    #     buffer.append(x.strip() + '.')
    # else:
    #     out.append(f'| {" | ".join(buffer)} |')
    #     buffer = [x.strip() + '.']

# out.append(f'| {" | ".join(buffer)} |')

ofile = Path(sys.argv[2])

data = '\n'.join(out)
# ofile.write_text(f"""| | |
# |:--|:--|
# {data}
# """)
pyperclip.copy(data)
ofile.write_text(data)
print("done")
