import time
from pages.elements_page import SmartMoneyTransfer


class TestElements:
    class TestSmartTransfer:

        # UZ_CARD IPOTEKA

        def test_uz_card_ipoteka_to_uz_card_other(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_uz_card_ipoteka_to_uz_card_other()
            time.sleep(5)

        def test_uz_card_ipoteka_to_uz_card_ipoteka(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_uz_card_ipoteka_to_uz_card_ipoteka()
            time.sleep(5)

        def test_uz_card_ipoteka_to_humo_ipoteka(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_uz_card_ipoteka_to_humo_ipoteka()
            time.sleep(5)

        def test_uz_card_ipoteka_to_humo_other(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_uz_card_ipoteka_to_humo_other()
            time.sleep(5)

        # HUMO IPOTEKA

        def test_humo_ipoteka_to_uz_card_ipoteka(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_humo_ipoteka_to_uz_card_ipoteka()
            time.sleep(5)

        def test_humo_ipoteka_to_uz_card_other(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_humo_ipoteka_to_uz_card_other()
            time.sleep(5)

        def test_humo_ipoteka_to_humo_ipoteka(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_humo_ipoteka_to_humo_ipoteka()
            time.sleep(5)

        def test_humo_ipoteka_to_humo_other(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_humo_ipoteka_to_humo_other()
            time.sleep(5)

        # HUMO OTHER

        def test_humo_other_to_humo_ipoteka(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_humo_other_to_humo_ipoteka()
            time.sleep(5)

        def test_humo_other_to_humo_other(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_humo_other_to_humo_other()
            time.sleep(5)

        def test_humo_other_to_uz_card_ipoteka(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_humo_other_to_uz_card_ipoteka()
            time.sleep(5)

        def test_humo_other_to_uz_card_other(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_humo_other_to_uz_card_other()
            time.sleep(5)

        # UZ_CARD OTHER

        def test_uz_card_other_to_uz_card_ipoteka(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_uz_card_other_to_uz_card_ipoteka()
            time.sleep(5)

        def test_uz_card_other_to_uz_card_other(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_uz_card_other_to_uz_card_other()
            time.sleep(5)

        def test_uz_card_other_to_humo_ipoteka(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_uz_card_other_to_humo_ipoteka()
            time.sleep(5)

        def test_uz_card_other_to_humo_other(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_uz_card_other_to_humo_other()
            time.sleep(5)

        # WALLET

        def test_wallet_to_uz_card_ipoteka(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_wallet_to_uz_card_ipoteka()
            time.sleep(5)

        def test_wallet_to_humo_ipoteka(self, driver):
            smart_transfer = SmartMoneyTransfer(driver, 'https://tbss.ipotekabank.uz:4443/#')
            smart_transfer.open()
            smart_transfer.smart_wallet_to_humo_ipoteka()
            time.sleep(5)
