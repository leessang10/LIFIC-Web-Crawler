import time
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dir_xlsx = "C:\\Users\\leess\\Downloads\\lific.xlsx"
table_range = "A678:Z757"
table_range_start, table_range_end = table_range.split(":")

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
info_list = []
for row in table:
    try:
        time.sleep(3)
        store_num = row[1].value
        print(cnt, ": ", store_num)
        cnt += 1
        # 매장 전화번호 + 엔터키를 입력해서 매장 정보 검색
        input_search = driver.find_element_by_class_name("input_search")

        input_search.clear()
        input_search.send_keys(store_num + Keys.ENTER)
        time.sleep(3)

        # Iframe 전환
        driver.switch_to.frame("entryIframe")

        # 업체 정보 표의 class name: _6aUG7
        store = driver.find_element_by_class_name("_6aUG7")
        store_infos = store.find_elements_by_class_name("_1M_Iz")
        for store_info in store_infos:
            info = str(store_info.text).replace("\n", "_")
            if info.startswith("주소"):
                row[2].value = info
            elif info.startswith("영업시간"):
                store_info.click()
                row[3].value = str(store_info.text).replace("\n", "_")
            elif info.startswith("편의"):
                row[4].value = info
            elif info.startswith("설명"):
                row[5].value = info

    except:
        print("error")
    finally:
        # 원래 프레임으로 빠져 나오기
        driver.switch_to.default_content()
        load_wb.save("C:\\Users\\leess\\Downloads\\lific.xlsx")
