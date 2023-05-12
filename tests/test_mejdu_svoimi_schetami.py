import time
from pages.mejdu_moimo_schetami_page import BetweenMyCards
import allure

@allure.suite("Тестирование между своими счетами")
class TestElements:

    @allure.feature("Между своими счетами")
    class TestSmartTransfer:

        # Перевод между своими счетами UZCARD(Ipoteka)

        @allure.title("uzcard(ipoteka) на uzcard(чужого банка)")
        def test_uz_card_ipoteka_to_uz_card_other(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_uz_card_ipoteka_to_uz_card_other()
            time.sleep(5)

        @allure.title("uzcard(ipoteka) на humo(ipoteka)")
        def test_uz_card_ipoteka_to_humo_ipoteka(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_uz_card_ipoteka_to_humo_ipoteka()
            time.sleep(5)

        @allure.title("uzcard(ipoteka) на humo(чужого банка)")
        def test_uz_card_ipoteka_to_humo_other(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_uz_card_ipoteka_to_humo_other()
            time.sleep(5)

        @allure.title("uzcard(ipoteka) на кошелек")
        def test_uz_card_ipoteka_to_my_wallet(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_uz_card_ipoteka_to_my_wallet()
            time.sleep(5)

# перевод между своими счетами HUMO(Ipoteka)

        @allure.title("humo(ipoteka) на uzcard(ipoteka)")
        def test_humo_ipoteka_to_uz_card_ipoteka(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_humo_ipoteka_to_uz_card_ipoteka()
            time.sleep(5)

        @allure.title("humo(ipoteka) на uzcard(чужого банка)")
        def test_humo_ipoteka_to_uz_card_other(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_humo_ipoteka_to_uz_card_other()
            time.sleep(5)

        @allure.title("humo(ipoteka) на humo(чужого банка)")
        def test_humo_ipoteka_to_humo_other(self, driver):
            between_transfer = BetweenMyCards(driver, 'hhttp://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_humo_ipoteka_to_humo_other()
            time.sleep(5)

        @allure.title("humo(ipoteka) на кошелек")
        def test_humo_ipoteka_to_my_wallet(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_humo_ipoteka_to_my_wallet()
            time.sleep(5)

# перевод между своими счетами HUMO OTHER

        @allure.title("humo(чужого банка) на humo(ipoteka)")
        def test_humo_other_to_humo_ipoteka(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_humo_other_to_humo_ipoteka()
            time.sleep(5)

        @allure.title("humo(чужого банка) на humo(чужого банка")
        def test_humo_other_to_humo_other(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_humo_other_to_humo_other()
            time.sleep(5)

        @allure.title("humo(чужого банка) на uzcard(ipoteka)")
        def test_humo_other_to_uz_card_ipoteka(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_humo_other_to_uz_card_ipoteka()
            time.sleep(5)

        @allure.title("humo(чужого банка) на uzcard(чужого банка)")
        def test_humo_other_to_uz_card_other(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_humo_other_to_uz_card_other()
            time.sleep(5)

        @allure.title("humo(чужого банка) на кошелек")
        def test_humo_other_to_my_wallet(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_humo_other_to_my_wallet()
            time.sleep(5)

# перевод между своими счетами UZCARD OTHER

        @allure.title("uzcard(чужого банка) на uzcard(ipoteka)")
        def test_uz_card_other_to_uz_card_ipoteka(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_uz_card_other_to_uz_card_ipoteka()
            time.sleep(5)

        @allure.title("uzcard(чужого банка) на humo(ipoteka)")
        def test_uz_card_other_to_humo_ipoteka(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_uz_card_other_to_humo_ipoteka()
            time.sleep(5)

        @allure.title("uzcard(чужого банка) на humo(чужого банка)")
        def test_uz_card_other_to_humo_other(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_uz_card_other_to_humo_other()
            time.sleep(5)

        @allure.title("uzcard(чужого банка) на кошелек")
        def test_uz_card_other_to_my_wallet(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_uz_card_other_to_my_wallet()
            time.sleep(5)

# перевод между своими счетами WALLET

        @allure.title("с кошелька на uzcard(ipoteka)")
        def test_wallet_to_uz_card_ipoteka(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_wallet_to_uz_card_ipoteka()
            time.sleep(5)

        @allure.title("с кошелька на humo(ipoteka)")
        def test_wallet_to_humo_ipoteka(self, driver):
            between_transfer = BetweenMyCards(driver, 'http://192.168.70.50:9090/lite/#')
            between_transfer.open()
            between_transfer.between_wallet_to_humo_ipoteka()
            time.sleep(5)
