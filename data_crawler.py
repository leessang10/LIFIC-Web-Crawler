import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xpath


def main(driver, row):
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
        for row in rows:
            # 클릭 가능하면 다 눌러보기
            row_str = str(row.text)
            if row_str.startswith("홈페이지"):
                continue
            else:
                row..click()
                time.sleep(2)



        for row in rows:
            row_str2 = str(row.text)
            # 주소, 영업시간, 가격표, 편의, 설명
            if row_str2.startswith("주소"):
                infos.append(row_str2[2:])
            elif row_str2.startswith("영업시간"):
                infos.append(row_str2[4:])
            elif row_str2.startswith("가격 정보 수정 제안"):
                infos.append(row_str2[11:])
            elif row_str2.startswith("편의"):
                infos.append(row_str2[2:])
            elif row_str2.startswith("설명"):
                infos.append(row_str2[2:])
            elif row_str.startswith("홈페이지"):
                infos.append(row_str2[4:])
            time.sleep(2)

    except:
        print("data_cralwer 에러")
    finally:
        print(infos)
        return infos
