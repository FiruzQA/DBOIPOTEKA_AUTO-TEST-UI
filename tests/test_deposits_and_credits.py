import time
from pages.element_page_second import Deposits, Credit


class TestDepAndCredit:
    class TestDeposits:

        def test_deposit_qulay(self, driver):
            qulay = Deposits(driver, 'https://tbss.ipotekabank.uz:4443/#')
            qulay.open()
            qulay.deposit_qulay()
            time.sleep(5)

        def test_deposit_nihol_1(self, driver):
            nihol_3 = Deposits(driver, 'https://tbss.ipotekabank.uz:4443/#')
            nihol_3.open()
            nihol_3.deposit_nihol_3()
            time.sleep(5)

        def test_deposit_nihol_2(self,driver):
            nihol_6 = Deposits(driver, 'https://tbss.ipotekabank.uz:4443/#')
            nihol_6.open()
            nihol_6.deposit_nihol_6()
            time.sleep(5)

        def test_deposit_nihol_3(self, driver):
            nihol_12 = Deposits(driver, 'https://tbss.ipotekabank.uz:4443/#')
            nihol_12.open()
            nihol_12.deposit_nihol_12()
            time.sleep(5)

    class TestCredit:

        def test_credit(self, driver):
            credit_online = Credit(driver, 'https://tbss.ipotekabank.uz:4443/#')
            credit_online.open()
            credit_online.online_credit()
            time.sleep(5)

        def test_replenishment_credit_wallet(self, driver):
            credit = Credit(driver, 'https://tbss.ipotekabank.uz:4443/#')
            credit.open()
            credit.replenishment_credit_wallet()
            time.sleep(15)

        def test_replenishment_credit_uz_card_ipoteka(self, driver):
            credit = Credit(driver, 'https://tbss.ipotekabank.uz:4443/#')
            credit.open()
            credit.replenishment_credit_uz_card_ipoteka()
            time.sleep(40)

        def test_replenishment_credit_uz_card_other(self, driver):
            credit = Credit(driver, 'https://tbss.ipotekabank.uz:4443/#')
            credit.open()
            credit.replenishment_credit_uz_card_other()
            time.sleep(40)

        def test_replenishment_credit_humo_ipoteka(self, driver):
            credit = Credit(driver, 'https://tbss.ipotekabank.uz:4443/#')
            credit.open()
            credit.replenishment_credit_humo_ipoteka()
            time.sleep(40)

        def test_replenishment_credit_humo_other(self, driver):
            credit = Credit(driver, 'https://tbss.ipotekabank.uz:4443/#')
            credit.open()
            credit.replenishment_credit_humo_other()
            time.sleep(40)

        def test_loan_repayments_credit(self, driver):
            credit = Credit(driver, 'https://tbss.ipotekabank.uz:4443/#')
            credit.open()
            credit.loan_repayments_credit()
            time.sleep(15)
