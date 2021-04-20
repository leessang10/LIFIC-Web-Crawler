import time
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dir_xlsx = "C:\\Users\\leess\\Downloads\\lific.xlsx"
table_range = "A838:AZ848"
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
        # Iframe 전환
        driver.switch_to.frame("entryIframe")
        # 업체 정보가 나타내는 정보의 수준을 4단계로 구분하여 입력받음
        print("A. 업체 정보에 있음\n"
              "B. 업체 홈페이지에 있음\n"
              "C. 소개글만 있음\n"
              "D. 최악임")
        
        status = input()
        row[5].value = status

        # 업체 정보 중 '간략한소개'을 개행없이 출력
        store_info = driver.find_element_by_class_name("_6aUG7")
        store_intro = store_info.find_element_by_class_name("_3__3i").click()
        intro = str(store_info.find_element_by_class_name("WoYOw").text)
        intro = intro.replace("\n", " ")
        print(intro)

        # Iframe 전환
        driver.switch_to.default_content()
    except:
        print("error")
    finally:
        # 무조건 엑셀파일 저장
        load_wb.save("C:\\Users\\leess\\Downloads\\lific.xlsx")


