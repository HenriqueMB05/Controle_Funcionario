from Controle_Funcionario.utils.ReadPdf import ReadPdf
from Controle_Funcionario.entities.UF import UF
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

    reader = ReadPdf("ficha.pdf")

    def find_UF(self, text: str):
        uf = UF
        part = [p.strip() for p in text]

        for p in part:
            try:
                return uf[p].name
            except KeyError:
                continue
        raise ValueError("UF NÃO ENCONTRADO")

    def find_address(self):
        part = self.reader.find_lines("Residência")
        if not part:
            return None
        match = re.search(r"\d{5}-?\d{3}", part)
        self.cep = match.group() if match else None
        address = part.split(",")
        public_space = address[0].split()
        self.public_space = ""
        for i, k in enumerate(public_space):
            if i == 0:
                self.type_public_space = k
            else:
                self.public_space += f"{k} "
        self.public_space.strip()
        self.district = address[3].strip()
        number = address[1].strip()
        self.number = number
        self.complement = address[2].strip()
        self.town = address[4].strip()
        self.uf = self.find_UF(address)
    




    def __repr__(self):
        return f"Cep:{self.cep}\nDistrict:{self.district}\nType:{self.type_public_space}\nPublic Space:{self.public_space}\nNumber:{self.number}\nComplement:{self.complement}\nTown:{self.town}\nUF:{self.uf}"






if __name__ == "__main__":

    add = Address()
    add.find_address()

    print(add)

