import time

from openpyxl import load_workbook
from selenium import webdriver

driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.maximize_window()
url = "https://www.msgtong.com/pages/_3_area/area.php"
driver.get(url)
time.sleep(3)
driver.find_element_by_class_name("course7").click()

# search_areas = "강남구", "강동구", "강북구", "강서구", "관악구", \
#              "광진구", "구로구", "금천구", "노원구", "도봉구", \
#              "동대문구", "동작구", "마포구", "서대문구", "서초구", \
#              "성동구", "성북구", "송파구", "양천구", "영등포구", \
#              "용산구", "은평구", "종로구", "중구", "중랑구"

search_areas = "남구", "달서구", "달성군", "동구", "북구", "서구", "수성구", "중구"


def scroll_down_max():
    prev_height = driver.execute_script("return document.body.scrollHeight")
    # 웹페이지 맨 아래까지 무한 스크롤
    while True:
        # 스크롤을 화면 가장 아래로 내린다
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # 페이지 로딩 대기
        time.sleep(2)
        # 현재 문서 높이를 가져와서 저장
        curr_height = driver.execute_script("return document.body.scrollHeight")
        if curr_height == prev_height:
            break
        else:
            prev_height = driver.execute_script("return document.body.scrollHeight")

def area_select(search_area):
    city = "대구"

    driver.find_element_by_id("areaZone").click()
    area1_list = driver.find_element_by_id("area_1")
    area1s = area1_list.find_elements_by_tag_name("a")
    for area1 in area1s:
        if area1.text == city:
            area1.click()

    area2_list = driver.find_element_by_id("area_2")
    area2s = area2_list.find_elements_by_tag_name("a")
    for area2 in area2s:
        if area2.text == search_area:
            area2.click()

def search_store_info():
    scroll_down_max()
    another_list = driver.find_element_by_id("anotherlist")
    adds = another_list.find_elements_by_class_name("add")
    for add in adds:
        store_name = add.find_element_by_class_name("tit").text
        store_address = add.find_element_by_class_name("address").text
        store_kind = add.find_element_by_class_name("shop-top-type").text
        print(store_kind, "_", store_address, "_", store_name)


for search_area in search_areas:
    print(search_area, "검색 결과")
    area_select(search_area)
    search_store_info()

