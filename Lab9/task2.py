from openpyxl import load_workbook

path = "table.xlsx"
wb_obj = load_workbook(path)
sheet_obj = wb_obj.active

sheet_obj["B14"] = "Максимальная з/п"
sheet_obj["B15"] = "Минимальная з/п"
sheet_obj["B16"] = "Средняя з/п от-ов по порядку:"

max_pay = sheet_obj[2][5].value
min_pay = sheet_obj[2][5].value
index_max = 2
index_min = 2

department_sum = 0
sums = []

for i in range(2, 11):
    if(i != 4 and i != 9):
        department_sum += sheet_obj[i][5].value
        if max_pay < sheet_obj[i][5].value:
            index_max = i
            max_pay = sheet_obj[i][5].value
        if min_pay > sheet_obj[i][5].value:
            index_min = i
            min_pay = sheet_obj[i][5].value
    else:
        sums.append(department_sum)
        department_sum = 0
sums.append(department_sum)
department_sum = 0

name_max = sheet_obj[index_max][1].value
name_min = sheet_obj[index_min][1].value

sums[0] /= 2
sums[1] /= 4
sums[2] /= 1

sheet_obj["C14"] = f"{name_max} - {max_pay}"
sheet_obj["C15"] = f"{name_min} - {min_pay}"
sheet_obj["C16"] = f"{sums[0]}, {sums[1]}, {sums[2]}"

wb_obj.save("table.xlsx")