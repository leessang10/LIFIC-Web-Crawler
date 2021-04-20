import time

from openpyxl import load_workbook
from selenium import webdriver

from test import data_crawler

# 엑셀 불러오기
load_wb = load_workbook("C:\\Users\\leess\\Downloads\\lific.xlsx")
load_ws = load_wb['Sheet1']
table = load_ws['A82':'AZ162']

driver = webdriver.Chrome("C:\\chromedriver.exe")
# 네이버 지도의 URL 주소
URL = "https://map.naver.com/v5/"
# 접속 시도
driver.get(URL)
# 페이지 로드 완료 후 3초간 대기
driver.implicitly_wait(3)

cnt = 0
info_list = []
for row in table:
    time.sleep(3)
    print("#", cnt, "#", row[1].value)
    info_list = data_crawler.main(driver, row)
    # 원래 프레임으로 빠져 나오기
    driver.switch_to.default_content()
    for i in range(len(info_list)):
        row[2 + i].value = info_list[i]

    info_list.clear()
    load_wb.save("C:\\Users\\leess\\Downloads\\lific.xlsx")
    cnt += 1