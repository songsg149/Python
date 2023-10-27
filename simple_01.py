import requests
from datetime import datetime, timedelta
import os
import pandas as pd

LOG_FOLDER = 'log'
TIMEOUT = timedelta(seconds=60)

def create_log_folder(log_folder):
    os.makedirs(log_folder, exist_ok=True)

def write_to_log(log_file_path, url, status, delay, df):
    timestamp = datetime.now().strftime("%m-%d %H:%M:%S")
    log_data = {'Timestamp': timestamp, 'URL': url, 'Status': status, 'Delay': delay}

    log_entry = pd.DataFrame([log_data])

    if os.path.exists(log_file_path):
        existing_df = pd.read_excel(log_file_path)
        df = pd.concat([existing_df, log_entry], ignore_index=True)
    else:
        df = log_entry

    df.to_excel(log_file_path, index=False)

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
    return False, TIMEOUT.total_seconds()

excel_file = 'urls.xlsx'
df = pd.read_excel(excel_file)
urls = df['url'].tolist()

for url in urls:
    status, delay = website_access_delay(url, TIMEOUT)
    current_time = datetime.now().strftime("%m-%d %H00")
    log_file_name = f"test_log_{current_time}.xlsx"
    log_file_path = os.path.join(LOG_FOLDER, log_file_name)

    if status is True:
        message = f"Website {url} 테스트 성공. 지연: {delay:.4f} 초\n"
    elif delay == TIMEOUT.total_seconds():
        message = f"Website {url} 에러: {TIMEOUT.total_seconds()} 초 후 타임아웃\n"
    else:
        message = f"Website {url} 다운됨. 응답 코드: {delay}\n"

    create_log_folder(LOG_FOLDER)
    write_to_log(log_file_path, url, status, delay, df)
    print(message)
