from msilib.schema import Property
import openpyxl


book = openpyxl.load_workbook('C:/Users/SK8/documents/programas/notifierToMakeCall/toCallNotifier/BOOK.xlsx')
sheet = book.active
yellow = sheet['F4']
blank = sheet['H2']

def getRGB(cell):
    properties = str(cell.fill).split()
    rgbs = filter(lambda x: 'rgb' in x, properties)
    rgb = list(rgbs)[0]
    hex = rgb[5: -2]
    return hex


print(getRGB(yellow))
print(getRGB(blank))
