from openpyxl import load_workbook

load_wb = load_workbook("C:\\Users\\leess\\Downloads\\lific.xlsx")
load_ws = load_wb['Sheet1']
table = load_ws['A1':'F1383']
# row[0]: 업체 명
# row[1]: 업체 전화번호
# row[2]: 업체 주소
# row[3]: 영업시간
# row[4]: 특이사항
# row[5]: 간략 소개

for row in table:
