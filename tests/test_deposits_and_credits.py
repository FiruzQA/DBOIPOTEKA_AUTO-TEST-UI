import time
from pages.element_page_second import Deposits, Credit
from pages.deposits_and_credit_page import DepositsDBO
import allure
@allure.suite("Deposits and Credits")
class TestDepAndCredit:
    @allure.feature("Deposits")
    class TestDeposits:

        @allure.title("check nihol3")
        def test_deposits(self, driver):
            deposit = DepositsDBO(driver, 'http://192.168.70.50:9090/lite/#')
            deposit.open()
            first = deposit.deposits('second')
            print(first)
            time.sleep(5)

        @allure.title("check qulay")
        def test_deposit_qulay(self, driver):
            nihol_3 = DepositsDBO(driver, 'http://192.168.70.50:9090/lite/')
            nihol_3.open()
            nihol_3.deposit_qulay()
            time.sleep(5)

    @allure.feature("Credit")
    class TestCredit:

        @allure.title("check credit")
        def test_credit(self, driver):
            credit_online = Credit(driver, 'https://tbss.ipotekabank.uz:4443/#')
            credit_online.open()
            credit_online.online_credit()
            time.sleep(5)

        @allure.title("check replenishment_credit_wallet ")
        def test_replenishment_credit_wallet(self, driver):
            credit = Credit(driver, 'https://tbss.ipotekabank.uz:4443/#')
            credit.open()
            credit.replenishment_credit_wallet()
            time.sleep(5)

        @allure.title("check replenishment_credit_uz_card_ipoteka")
        def test_replenishment_credit_uz_card_ipoteka(self, driver):
            credit = Credit(driver, 'https://tbss.ipotekabank.uz:4443/#')
            credit.open()
            credit.replenishment_credit_uz_card_ipoteka()
            time.sleep(5)

        @allure.title("check replenishment_credit_uz_card_other")
        def test_replenishment_credit_uz_card_other(self, driver):
            credit = Credit(driver, 'https://tbss.ipotekabank.uz:4443/#')
            credit.open()
            credit.replenishment_credit_uz_card_other()
            time.sleep(5)

        @allure.title("check replenishment_credit_humo_ipoteka")
        def test_replenishment_credit_humo_ipoteka(self, driver):
            credit = Credit(driver, 'https://tbss.ipotekabank.uz:4443/#')
            credit.open()
            credit.replenishment_credit_humo_ipoteka()
            time.sleep(5)

        @allure.title("check replenishment_credit_humo_other")
        def test_replenishment_credit_humo_other(self, driver):
            credit = Credit(driver, 'https://tbss.ipotekabank.uz:4443/#')
            credit.open()
            credit.replenishment_credit_humo_other()
            time.sleep(5)

        @allure.title("check loan_repayments_credit")
        def test_loan_repayments_credit(self, driver):
            credit = Credit(driver, 'https://tbss.ipotekabank.uz:4443/#')
            credit.open()
            credit.loan_repayments_credit()
            time.sleep(5)
