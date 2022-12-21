import time
from generator.generator import generated_person
from locators.element_page_locators import BondWithBankLocators, NegativeLogInLocators
from pages.base_page import BasePage
import requests

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
        except AssertionError as a:
            print(a)

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






