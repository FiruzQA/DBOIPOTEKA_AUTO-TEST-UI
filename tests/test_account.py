import time
from pages.element_page_second import BondWithBank, ChangePhoto, LogInPage


class TestElements:
    class TestLogIn:

        def test_log_in(self, driver):
            log_in_page = LogInPage(driver, 'https://tbss.ipotekabank.uz:4443/#')
            log_in_page.open()
            log_in_page.login_to_account()
            time.sleep(5)
            print('Succesfully logined')

    class TestBondWithBank:

        def test_bond_with_bank(self, driver):
            bond_with_bank_page = BondWithBank(driver, "https://dbo.ipotekabank.uz/#")
            bond_with_bank_page.open()
            response_code = bond_with_bank_page.click_to_link_bond_with_bank('https://jivo.chat/v1Pf07r4Kv')
            assert response_code == 200
            print(response_code)
            print(response_code == 200)
            time.sleep(5)

    class TestChangePhoto:

        def test_change_photo(self, driver):
            change_photo = ChangePhoto(driver, "https://dbo.ipotekabank.uz/#")
            change_photo.open()
            change_photo.change_photo_on_account()
