import time
from pages.element_page_second import BondWithBank
import requests

class TestElements:
    class TestBondWithBank:

        def test_bond_with_bank(self, driver):
            bond_with_bank_page = BondWithBank(driver, "https://dbo.ipotekabank.uz/#")
            bond_with_bank_page.open()
            response_code = bond_with_bank_page.click_to_link_bond_with_bank('https://jivo.chat/v1Pf07r4Kv')
            assert response_code == 200
            print(response_code)
            print(response_code == 200)
            time.sleep(5)

