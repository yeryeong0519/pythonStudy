import openpyxl
wb = openpyxl.load_workbook('./sample.xlsx')
sheet = wb['mlist']
for row in sheet.iter_rows(min_row = 2):
    for cell in row:
        print(cell.value)
        
wb.close()