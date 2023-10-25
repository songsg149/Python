import requests
from bs4 import BeautifulSoup

response = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%85%B8%EB%9E%98+%EC%88%9C%EC%9C%84&oquery=%EC%9B%94%EB%B3%84%EA%B0%9C%EB%B4%89%EC%98%81%ED%99%94&tqi=ig66qwprvh8ssLnzyS8ssssssGC-290273')

# #main_pack > section.sc_new.sp_pmusic._fe_music_collection > div > div.chart_list_wrap._sap_list > ul:nth-child(1) > li:nth-child(1) > div > div.detail_area > a > span


soup = BeautifulSoup(response.text, 'html.parser')

# Use the CSS selector to extract the desired content
css_selector = "#main_pack > section.sc_new.sp_pmusic._fe_music_collection > div > div.chart_list_wrap._sap_list > ul:nth-child(1) > li:nth-child(1) > div > div.detail_area > a > span"
second = "#main_pack > section.sc_new.sp_pmusic._fe_music_collection > div > div.chart_list_wrap._sap_list > ul:nth-child(1) > li:nth-child(2) > div > div.detail_area > a > span"
selected_element = soup.select_one(css_selector)
second_element = soup.select_one(second)
print(selected_element.get_text())
print(second_element.get_text())


