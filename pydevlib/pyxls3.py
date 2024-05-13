import openpyxl
wb = openpyxl.load_workbook('./sample.xlsx')
sheet = wb['mlist']
cells = sheet['A2':'C3']
for row in cells:
    for cell in row :
        print('-'*10)
        
wb.close()