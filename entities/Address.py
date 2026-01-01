from Controle_Funcionario.utils.ReadPdf import ReadPdf
from Controle_Funcionario.entities.UF import UF
from Controle_Funcionario.entities.Public_Space import Public_Space
from dataclasses import dataclass
from typing import Optional, Final
import re




@dataclass
class Address:
    cep: str = ""
    district: Optional[str] = None
    type_public_space: str = ""
    public_space: str = ""
    number: Optional[str] = None
    complement: Optional[str] = None
    town: str = ""
    uf: Optional[UF] =  None

    complement_key = ("CASA", "CS", "QD", "LT","ST", "AP","APT", "APTO")


    reader = ReadPdf("ficha.pdf")

    def find_number(self, key: str):
        if not key:
            return None
        
        key = [k.strip() for k in key]
        
        for k in key:
            if k.isdigit():
                return k
        return None
    

    def find_complement(self, key:str):
        if not key:
            return None
        
        key = [k.strip() for k in key]

        for p in key:
            p.upper()
            for k in self.complement_key:
                if p.startswith(k):
                    return p
            
        return None
        

    def find_UF(self, key: str):
        uf = UF

        key = [k.strip() for k in key]

        for k in key:
            try:
                return uf[k].name
            except KeyError:
                continue
        raise ValueError("UF NÃO ENCONTRADO")


    def find_public_space(self, key: str):
        PS = Public_Space
        key = key[0].split()
        key = [k.upper() for k in key]
        var = ""

        for k in key:
            for j in key:
                if j not in PS:
                    var += j+" "
            return PS[k.upper()].value, var.strip()
        
        return None


    def find_address(self):
        part = self.reader.find_lines("Residência")
        if not part:
            return None
        match = re.search(r"\d{5}-?\d{3}", part)
        self.cep = match.group() if match else None
        address = part.split(",")
        self.type_public_space, self.public_space = self.find_public_space(address)
        self.district = address[3].strip()
        self.number = self.find_number(address)
        self.complement = self.find_complement(address)
        self.town = address[4].strip()
        self.uf = self.find_UF(address)
    




    def __repr__(self):
        return f"Cep:{self.cep}\nDistrict:{self.district}\nType:{self.type_public_space}\nPublic Space:{self.public_space}\nNumber:{self.number}\nComplement:{self.complement}\nTown:{self.town}\nUF:{self.uf}"






if __name__ == "__main__":

    add = Address()
    add.find_address()

    print(add)

