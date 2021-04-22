import time
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

dir_xlsx = "C:\\Users\\leess\\Downloads\\dagym.xlsx"
table_range = "A1:AZ1300"
table_range_start, table_range_end = table_range.split(":")

load_wb = load_workbook(dir_xlsx)
load_ws = load_wb['Sheet1']
table = load_ws[table_range_start:table_range_end]

driver = webdriver.Chrome("C:\\chromedriver.exe")
# 네이버 지도의 URL 주소
URL = "https://www.da-gym.co.kr/dagym-list"
# 접속 시도
driver.get(URL)
# 페이지 로드 완료 후 3초간 대기
driver.implicitly_wait(3)
scroll_down_max()
cnt = 0
gym_names = driver.find_elements_by_class_name("gym-name")
for gym_name in gym_names:
    print(gym_name.text)



load_wb.save("C:\\Users\\leess\\Downloads\\dagym.xlsx")


