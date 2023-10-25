import re
from playwright.sync_api import Page, expect
from datetime import datetime
import traceback
import os

try:
    # 폴더를 생성하는 함수
    def create_log_folder(log_folder):
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

    def crx(page: Page):

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

    def hyundai_be(page: Page):

        page.goto("https://www.hyundai.com/be/fr.html")
        page.goto("https://www.hyundai.com/be/nl.html")

    def hyundai_ch(page: Page):
        # Click the get started link.
        page.goto("https://www.hyundai.com/ch/de.html")
        page.goto("https://www.hyundai.com/ch/de/modelle/all-new-kona-electric/konfigurator.html#/trims")
        page.goto("https://www.hyundai.com/ch/de/vertriebsnetz-schweiz.html")
        page.goto("https://www.hyundai.com/ch/fr.html")
        page.goto("https://www.hyundai.com/ch/fr/modeles/all-new-kona-electric/configurator.html#/trims")
        page.goto("https://www.hyundai.com/ch/fr/reseau-suisse.html")
        page.goto("https://www.hyundai.com/ch/it.html")
        page.goto("https://www.hyundai.com/ch/it/modelli/all-new-kona-electric/konfigurator.html#/trims")
        page.goto("https://www.hyundai.com/ch/it/rete-svizzera.html")

    def hyundai_cz(page: Page):

        page.goto("https://www.hyundai.com/cz/cz.html")
        page.goto("https://www.hyundai.com/cz/modely.html")
        page.goto("https://www.hyundai.com/cz/modely/bayon/konfigurator.html#/trims")

    def hyundai_de(page: Page):

        page.goto("https://www.hyundai.com/de/de.html")
        page.goto("https://www.hyundai.com/de/de/beratung-kauf/entdecken-und-erwerben/angebot.html")
        page.goto("https://www.hyundai.com/de/de/beratung-kauf/entdecken-und-erwerben/haendlersuche.html")
        page.goto("https://www.hyundai.com/de/de/beratung-kauf/entdecken-und-erwerben/probefahrt.html")
        page.goto("https://www.hyundai.com/de/de/hyundai-welt/sponsoring-und-events/eintracht.html")
        page.goto("https://www.hyundai.com/de/de/hyundai-welt/sponsoring-und-events/eintracht/eintracht-deals.html")
        page.goto("https://www.hyundai.com/de/de/hyundai-welt/sponsoring-und-events/eintracht/sge-moments.html")
        page.goto("https://www.hyundai.com/de/de/konfigurator/")
        page.goto("https://www.hyundai.com/de/de/modelle.html")
        page.goto("https://www.hyundai.com/de/de/newsletter.html")

    def hyundai_es(page: Page):

        page.goto("https://www.hyundai.com/es.html")
        page.goto("https://www.hyundai.com/es/modelos/kona-electrico-2021/configuracion.html#/powertrain")

    def hyundai_fr(page: Page):

        page.goto("https://www.hyundai.com/fr/fr.html")
        page.goto("https://www.hyundai.com/fr/fr/modeles/ioniq5/configurateur.html#/trims")

    def hyundai_it(page: Page):

        page.goto("https://www.hyundai.com/it.html")
        page.goto("https://www.hyundai.com/it/models/nuova-ioniq-5/configuratore.html#/trims")

    def hyundai_nl(page: Page):

        page.goto("https://www.hyundai.com/nl/nl.html")
        page.goto("https://www.hyundai.com/nl/nl/dealers.html")
        page.goto("https://www.hyundai.com/nl/nl/modellen/kona-electric/configurator.html#/trims")

    def hyundai_pl(page: Page):

        page.goto("https://www.hyundai.com/pl/pl.html")
        page.goto("https://www.hyundai.com/pl/pl/modele/ioniq5.html")
        page.goto("https://www.hyundai.com/pl/pl/modele/tucson/konfigurator.html#/trims")

    def hyundai_sk(page: Page):

        page.goto("https://www.hyundai.com/sk/sk.html")
        page.goto("https://www.hyundai.com/sk/sk/modely/kona-hybrid/konfigurator.html#/trims")
        page.goto("https://www.hyundai.com/sk/sk/modely/nova-i10/konfigurator.html#/trims")
        page.goto("https://www.hyundai.com/sk/sk/modely/nova-i20/konfigurator.html#/trims")
        page.goto("https://www.hyundai.com/sk/sk/predaj/kontakty/autorizovane-predajne.html")
        page.goto("https://www.hyundai.com/sk/sk/predaj/predaj/konfigurator.html")
        page.goto("https://www.hyundai.com/sk/sk/sluzby/online-sluzby/cenova-ponuka.html")
        page.goto("https://www.hyundai.com/sk/sk/sluzby/online-sluzby/testovacia-jazda.html")

    def hyundai_uk(page: Page):

        page.goto("https://www.hyundai.com/uk/en.html")
        page.goto("https://www.hyundai.com/uk/en/choose-model.html")
        page.goto("https://www.hyundai.com/uk/en/models/all-new-kona/configurator.html#/trims")
        page.goto("https://www.hyundai.com/uk/en/models/all-new-kona-hybrid/configurator.html#/trims")
        page.goto("https://www.hyundai.com/uk/en/models/ioniq5/configurator.html#/trims")
        page.goto("https://www.hyundai.com/uk/en/models/ioniq6/configurator.html#/trims")
        page.goto("https://www.hyundai.com/uk/en/models/kona-electric/configurator.html#/trims")
        page.goto("https://www.hyundai.com/uk/en/offers/new-cars/model.html")

    def hyundai_etc(page: Page):

        page.goto("https://www.hyundai.com/eu.html")
        page.goto("https://www.hyundai.com/lu.html")
        page.goto("https://www.hyundai.com/no/no.html")
        page.goto("https://www.hyundai.news/eu.html")
        page.goto("https://hap.hyundai-europe.com/login/loginPage")

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
