import time
from generator.generator import generated_person
from locators.element_page_locators import LogInLocators
from locators.element_page_locators import BetweenMoneyTransferLocators
from locators.element_page_locators import SmartMoneyTransferLocators
from locators.element_page_locators import TransferWithNumberLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class LogInPage(BasePage):
    locators = LogInLocators

    def login_to_account(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        return number, password


class BetweenTransferUzCardIpoteka(BasePage):
    locators = BetweenMoneyTransferLocators
# UZ_CARD-IPOTEKA

    def between_uz_card_ipoteka_to_uz_card_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(3)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.CHOOSE_UZ_CARD_OTHER).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.CHOOSE_UZ_CARD_IPOTEKA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

    def between_uz_card_ipoteka_to_humo_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(3)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.HUMO_IPOTEKA).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.CHOOSE_UZ_CARD_IPOTEKA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

    def between_uz_card_ipoteka_to_humo_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(3)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.HUMO_OTHER).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.CHOOSE_UZ_CARD_IPOTEKA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

    def between_uz_card_ipoteka_to_my_wallet(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(3)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.MY_WALLET).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.CHOOSE_UZ_CARD_IPOTEKA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

# HUMO-IPOTEKA

    def between_humo_ipoteka_to_uz_card_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(3)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.CHOOSE_UZ_CARD_IPOTEKA).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_IPOTEKA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

    def between_humo_ipoteka_to_uz_card_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(3)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.CHOOSE_UZ_CARD_OTHER).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_IPOTEKA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

    def between_humo_ipoteka_to_humo_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(3)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.HUMO_OTHER).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_IPOTEKA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

    def between_humo_ipoteka_to_my_wallet(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(3)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.MY_WALLET).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_IPOTEKA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

# HUMO OTHER

    def between_humo_other_to_humo_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(3)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.HUMO_IPOTEKA).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_OTHER).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

    def between_humo_other_to_humo_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(3)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.HUMO_OTHER_SECOND).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_OTHER).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

    def between_humo_other_to_uz_card_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(3)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.CHOOSE_UZ_CARD_IPOTEKA).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_OTHER).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

    def between_humo_other_to_uz_card_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(3)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.CHOOSE_UZ_CARD_OTHER).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_OTHER).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

    def between_humo_other_to_my_wallet(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(3)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.MY_WALLET).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_OTHER).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

# UZ_CARD OTHER

    def between_uz_card_other_to_uz_card_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(3)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.CHOOSE_UZ_CARD_IPOTEKA).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.CHOOSE_UZ_CARD_OTHER).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

    def between_uz_card_other_to_humo_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(5)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.HUMO_IPOTEKA).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.CHOOSE_UZ_CARD_OTHER).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

    def between_uz_card_other_to_humo_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(5)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.HUMO_OTHER).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.CHOOSE_UZ_CARD_OTHER).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

    def between_uz_card_other_to_my_wallet(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(5)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.MY_WALLET).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.CHOOSE_UZ_CARD_OTHER).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

    def between_wallet_to_uz_card_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(5)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.CHOOSE_UZ_CARD_IPOTEKA).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.MY_WALLET).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        # self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()

    def between_wallet_to_humo_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        self.element_is_visible(self.locators.MY_CARDS).click()
        time.sleep(5)
        self.element_is_visible(self.locators.GET_CARD).click()
        self.element_is_visible(self.locators.HUMO_IPOTEKA).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_TO_CHOOSE_CARD).click()
        self.element_is_visible(self.locators.MY_WALLET).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        # self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.CLICK_CLOSE).click()


class TransferWithNumber(BasePage):
    locators = TransferWithNumberLocators

    def uz_card_ipoteka_to_client_number(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        push = client_info.push_sms
        summa = client_info.summa
        client_number = client_info.nomer_klienta
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.UZ_CARD_IPOTEKA).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_NUMBER).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CLIENT_NUMBER).send_keys(client_number)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def humo_ipoteka_to_client_number(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        push = client_info.push_sms
        summa = client_info.summa
        client_number = client_info.nomer_klienta
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_IPOTEKA).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_NUMBER).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CLIENT_NUMBER).send_keys(client_number)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def humo_other_to_client_number(self, type_click):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        push = client_info.push_sms
        summa = client_info.summa
        client_number = client_info.nomer_klienta
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_OTHER).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_NUMBER).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CLIENT_NUMBER).send_keys(client_number)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def uz_card_other_to_client_number(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        push = client_info.push_sms
        summa = client_info.summa
        client_number = client_info.nomer_klienta
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.UZ_CARD_OTHER).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_NUMBER).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CLIENT_NUMBER).send_keys(client_number)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def my_wallet_to_client_number(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        push = client_info.push_sms
        summa = client_info.summa
        client_number = client_info.nomer_klienta
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.MY_WALLET).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_NUMBER).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CLIENT_NUMBER).send_keys(client_number)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()


class SmartMoneyTransfer(BasePage):
    locators = SmartMoneyTransferLocators

# UZ_CARD IPOTEKA

    def smart_uz_card_ipoteka_to_uz_card_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        uz_card = client_info.uzcard_other
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.UZ_CARD_IPOTEKA).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(uz_card)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def smart_uz_card_ipoteka_to_uz_card_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        uz_card = client_info.uz_card_ipoteka_client
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.UZ_CARD_IPOTEKA).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(uz_card)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def smart_uz_card_ipoteka_to_humo_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        humo = client_info.humo_ipoteka_client
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.UZ_CARD_IPOTEKA).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(humo)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def smart_uz_card_ipoteka_to_humo_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        humo = client_info.humo_other
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.UZ_CARD_IPOTEKA).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(humo)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

# HUMO IPOTEKA

    def smart_humo_ipoteka_to_uz_card_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        uz_card = client_info.uz_card_ipoteka_client
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_IPOTEKA).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(uz_card)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def smart_humo_ipoteka_to_uz_card_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        uz_card = client_info.uzcard_other
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_IPOTEKA).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(uz_card)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def smart_humo_ipoteka_to_humo_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        humo = client_info.humo_ipoteka_client
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_IPOTEKA).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(humo)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def smart_humo_ipoteka_to_humo_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        humo = client_info.humo_other
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_IPOTEKA).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(humo)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

# HUMO OTHER

    def smart_humo_other_to_humo_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        humo = client_info.humo_ipoteka_client
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_OTHER).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(humo)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def smart_humo_other_to_humo_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        humo = client_info.humo_other_second
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_OTHER).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(humo)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def smart_humo_other_to_uz_card_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        uz_card = client_info.uz_card_ipoteka_client
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_OTHER).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(uz_card)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def smart_humo_other_to_uz_card_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        uz_card = client_info.uz_card_other_second
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.HUMO_OTHER).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(uz_card)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

# UZ_CARD OTHER

    def smart_uz_card_other_to_uz_card_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        uz_card = client_info.uz_card_ipoteka_client
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.UZ_CARD_OTHER).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(uz_card)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def smart_uz_card_other_to_uz_card_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        uz_card = client_info.uz_card_other_second
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.UZ_CARD_OTHER).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(uz_card)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def smart_uz_card_other_to_humo_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        humo = client_info.humo_ipoteka_client
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.UZ_CARD_OTHER).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(humo)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def smart_uz_card_other_to_humo_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        humo = client_info.humo_other_second
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.UZ_CARD_OTHER).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(humo)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CLICK_CONFIRM).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

# WALLET

    def smart_wallet_to_uz_card_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        uz_card = client_info.uz_card_ipoteka_client
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.MY_WALLET).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(uz_card)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()

    def smart_wallet_to_humo_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        humo = client_info.humo_ipoteka_client
        push = client_info.push_sms
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_CARD).click()
        self.element_is_visible(self.locators.MY_WALLET).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHOOSE_RECEIVER).click()
        self.element_is_visible(self.locators.TRANSFER_BETWEEN_CARDS).click()
        self.element_is_visible(self.locators.BUTTON_NEXT).click()
        self.element_is_visible(self.locators.CARD_NUMBER).send_keys(humo)
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        time.sleep(2)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()