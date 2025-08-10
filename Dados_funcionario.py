from openpyxl import Workbook, load_workbook
import os

# O nome por enquanto será pré-definido depois o usúario será responsavel por passar um arquivo já existente ou criar um novo
path_file = "Controle_Funcionario.xlsx"

try:
    wb = load_workbook(path_file)
except FileNotFoundError:
    wb = Workbook()    
ws = wb.active

# Area do preenchimento da planilha

wb.save(path_file)