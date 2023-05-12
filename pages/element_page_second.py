import allure
import time
from generator.generator import generated_person, generated_file
from locators.element_page_locators import BondWithBankLocators, NegativeLogInLocators, ChangePhotoLocators, \
    LogInLocators, DepositsLocators, CreditLocators
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
import requests


class LogInPage(BasePage):
    locators = LogInLocators

    def login_to_account(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()


class BondWithBank(BasePage):
    locators = BondWithBankLocators()

    def click_to_link_bond_with_bank(self, url):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        click_link = self.element_is_visible(self.locators.CLICK_CHAT_BANK)
        try:
            request = requests.get(url)
            if request.status_code == 200:
                click_link.click()
                return request.status_code
        except TimeoutException:
            request = requests.get(url)
            if request.status_code == 200:
                click_link.click()
                return request.status_code

class NegativeLogIn(BasePage):
    locators = NegativeLogInLocators()

    def negative_log_in(self, type_click):
        client_info = next(generated_person())
        number = client_info.invalidlogin
        password = client_info.invalidpassword
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        if type_click == "click":
            self.action_click(self.element_is_visible(self.locators.SIGNIN))
            return self.negative_log_in_check(self.locators.TEXT)
        time.sleep(2)
        if type_click == "close":
            self.action_click(self.element_is_visible(self.locators.CLOSE_ERROR))

    def negative_log_in_check(self, element):
        return self.element_is_present(element).text


class ChangePhoto(BasePage):
    locators = ChangePhotoLocators()

    def change_photo_on_account(self):
        file, path = generated_file()
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_UP_PONEL).click()
        self.element_is_visible(self.locators.CLICK_TO_MY_PROFILE).click()
        self.element_is_visible(self.locators.CLICK_ON_PHOTO).click()
        self.element_is_visible(self.locators.CLICK_TO_DOWNLOAD).click()
        self.element_is_visible(self.locators.CLICK_TO_DOWNLOAD).send_keys(path)
        time.sleep(5)


class Deposits(BasePage):
    locators = DepositsLocators()

    def deposit_qulay(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        qulay = client_info.qulay
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(3)
        self.element_is_visible(self.locators.PRODUCTS_AND_SERVICE).click()
        self.element_is_visible(self.locators.DEPOSITS).click()
        self.element_is_visible(self.locators.OFORMIT_QULAY).click()
        self.element_is_visible(self.locators.ISTOCHNIK).click()
        self.element_is_visible(self.locators.WALLET).click()
        self.element_is_visible(self.locators.PERCENT_TO_WALLET).click()
        self.element_is_visible(self.locators.PERCENT_TO_WALLET_SECOND).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(qulay)
        self.element_is_visible(self.locators.BUTTON_OPEN_DEP).click()
        time.sleep(2)
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()
        self.element_is_visible(self.locators.CHECK_STORY).click()
        self.element_is_visible(self.locators.REQUESTS).click()
        time.sleep(2)
        self.element_is_visible(self.locators.UPDATE).click()

    def deposit_nihol_3(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        nihol_3 = client_info.nihols
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(3)
        self.element_is_visible(self.locators.PRODUCTS_AND_SERVICE).click()
        self.element_is_visible(self.locators.OFORMIT_NIHOL_3).click()
        self.element_is_visible(self.locators.ISTOCHNIK).click()
        self.element_is_visible(self.locators.WALLET).click()
        self.element_is_visible(self.locators.PERCENT_TO_WALLET).click()
        self.element_is_visible(self.locators.PERCENT_TO_WALLET_SECOND).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(nihol_3)
        self.element_is_visible(self.locators.BUTTON_OPEN_DEP).click()
        time.sleep(2)
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()
        self.element_is_visible(self.locators.CHECK_STORY).click()
        self.element_is_visible(self.locators.REQUESTS).click()
        time.sleep(2)
        self.element_is_visible(self.locators.UPDATE).click()

    def deposit_nihol_6(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        nihol_6 = client_info.nihols
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(3)
        self.element_is_visible(self.locators.PRODUCTS_AND_SERVICE).click()
        self.element_is_visible(self.locators.OFORMIT_NIHOL_6).click()
        self.element_is_visible(self.locators.ISTOCHNIK).click()
        self.element_is_visible(self.locators.WALLET).click()
        self.element_is_visible(self.locators.PERCENT_TO_WALLET).click()
        self.element_is_visible(self.locators.PERCENT_TO_WALLET_SECOND).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(nihol_6)
        self.element_is_visible(self.locators.BUTTON_OPEN_DEP).click()
        time.sleep(2)
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()
        self.element_is_visible(self.locators.CHECK_STORY).click()
        self.element_is_visible(self.locators.REQUESTS).click()
        time.sleep(2)
        self.element_is_visible(self.locators.UPDATE).click()

    def deposit_nihol_12(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        nihol_12 = client_info.nihols
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(3)
        self.element_is_visible(self.locators.PRODUCTS_AND_SERVICE).click()
        self.element_is_visible(self.locators.OFORMIT_NIHOL_12).click()
        self.element_is_visible(self.locators.ISTOCHNIK).click()
        self.element_is_visible(self.locators.WALLET).click()
        self.element_is_visible(self.locators.PERCENT_TO_WALLET).click()
        self.element_is_visible(self.locators.PERCENT_TO_WALLET_SECOND).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(nihol_12)
        self.element_is_visible(self.locators.BUTTON_OPEN_DEP).click()
        time.sleep(2)
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()
        self.element_is_visible(self.locators.CHECK_STORY).click()
        self.element_is_visible(self.locators.REQUESTS).click()
        time.sleep(2)
        self.element_is_visible(self.locators.UPDATE).click()


class Credit(BasePage):
    locators = CreditLocators()

    def online_credit(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        push = client_info.push_sms
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(3)
        self.element_is_visible(self.locators.PRODUCTS_AND_SERVICE).click()
        self.element_is_visible(self.locators.CHOOSE_CREDIT).click()
        self.element_is_visible(self.locators.CLICK_TERM_OF_CREDIT).click()
        self.element_is_visible(self.locators.TERM_OF_CREDIT).click()
        self.element_is_visible(self.locators.RADIO_BUTTON_ANNUITE).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CHECK_BOX_OFERTA).click()
        self.element_is_visible(self.locators.CLICK_BUTTON_SEND).click()
        time.sleep(3)
        self.element_is_visible(self.locators.PUSH_SMS).send_keys(push)
        self.element_is_visible(self.locators.CLICK_NEXT_SECOND).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()
        self.element_is_visible(self.locators.CHECK_STORY).click()
        self.element_is_visible(self.locators.REQUESTS).click()
        time.sleep(7)
        self.element_is_visible(self.locators.UPDATE).click()

    def replenishment_credit_wallet(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_EXIST_CREDIT).click()
        self.element_is_visible(self.locators.REPAY_BUTTON).click()
        self.element_is_visible(self.locators.ISTOCHNIK).click()
        self.element_is_visible(self.locators.CHOOSE_WALLET).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA_SECOND).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CONTINUE_BUTTON).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()
        self.action_click(self.element_is_visible(self.locators.PAGE_DOWN))

    def replenishment_credit_uz_card_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_EXIST_CREDIT).click()
        self.element_is_visible(self.locators.REPAY_BUTTON).click()
        self.element_is_visible(self.locators.ISTOCHNIK).click()
        self.element_is_visible(self.locators.CHOOSE_UZCARD_IPOTEKA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA_SECOND).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CONTINUE_BUTTON).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()
        self.action_click(self.element_is_visible(self.locators.PAGE_DOWN))

    def replenishment_credit_uz_card_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_EXIST_CREDIT).click()
        self.element_is_visible(self.locators.REPAY_BUTTON).click()
        self.element_is_visible(self.locators.ISTOCHNIK).click()
        self.element_is_visible(self.locators.CHOOSE_UZCARD_OTHER).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA_SECOND).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CONTINUE_BUTTON).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()
        self.action_click(self.element_is_visible(self.locators.PAGE_DOWN))

    def replenishment_credit_humo_ipoteka(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_EXIST_CREDIT).click()
        self.element_is_visible(self.locators.REPAY_BUTTON).click()
        self.element_is_visible(self.locators.ISTOCHNIK).click()
        self.element_is_visible(self.locators.CHOOSE_HUMO_IPOTEKA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA_SECOND).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CONTINUE_BUTTON).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()
        self.action_click(self.element_is_visible(self.locators.PAGE_DOWN))

    def replenishment_credit_humo_other(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_EXIST_CREDIT).click()
        self.element_is_visible(self.locators.REPAY_BUTTON).click()
        self.element_is_visible(self.locators.ISTOCHNIK).click()
        self.element_is_visible(self.locators.CHOOSE_HUMO_OTHER).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA_SECOND).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.CONTINUE_BUTTON).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()
        self.action_click(self.element_is_visible(self.locators.PAGE_DOWN))

    def loan_repayments_credit(self):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.summa
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(5)
        self.element_is_visible(self.locators.CHOOSE_EXIST_CREDIT).click()
        self.element_is_visible(self.locators.LOAN_REPAYMENT_BUTTON).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA_SECOND).send_keys(summa)
        time.sleep(3)
        self.element_is_visible(self.locators.CLICK_NEXT).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()
        self.action_click(self.element_is_visible(self.locators.PAGE_DOWN))
