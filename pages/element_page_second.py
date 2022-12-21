import time
from generator.generator import generated_person
from locators.element_page_locators import BondWithBankLocators
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




