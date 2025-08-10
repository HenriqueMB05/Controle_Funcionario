import pdfplumber as pp

path = "ficha.pdf"

# Verifica se o nome está na lista, retorna o indíce da linha
def find_line(name):
    for i, k in enumerate(lines):
        print(i, k)
        if name in lines:
            return i

# Abre o arquivo pdf e transforma todo o pdf em texto
with pp.open(path) as pdf:
    txt = ""
    for page in pdf.pages:
        txt += page.extract_text()+'\n'

lines = txt.splitlines()
#line_number = find_line(keyWord)
print(lines[18])