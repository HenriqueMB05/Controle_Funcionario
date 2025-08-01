import os
from concurrent.futures import ThreadPoolExecutor, as_completed

def find(name):
    root = "c:\\users\\matos"


    for pasta_atual, subpasta, arquivos in os.walk(root, topdown=True):
        subpasta[:] = [p for p in subpasta if not p.startswith("$") and "windows" not in p and "system" not in p and not p.startswith('.')]
        if name in arquivos:
            caminho =os.path.join(pasta_atual, name)
            return caminho
    return None

d
if __name__ == '__main__':
    print(find("dados_contatos_sem_parenteses.txt"))