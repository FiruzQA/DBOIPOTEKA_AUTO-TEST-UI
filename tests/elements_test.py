import time
from pages.elements_page import LogInPage
from pages.elements_page import SmartTransferUzCardIpoteka


class TestElements:
    class TestLogIn:

        def test_log_in(self, driver):
            log_in_page = LogInPage(driver, 'http://192.168.70.50:9090/lite/')
            log_in_page.open()
            log_in_page.login_to_account()
            time.sleep(5)

    class TestSmartTransfer:

        def test_uz_card_ipoteka_to_uz_card_other(self, driver):
            smart_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            smart_transfer.open()
            smart_transfer.between_uz_card_ipoteka_to_uz_card_other()
            time.sleep(5)

        def test_uz_card_ipoteka_to_humo_ipoteka(self, driver):
            smart_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            smart_transfer.open()
            smart_transfer.between_uz_card_ipoteka_to_humo_ipoteka()
            time.sleep(5)

        def test_humo_ipoteka_to_uz_card_ipoteka(self, driver):
            smart_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            smart_transfer.open()
            smart_transfer.between_humo_ipoteka_to_uz_card_ipoteka()
            time.sleep(10)
