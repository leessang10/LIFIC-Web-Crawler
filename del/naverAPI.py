# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import json
import os
import sys
import urllib.request

from aiohttp.typedefs import JSONDecoder


def get_address(phone):
    client_id = "RfTq6_EAz3lROnZFROef"
    client_secret = "yOeoscBMw9"
    encText = urllib.parse.quote(phone)
    url = "https://openapi.naver.com/v1/search/local.json?query=" + encText # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()


    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)