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

# перевод между своими счетами UZCARD(Ipoteka)

        def test_uz_card_ipoteka_to_uz_card_other(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_uz_card_ipoteka_to_uz_card_other()
            time.sleep(5)

        def test_uz_card_ipoteka_to_humo_ipoteka(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_uz_card_ipoteka_to_humo_ipoteka()
            time.sleep(5)

        def test_uz_card_ipoteka_to_humo_other(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_uz_card_ipoteka_to_humo_other()
            time.sleep(5)

        def test_uz_card_ipoteka_to_my_wallet(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_uz_card_ipoteka_to_my_wallet()
            time.sleep(5)

# перевод между своими счетами HUMO(Ipoteka)

        def test_humo_ipoteka_to_uz_card_ipoteka(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_humo_ipoteka_to_uz_card_ipoteka()
            time.sleep(5)

        def test_humo_ipoteka_to_uz_card_other(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_humo_ipoteka_to_uz_card_other()
            time.sleep(5)

        def test_humo_ipoteka_to_humo_other(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_humo_ipoteka_to_humo_other()
            time.sleep(5)

        def test_humo_ipoteka_to_my_wallet(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_humo_ipoteka_to_my_wallet()
            time.sleep(5)

# перевод между своими счетами HUMO OTHER

        def test_humo_other_to_humo_ipoteka(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_humo_other_to_humo_ipoteka()
            time.sleep(5)

        def test_humo_other_to_humo_other(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_humo_other_to_humo_other()
            time.sleep(5)

        def test_humo_other_to_uz_card_ipoteka(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_humo_other_to_uz_card_ipoteka()
            time.sleep(5)

        def test_humo_other_to_uz_card_other(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_humo_other_to_uz_card_other()
            time.sleep(5)

        def test_humo_other_to_my_wallet(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_humo_other_to_my_wallet()
            time.sleep(5)

# перевод между своими счетами UZCARD OTHER

        def test_uz_card_other_to_uz_card_ipoteka(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_uz_card_other_to_uz_card_ipoteka()
            time.sleep(5)

        def test_uz_card_other_to_humo_ipoteka(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_uz_card_other_to_humo_ipoteka()
            time.sleep(5)

        def test_uz_card_other_to_humo_other(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_uz_card_other_to_humo_other()
            time.sleep(5)

        def test_uz_card_other_to_my_wallet(self, driver):
            between_transfer = SmartTransferUzCardIpoteka(driver, 'http://192.168.70.50:9090/lite/')
            between_transfer.open()
            between_transfer.between_uz_card_other_to_my_wallet()
            time.sleep(5)
