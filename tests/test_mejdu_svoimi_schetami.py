import time
from pages.elements_page import BetweenTransferUzCardIpoteka


class TestElements:

    class TestSmartTransfer:

        # Перевод между своими счетами UZCARD(Ipoteka)

        def test_uz_card_ipoteka_to_uz_card_other(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_uz_card_ipoteka_to_uz_card_other()
            time.sleep(5)

        def test_uz_card_ipoteka_to_humo_ipoteka(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_uz_card_ipoteka_to_humo_ipoteka()
            time.sleep(5)

        def test_uz_card_ipoteka_to_humo_other(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_uz_card_ipoteka_to_humo_other()
            time.sleep(5)

        def test_uz_card_ipoteka_to_my_wallet(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_uz_card_ipoteka_to_my_wallet()
            time.sleep(5)

# перевод между своими счетами HUMO(Ipoteka)

        def test_humo_ipoteka_to_uz_card_ipoteka(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_humo_ipoteka_to_uz_card_ipoteka()
            time.sleep(5)

        def test_humo_ipoteka_to_uz_card_other(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_humo_ipoteka_to_uz_card_other()
            time.sleep(5)

        def test_humo_ipoteka_to_humo_other(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_humo_ipoteka_to_humo_other()
            time.sleep(5)

        def test_humo_ipoteka_to_my_wallet(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_humo_ipoteka_to_my_wallet()
            time.sleep(5)

# перевод между своими счетами HUMO OTHER

        def test_humo_other_to_humo_ipoteka(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_humo_other_to_humo_ipoteka()
            time.sleep(5)

        def test_humo_other_to_humo_other(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_humo_other_to_humo_other()
            time.sleep(5)

        def test_humo_other_to_uz_card_ipoteka(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_humo_other_to_uz_card_ipoteka()
            time.sleep(5)

        def test_humo_other_to_uz_card_other(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_humo_other_to_uz_card_other()
            time.sleep(5)

        def test_humo_other_to_my_wallet(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_humo_other_to_my_wallet()
            time.sleep(5)

# перевод между своими счетами UZCARD OTHER

        def test_uz_card_other_to_uz_card_ipoteka(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_uz_card_other_to_uz_card_ipoteka()
            time.sleep(5)

        def test_uz_card_other_to_humo_ipoteka(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_uz_card_other_to_humo_ipoteka()
            time.sleep(5)

        def test_uz_card_other_to_humo_other(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_uz_card_other_to_humo_other()
            time.sleep(5)

        def test_uz_card_other_to_my_wallet(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_uz_card_other_to_my_wallet()
            time.sleep(5)

# перевод между своими счетами WALLET

        def test_wallet_to_uz_card_ipoteka(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_wallet_to_uz_card_ipoteka()
            time.sleep(5)

        def test_wallet_to_humo_ipoteka(self, driver):
            between_transfer = BetweenTransferUzCardIpoteka(driver, 'https://tbss.ipotekabank.uz:4443/#')
            between_transfer.open()
            between_transfer.between_wallet_to_humo_ipoteka()
            time.sleep(5)
