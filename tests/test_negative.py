import time
from pages.element_page_second import NegativeLogIn

class TestElements:
    class TestNegativeLogIn:

        def test_negative_log_in(self, driver):
            log_in = NegativeLogIn(driver, "http://192.168.70.50:9090/lite/#")
            log_in.open()
            click = log_in.negative_log_in('click')
            log_in.negative_log_in('close')
            print(click)
            assert click == 'Неверно указано имя пользователя или пароль'
            time.sleep(5)
