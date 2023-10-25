import re
from playwright.sync_api import Page, expect
from datetime import datetime
import traceback
import os

# 폴더를 생성하는 함수
def create_log_folder(log_folder):
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

def test_06(page: Page):
    try:
        page.goto("https://www.hyundai.com/fr/fr.html")
        page.goto("https://www.hyundai.com/fr/fr/modeles/ioniq5/configurateur.html#/trims")

        # 성공할 때 로그 남기기
        success_message = "테스트가 성공적으로 완료되었습니다."
        current_time = datetime.now().strftime("%m-%d %H%M")
        log_file_folder = r'..\test\log'
        create_log_folder(log_file_folder)  # 폴더 생성 함수 호출
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
        create_log_folder(log_file_folder)  # 폴더 생성 함수 호출
        log_file_name = f"../test/log/test_log_{current_time}.txt"
        log_file_path = os.path.join(log_file_folder, log_file_name)
        with open(log_file_name, "a", encoding="utf-8") as log_file:
            log_file.write(f"시간: {current_time}, 에러 발생: {error_message}\n")
            log_file.write(f"Traceback:\n{traceback_str}\n")
