from openpyxl import Workbook

wb = Workbook()
ws = wb.active

excelHeader = ["A1", "B1", "C1", "D1", "E1"]
excelHeaderName = ["userName", "name", "email", "phoneNumber", "country"]
for i in range(len(excelHeader)):
    ws[excelHeader[i]] = excelHeaderName[i]
    print(excelHeader[i] + " = " + excelHeaderName[i])

wb.save("DataFile.xlsx")
