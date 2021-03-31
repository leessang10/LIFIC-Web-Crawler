from selenium import webdriver
from openpyxl import load_workbook
from selenium.webdriver.common.keys import Keys

import xpath

global driver


class GetInfo:
    def store_info(self):
        # 매장 전화번호 + 엔터키를 입력해서 매장 정보 검색
        driver.find_element_by_class_name("input_search").send_keys(store["phone"] + Keys.ENTER)
        # 검색 결과 로드하고 3초간 대기
        driver.implicitly_wait(3)

    def phone(self):
        # 네이버 안전 전화번호 추출
        store["phone_naver"] = driver.find_element_by_xpath(xpath.phone_naver).text
        # 업체 전화번호 상세정보 아이콘 클릭
        driver.find_element_by_xpath(xpath.phone_icon).click()
        # 업체 일반 전화번호 추출
        store["phone_origin"] = driver.find_element_by_xpath(xpath.phone_origin).text

    def address(self):
        # 업체 도로명 주소 추출
        store["address"] = driver.find_element_by_xpath(xpath.address).text

    def opening_hours(self):
        # 업체 영업 시간 클릭해서 상세 정보 확인
        driver.find_element_by_xpath(xpath.opening_click).click()
        # 업체 영업 시간 추출
        store["opening_hours"] = driver.find_element_by_xpath(xpath.opening_hours).text

    def feature(self):
        # 업체 특이사항 추출
        store["feature"] = driver.find_element_by_xpath(xpath.feature).text

    def intro(self):
        # 업체 간단소개글 추출
        store["intro"] = driver.find_element_by_xpath(xpath.intro).text


def open_web_page():
    # web driver 설정
    chrome_driver = "C:\\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver)
    # 네이버 지도의 URL 주소
    URL = "https://map.naver.com/v5/"
    # 접속 시도
    driver.get(URL)
    # 페이지 로드 완료 후 3초간 대기
    driver.implicitly_wait(3)


#매장 정보
store = {
    "phone": "",
    "phone_naver": "",
    "phone_origin": "",
    "address": "",
    "opening_hours": "",
    "feature": "",
    "intro": ""
}

# 매장 정보 엑셀 파일의 경로
xlsx = ""



open_web_page()

GetInfo.store_info()

GetInfo.phone()

GetInfo.address()

GetInfo.opening_hours()

GetInfo.feature()

GetInfo.intro()

print(store)