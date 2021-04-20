import time

from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.maximize_window()
url = "https://www.msgtong.com/pages/_3_area/area.php"
driver.get(url)
time.sleep(3)

load_wb = load_workbook("C:\\Users\\leess\\Downloads\\marong.xlsx")
load_ws = load_wb['Sheet1']
table = load_ws['A116':'AM149']
cnt = 1
for row in table:
    try:
        store_name = row[3].value
        print(cnt, ": ", store_name)
        cnt += 1

        search_bar = driver.find_element_by_id("publicLatestInput")
        search_bar.clear()
        search_bar.send_keys(store_name + Keys.ENTER)
        time.sleep(3)

        driver.find_element_by_class_name("shop-box").click()
        time.sleep(3)

        shop_detail_tab = driver.find_element_by_class_name("shop-detail-tab")
        tabs = shop_detail_tab.find_elements_by_tag_name("li")
        for tab in tabs:
            if tab.text == "업소정보":
                tab.click()

        time.sleep(2)

        shop_collapses = driver.find_elements_by_class_name("shop-collapse")

        for shop_collapse in shop_collapses:
            tit = shop_collapse.find_element_by_class_name("tit")
            if tit.text == "중국 가능한 코스":
                row[5].value = "TRUE"
                idx_cha = 14
                possible_courses = shop_collapse.find_elements_by_class_name("show")
                for possible_course in possible_courses:
                    #print("중국", possible_course.text)
                    if possible_course.text == "스포츠관리":
                        row[idx_cha].value = "TRUE"
                    elif possible_course.text == "아로마관리":
                        row[idx_cha+1].value = "TRUE"
                    elif possible_course.text == "발관리":
                        row[idx_cha+2].value = "TRUE"
                    elif possible_course.text == "커플관리":
                        row[idx_cha+3].value = "TRUE"
                    else:
                        row[idx_cha+4].value = "TRUE"

            elif tit.text == "태국 가능한 코스":
                row[6].value = "TRUE"
                idx_tai = 7
                possible_courses = shop_collapse.find_elements_by_class_name("show")
                for possible_course in possible_courses:
                    #print("태국", possible_course.text)
                    if possible_course.text == "타이관리":
                        row[idx_tai].value = "TRUE"
                    elif possible_course.text == "아로마관리":
                        row[idx_tai+1].value = "TRUE"
                    elif possible_course.text == "발관리":
                        row[idx_tai+2].value = "TRUE"
                    elif possible_course.text == "스웨디시관리":
                        row[idx_tai+3].value = "TRUE"
                    elif possible_course.text == "커플관리":
                        row[idx_tai+4].value = "TRUE"
                    elif possible_course.text == "스파관리":
                        row[idx_tai+5].value = "TRUE"
                    else:
                        row[idx_tai+6].value = "TRUE"

            elif tit.text == "한국 가능한 코스":
                row[4].value = "TRUE"
                idx_kor = 19
                possible_courses = shop_collapse.find_elements_by_class_name("show")
                for possible_course in possible_courses:
                    #print("한국", possible_course.text)
                    if possible_course.text == "건식관리":
                        row[idx_kor].value = "TRUE"
                    elif possible_course.text == "아로마관리":
                        row[idx_kor+1].value = "TRUE"
                    elif possible_course.text == "발관리":
                        row[idx_kor+2].value = "TRUE"
                    elif possible_course.text == "스웨디시관리":
                        row[idx_kor+3].value = "TRUE"
                    elif possible_course.text == "커플관리":
                        row[idx_kor+4].value = "TRUE"
                    elif possible_course.text == "지압관리":
                        row[idx_kor+5].value = "TRUE"
                    elif possible_course.text == "경락관리":
                        row[idx_kor+6].value = "TRUE"
                    elif possible_course.text == "교정관리":
                        row[idx_kor+7].value = "TRUE"
                    elif possible_course.text == "스파관리":
                        row[idx_kor+8].value = "TRUE"
                    else:
                        row[idx_kor].value = "TRUE"

            elif tit.text == "가능한 서비스":
                possible_services = shop_collapse.find_elements_by_class_name("icon")
                idx_srv = 29
                for possible_service in possible_services:
                    #print("서비스", possible_service.text)
                    if possible_service.text == "24시 영업":
                        row[idx_srv].value = "TRUE"
                    elif possible_service.text == "무료주차":
                        row[idx_srv+1].value = "TRUE"
                    elif possible_service.text == "조건부수면가능":
                        row[idx_srv+2].value = "TRUE"
                    elif possible_service.text == "커플실":
                        row[idx_srv+3].value = "TRUE"
                    elif possible_service.text == "단체실":
                        row[idx_srv+4].value = "TRUE"
                    elif possible_service.text == "와이파이":
                        row[idx_srv+5].value = "TRUE"
                    elif possible_service.text == "개인실":
                        row[idx_srv+6].value = "TRUE"
                    elif possible_service.text == "샤워가능":
                        row[idx_srv+7].value = "TRUE"
                    elif possible_service.text == "예약필수":
                        row[idx_srv+8].value = "TRUE"
                    elif possible_service.text == "남녀 화장실 구분":
                        row[idx_srv+9].value = "TRUE"
    except:
        print(store_name, "Error")
    finally:
        load_wb.save("C:\\Users\\leess\\Downloads\\marong.xlsx")