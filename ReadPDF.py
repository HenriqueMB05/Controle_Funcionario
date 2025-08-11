import pdfplumber as pp

path = "ficha.pdf"
empregado = []
data = ["Empregado ", "Data de nascimento", "sexo", "Residência"]
# Verifica se o nome está na lista, retorna o indíce da linha
def find_line(name):
    for i, k in enumerate(lines):
        if name in k:
            return lines[i+1]
def fmtData(lista):
    for i, k in enumerate(data):
        match(k):
            case "Empregado ":
                lista.append(k)
            case "Data de nascimento":
                date = find_line(k).split(" ")
                lista.append(date[0])
            case "Residência":
                # Divide por virgula para pegar todos os elemento rua, bairro e etc...
                address = find_line(k).split(",")
                lista.append(address[-3])
                
                # Precisa do tipo de lougradouro, como rua, avenida, viela
                # Por isso tem que fatiar a string novamente
                address_name = address[0].split(" ")
                lista.append(address_name[0])
                lista.append(" ".join(address_name[1:]).strip())
                try:
                    num = int(address[1])
                    lista.append(num)

                except ValueError:
                    lista.append(" ")

                
    return lista             
""" def EmpData(lista):
    for i, k in enumerate(data):    
        if k in "sexo":
            lista.append("M")
        lista.append(fmtData(k))
    # Por algum motivo ainda adiciona um item None no fim da lista
    lista.pop()
    return lista """

# Abre o arquivo pdf e transforma todo o pdf em texto
with pp.open(path) as pdf:
    txt = ""
    for page in pdf.pages:
        txt += page.extract_text()+'\n'

lines = txt.splitlines()

fmtData(empregado)

for i, k in enumerate(empregado):
    print(k)

