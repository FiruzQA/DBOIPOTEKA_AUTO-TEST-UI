import time
from generator.generator import generated_person
from pages.base_page import BasePage
from locators.element_page_locators import DepositsLocators


class DepositsDBO(BasePage):
    locators = DepositsLocators

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

    def deposits(self, deposit_choose):
        client_info = next(generated_person())
        number = client_info.loginnumber
        password = client_info.password
        summa = client_info.depositnihols
        self.element_is_visible(self.locators.NUMBER).send_keys(number)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGNIN).click()
        time.sleep(3)
        self.element_is_visible(self.locators.PRODUCTS_AND_SERVICE).click()
        deposits = {
            'first':
                {'choose': self.locators.OFORMIT_NIHOL_3},
            'second':
                {'choose': self.locators.OFORMIT_NIHOL_6},
            'third':
                {'choose': self.locators.OFORMIT_NIHOL_12},
        }
        deposit_choose = self.element_is_visible(deposits[deposit_choose]['choose'])
        deposit_choose.click()
        self.element_is_visible(self.locators.ISTOCHNIK).click()
        self.element_is_visible(self.locators.WALLET).click()
        self.element_is_visible(self.locators.PERCENT_TO_WALLET).click()
        self.element_is_visible(self.locators.PERCENT_TO_WALLET_SECOND).click()
        self.element_is_visible(self.locators.TAG_SUMMA).click()
        self.element_is_visible(self.locators.TAG_SUMMA).send_keys(summa)
        self.element_is_visible(self.locators.BUTTON_OPEN_DEP).click()
        time.sleep(2)
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()
        self.element_is_visible(self.locators.CHECK_STORY).click()
        self.element_is_visible(self.locators.REQUESTS).click()
        time.sleep(2)
        self.element_is_visible(self.locators.UPDATE).click()
