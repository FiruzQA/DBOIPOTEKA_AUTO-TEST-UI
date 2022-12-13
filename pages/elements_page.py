import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from generator.generator import generated_person
from locators.element_page_locators import LogInLocators
from locators.element_page_locators import BetweenMoneyTransferLocators
from pages.base_page import BasePage


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


class SmartTransferUzCardIpoteka(BasePage):
    locators = BetweenMoneyTransferLocators

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
        # self.element_is_not_visible(self.locators.PAGE_DOWN_ELEMENT)
