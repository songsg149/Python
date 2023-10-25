import re
from playwright.sync_api import Page, expect
from datetime import datetime
import traceback
import os

# 폴더를 생성하는 함수
def create_log_folder(log_folder):
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

def test_crx(page: Page):
    try:
        page.goto("http://10.122.27.20:4503/crx/de/index.jsp")
        page.goto("http://10.122.27.21:4503/crx/de/index.jsp")
        page.goto("http://10.122.27.22:4503/crx/de/index.jsp")
        page.goto("http://10.122.27.23:4502/crx/de/index.jsp")
        page.goto("http://10.122.46.75/content/hyundai/fr/fr.html")
        page.goto("http://10.122.46.77/content/hyundai/fr/fr.html")
        page.goto("https://aem.hyundai.com/eu.html")
        page.goto(
            "https://author-aem.hyundai.com/libs/granite/core/content/login.html?resource=%2Faem%2Fstart.html&$$login$$=%24%24login%24%24&j_reason=unknown&j_reason_code=unknown")
        page.goto("https://org-eu-www.hyundai.com/eu.html")
        page.goto("https://www.hyundai.com/be/fr.html")
        page.goto("https://www.hyundai.com/be/nl.html")

        # 성공할 때 로그 남기기
        success_message = "테스트가 성공적으로 완료되었습니다."
        current_time = datetime.now().strftime("%m-%d %H%M")
        log_file_folder = r'..\test\log'
        create_log_folder(log_file_folder) # 폴더 생성 함수 호출
        log_file_name = f"../test/log/test_log_{current_time}.txt"
        log_file_path = os.path.join(log_file_folder, log_file_name)
        with open(log_file_name, "a", encoding="utf-8") as log_file:
            log_file.write(f"시간: {current_time}, {success_message}\n")

    except Exception as e:
        # 예외가 발생한 시간과 에러 메시지를 로그에 추가
        error_message = str(e)
        traceback_str = traceback.format_exc()  # 현재 예외의 traceback 정보를 문자열로 얻음
        current_time = datetime.now().strftime("%m-%d %H%M")
        log_file_folder = r'..\test\log'
        create_log_folder(log_file_folder) # 폴더 생성 함수 호출
        log_file_name = f"../test/log/test_log_{current_time}.txt"
        log_file_path = os.path.join(log_file_folder, log_file_name)
        with open(log_file_name, "a", encoding="utf-8") as log_file:
            log_file.write(f"시간: {current_time}, 에러 발생: {error_message}\n")
            log_file.write(f"Traceback:\n{traceback_str}\n")
