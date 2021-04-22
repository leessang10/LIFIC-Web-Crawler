import time
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# glance.py
# 검색하며 중간에 입력을 받음
# 동시작업할 때 사용한다
def get_store_info():
    section_info = driver.find_element_by_class_name("_6aUG7")
    infos = section_info.find_elements_by_class_name("_1M_Iz")
    for info in infos:
        info_str = str(info.text).replace("\n", "_")
        if info_str.startswith("설명"):
            info.click()
    for info in infos:
        info_str = str(info.text).replace("\n", "_")
        if info_str.startswith("설명"):
            print(info_str)


dir_xlsx = "C:\\Users\\leess\\Downloads\\lific.xlsx"
table_start = 1028
cnt = table_start
table_range_start = "A" + str(table_start)
table_range_end = "Z" + str(table_start+90)

load_wb = load_workbook(dir_xlsx)
load_ws = load_wb['Sheet1']
table = load_ws[table_range_start:table_range_end]

driver = webdriver.Chrome("C:\\chromedriver.exe")
# 네이버 지도의 URL 주소
URL = "https://map.naver.com/v5/"
# 접속 시도
driver.get(URL)
# 페이지 로드 완료 후 3초간 대기
driver.implicitly_wait(3)

cnt = 0
for row in table:
    try:
        # 업체 명, 업체 번호 출력
        store_name = row[0].value
        store_num = row[1].value
        print("==================================================")
        print(cnt, ":", store_name, store_num, sep=" ")
        cnt += 1

        # 매장 전화번호 + 엔터키를 입력해서 매장 정보 검색
        input_search = driver.find_element_by_class_name("input_search")
        input_search.clear()
        input_search.send_keys(store_num + Keys.ENTER)
        time.sleep(3)
        # 업체 정보가 나타내는 정보의 수준을 4단계로 구분하여 입력받음
        print("a. 가격 o\n"
              "b. 가격 x\n"
              "c. 정보 x")

        status = input()
        if status == 'a':
            row[5].value = "O"
        elif status == 'b':
            row[5].value = "상품정보 없음"
        elif status == 'c':
            row[5].value = "X"

        if status != 'c':
            # Iframe 전환
            driver.switch_to.frame("entryIframe")

            # 업체 정보 중 '소개'를 개행없이 출력
            get_store_info()

            # Iframe 전환
            driver.switch_to.default_content()
    except:
        print("error")
    finally:
        # 무조건 엑셀파일 저장
        load_wb.save("C:\\Users\\leess\\Downloads\\lific.xlsx")


