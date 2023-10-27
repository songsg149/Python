import requests
from datetime import datetime, timedelta
import os

LOG_FOLDER = r'log' # 현재 위치 폴더에 로그폴더를 생성하기
TIMEOUT = timedelta(seconds=60)

def create_log_folder(log_folder):
    os.makedirs(log_folder, exist_ok=True)

def write_to_log(log_file_path, message):
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(message)

def website_health_check(url):
    try:
        response = requests.get(url)
        return True if response.status_code == 200 else response.status_code
    except requests.exceptions.RequestException as e:
        return e

def website_access_delay(url, timeout):
    start_time = datetime.now()
    while datetime.now() - start_time < timeout:
        status = website_health_check(url)
        if status is True:
            end_time = datetime.now()
            return True, (end_time - start_time).total_seconds()
    return False, None

with open("urls.txt", "r") as file:
    urls = file.read().splitlines()

for url in urls:
    status, delay = website_access_delay(url, TIMEOUT)
    current_time = datetime.now().strftime("%m-%d %H00")
    log_file_name = f"test_log_{current_time}.txt"
    log_file_path = os.path.join(LOG_FOLDER, log_file_name)

    if status is True:
        message = f"{url} 테스트 성공. 지연: {delay:.4f} 초\n"
    elif delay is None:
        message = f"{url} 에러: {TIMEOUT.total_seconds()} 초 후 타임아웃\n"
    else:
        message = f"{url} 다운됨. 응답 코드: {delay}\n"

    create_log_folder(LOG_FOLDER)
    write_to_log(log_file_path, message)
    print(message)
