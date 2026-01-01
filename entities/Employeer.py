from Controle_Funcionario.utils.ReadPdf import ReadPdf
from Controle_Funcionario.entities.Address import Address
from dataclasses import dataclass
from typing import Optional, Final
import re


@dataclass
class Employeer:
    name: Optional[str] = None
    birth: Optional[str] = None
    sexo: Optional[str] = None
    cpf: Optional[str] = None
    address: Optional[Address] = None
    reader = ReadPdf("ficha.pdf")


        
    def employeer_data(self):
        self.name = self.reader.find_lines("Empregado ")
        birth = self.reader.find_lines("Data de nascimento")
        birth = re.search(r"\d{2}/?\d{2}/?\d{4}", birth)
        self.birth = birth.group() if birth else None
        sex = self.reader.find_lines("Sexo").split()
        if "Masculino" in sex:
            self.sexo = "M"
        elif "Feminino" in sex:
            self.sexo = "F"
        # address = Address()
        self.address = Address()
        self.address.find_address()
        
        
    def find_cpf(self):
        cpf = ""
        line = self.reader.find_lines("CPF").split(" ")
        for i, k in enumerate(line):
            if i<2:
                cpf += k
        self.cpf = cpf

emp = Employeer()
emp.employeer_data()

print(emp.address.cep)
