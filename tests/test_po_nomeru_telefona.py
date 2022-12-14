import time
from pages.elements_page import TransferWithNumber


class TestElements:
    class TestWithClientNumber:

        def test_uz_card_ipoteka_to_client_number(self, driver):
            test_transfer = TransferWithNumber(driver, 'http://192.168.70.50:9090/lite/#')
            test_transfer.open()
            test_transfer.uz_card_ipoteka_to_client_number()
            time.sleep(5)

        def test_humo_ipoteka_to_client_number(self, driver):
            number_transfer = TransferWithNumber(driver, 'http://192.168.70.50:9090/lite/#')
            number_transfer.open()
            number_transfer.humo_ipoteka_to_client_number()
            time.sleep(5)

        def test_humo_other_to_client_number(self, driver):
            number_transfer = TransferWithNumber(driver, 'http://192.168.70.50:9090/lite/#')
            number_transfer.open()
            number_transfer.humo_other_to_client_number()
            time.sleep(5)

        def test_uz_card_other_to_client_number(self, driver):
            number_transfer = TransferWithNumber(driver, 'http://192.168.70.50:9090/lite/#')
            number_transfer.open()
            number_transfer.uz_card_other_to_client_number()
            time.sleep(5)

        def test_my_wallet_to_client_number(self, driver):
            number_transfer = TransferWithNumber(driver, 'http://192.168.70.50:9090/lite/#')
            number_transfer.open()
            number_transfer.my_wallet_to_client_number()
            time.sleep(5)
