from msilib.schema import Property
import openpyxl


book = openpyxl.load_workbook('C:/Users/SK8/Documents/programas/notifierToMakeCall/NotifierToMakeCall/VACUNAS Y DESPARASITANTES ACTUAL2.0.xlsx')
sheet = book.active
conNegr = sheet['B4']
sinNegr = sheet['C4']
red = sheet['F10']
cel = sheet['F8']

def backgroundRGB(cell) -> str:
    properties = str(cell.fill).split()
    rgbs = filter(lambda x: 'rgb' in x, properties)
    rgb = list(rgbs)[0]
    hex = rgb[5: -2]
    return hex


def letterRGB(cell) -> str:
    #cell.value = str(cell.value)
    return str(cell.font.color.rgb)


cells = ['F'+str(i) for i in range(589, 613)]
print(cabecera := 'letter \t type \t background \t content')
    # 
for cell in cells:
    print('-'*len(cabecera))
    print(cell, end='\t')
    cell = sheet[cell]
    print(letterRGB(cell), '\t', type(cell.value), '\t', backgroundRGB(cell), '\t', cell.value)

