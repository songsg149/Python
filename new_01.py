import requests
from datetime import datetime
import time
import os
import pandas as pd

LOG_FOLDER = r'..\test\log'
TIMEOUT = 60

def create_log_folder(log_folder):
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

def write_to_log(log_file_path, message):
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(message)

def website_health_check(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return response.status_code
    except requests.exceptions.RequestException as e:
        return e

def website_access_delay(url, timeout):
    start_time = time.time()
    while time.time() - start_time < timeout:
        status = website_health_check(url)
        if status is True:
            end_time = time.time()
            return (True, end_time - start_time)
        time.sleep(1)
    return (False, None)

excel_file = 'urls.xlsx'
df = pd.read_excel(excel_file)
urls = df['url'].tolist()

for url in urls:
    status, delay = website_access_delay(url, TIMEOUT)
    current_time = datetime.now().strftime("%m-%d %H00")
    log_file_name = f"test_log_{current_time}.txt"
    log_file_path = os.path.join(LOG_FOLDER, log_file_name)

    if status is True:
        message = f"Website {url} 테스트 성공. 지연: {delay:.4f} 초\n"
    elif delay is None:
        message = f"Website {url} 에러: {TIMEOUT} 초 후 타임아웃\n"
    else:
        message = f"Website {url} 다운됨. 응답 코드: {delay}\n"

    create_log_folder(LOG_FOLDER)
    write_to_log(log_file_path, message)
    print(message)  # 실시간 피드백을 위해 콘솔에 출력

