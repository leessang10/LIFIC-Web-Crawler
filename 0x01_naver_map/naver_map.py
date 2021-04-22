import time
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# raw_main.py의 리팩토링 버전
# GUI 만들 계획

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


def print_store(name, num):
    global cnt
    print(cnt, ":", name, num, sep=" ")
    cnt += 1

def search_store_info(num):
    input_search = driver.find_element_by_class_name("input_search")
    input_search.clear()
    input_search.send_keys(num + Keys.ENTER)
    time.sleep(3)

def click_info():
    section_info = driver.find_element_by_class_name("_6aUG7")
    infos = section_info.find_elements_by_class_name("_1M_Iz")
    for info in infos:
        info_str = str(info.text).replace("\n", "_")
        if info_str.startswith("영업시간"):
            info.click()

def get_store_info():
    section_info = driver.find_element_by_class_name("_6aUG7")
    infos = section_info.find_elements_by_class_name("_1M_Iz")
    for info in infos:
        info_str = str(info.text).replace("\n", "_")
        if info_str.startswith("주소"):
            row[2].value = info_str
        elif info_str.startswith("영업시간"):
            row[3].value = info_str
        elif info_str.startswith("편의"):
            row[4].value = info_str


for row in table:
    try:
        store_name = row[0].value
        store_num = row[1].value
        print_store(store_name, store_num)

        # 매장 전화번호 + 엔터키를 입력해서 매장 정보 검색
        search_store_info(store_num)

        # Iframe 전환
        driver.switch_to.frame("entryIframe")
        try:
            click_info()
        except:
            pass
        try:
            get_store_info()
        except:
            pass
    except:
        print("error")
    finally:
        # 원래 프레임으로 빠져 나오기
        driver.switch_to.default_content()
        load_wb.save("C:\\Users\\leess\\Downloads\\lific.xlsx")
