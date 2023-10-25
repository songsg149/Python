# # import subprocess
# #
# # test = "World!"
# # # 문자열 포맷팅을 사용하여 변수 test를 적용
# # subprocess.run(['python', '-c', f'print("{test}")'])
# #
# # 동현
# import new1 from new
#
# 신규함수()
#
# my_function

# main_script.py

from test_01 import crx, create_log_folder
from playwright.sync_api import sync_playwright

# Playwright 초기화 및 페이지 생성
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    try:
        # crx 함수 호출
        crx(page)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # 브라우저 종료
        browser.close()