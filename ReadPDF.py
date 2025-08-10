import pdfplumber as pp

path = "ficha.pdf"

data = ["Empregado ", "Data de nascimento", " ",]
# Verifica se o nome está na lista, retorna o indíce da linha
def find_line(name):
    for i, k in enumerate(lines):
        if name in k:
            return lines[i+1]

def EmpData(lista):
    for i, k in enumerate(data):    
        if k is not " ":
            lista.append(find_line(k))
        lista.append("M")
    return lista

# Abre o arquivo pdf e transforma todo o pdf em texto
with pp.open(path) as pdf:
    txt = ""
    for page in pdf.pages:
        txt += page.extract_text()+'\n'
lines = txt.splitlines()
