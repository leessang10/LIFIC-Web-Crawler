import time
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 엑셀 불러오기
load_wb = load_workbook("C:\\Users\\leess\\Downloads\\lific.xlsx")
load_ws = load_wb['Sheet1']
table = load_ws['A758':'AZ837']

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
    print(cnt, ": ", row[1].value)
    cnt += 1
    # 매장 전화번호 + 엔터키를 입력해서 매장 정보 검색
    driver.find_element_by_class_name("input_search").clear()
    driver.find_element_by_class_name("input_search").send_keys(row[1].value + Keys.ENTER)
    time.sleep(3)
    # 업체 주소, 운영시간, 가격표, 특이사항, 간단소개
    infos = []
    try:
        # Iframe 전환
        driver.switch_to.frame("entryIframe")

        # 업체 정보 표의 class name: _6aUG7
        info = driver.find_element_by_class_name("_6aUG7")

        rows = info.find_elements_by_class_name("_1M_Iz")

        for row1 in rows:
            row_str = str(row1.text)
            if row_str.startswith("영업시간"):
                row1.click()

        time.sleep(2)

        for row2 in rows:
            row_str2 = str(row2.text)
            # 주소, 영업시간, 가격표, 편의, 설명
            if row_str2.startswith("주소"):
                infos.append(row_str2[2:])
            elif row_str2.startswith("영업시간"):
                infos.append(row_str2[4:])
            elif row_str2.startswith("편의"):
                infos.append(row_str2[2:])

    except:
        infos.clear()
        infos.append("error")
    finally:
        # 원래 프레임으로 빠져 나오기
        driver.switch_to.default_content()
        print(infos)
        info_list = infos
        for i in range(len(info_list)):
            row[2 + i].value = info_list[i]
        load_wb.save("C:\\Users\\leess\\Downloads\\lific.xlsx")
        cnt += 1