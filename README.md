# LIFIC-Web-Crawler
LIFIC DB 데이터 크롤링 작업을 자동화

0x01. naver_map: **네이버지도**의 업체정보를 가져옴
  1. raw_main.py: 가장 처음 만든 프로그램. 구현, 동작되지만 모듈화가 안되어있음
  2. naver_map.py: raw_main.py를 리팩토링하기 위한 py파일
  3. glance.py: 기존 비동기적인 일괄처리 방식에서 동기적인 방식으로 수정함. 프로그램 실행 과정 도중 수작업을 할 수 있음

0x02. matong: **마통**에서 업체 정보를 가져옴
  1. matong_get_store_list.py: 지역별 업체 리스트를 출력
  2. matong_get_store_info.py: 엑셀의 업체 리스트를 순회하며 업체 정보를 검색 후 필요한 정보를 가져옴

0x10. del: 휴지통

0x11. test: 구현 테스트용 폴더
