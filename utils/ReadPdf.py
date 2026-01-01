import pdfplumber as pdf
from typing import Optional

class ReadPdf:
    def __init__(self, path):
        self.lines =""
        self.path = path
        #self.parts: Optional[str] = None
        self.parts = ""


    def read(self):
        with pdf.open(self.path) as file:
            for page in file.pages:
                self.lines += page.extract_text()
        return self.lines
    
    # Dependendo do dado é preciso saber se a função vai pular ou não uma linha

    def find_lines(self, key: str):
        self.read()
        lines = self.lines.splitlines()
        for i, line in enumerate(lines):
            if key.lower() == "residência" and key.lower()  in line.lower():
              self.parts = lines[i+1]+" "+lines[i+2]
              self.parts.split(",")
              return  self.parts
            elif key.lower() in line.lower():
                return lines[i+1]
        return None


# Area do debug
if __name__ == "__main__":
    reader = ReadPdf("ficha.pdf")

    print(reader.find_lines("Residência"))

