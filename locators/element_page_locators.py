from selenium.webdriver.common.by import By


class LogInLocators:

    NUMBER = (By.CSS_SELECTOR, "input[placeholder='Телефон']")
    PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Пароль'")
    SIGNIN = (By.CSS_SELECTOR, "button[class='br-button pri br-login-click-enter']")
    TEXT = (By.CSS_SELECTOR, "div[class='br-message']")
    CLOSE_ERROR = (By.CSS_SELECTOR, "button[class='br-button br-dialog-button-cancel']")


class BetweenMoneyTransferLocators:

    NUMBER = (By.CSS_SELECTOR, "input[placeholder='Телефон']")
    PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Пароль'")
    SIGNIN = (By.CSS_SELECTOR, "button[class='br-button pri br-login-click-enter']")

    MY_CARDS = (By.XPATH, "//div[text()='Перевод между моими счетами и картами']")
    CHOOSE_UZ_CARD_IPOTEKA = (By.CSS_SELECTOR, "div[class='br-product-sel-text-name product-name product-wid-name"
                                               "-giyhYGM3BNNuLhxX0HhhssDyCx9uRVsgZegcCJPZpQaCeqUwKtu29L2ZmvOW']")
    HUMO_IPOTEKA = (By.XPATH, "//div[text()='HUMO CARD PHYSICAL']")
    CLICK_TO_CHOOSE_CARD = (By.CSS_SELECTOR, "input[placeholder='Источник']")
    GET_CARD = (By.CSS_SELECTOR, "input[placeholder='Получатель']")
    CHOOSE_UZ_CARD_OTHER = (By.XPATH, "//li[@class='br-input-select-item br-input-select-item-click index-1']")
    TAG_SUMMA = (By.CSS_SELECTOR, "input[style='text-align: right;']")
    TAG_SUMMA_SECOND = (By.CSS_SELECTOR, "input[placeholder='Сумма']")
    CLICK_NEXT = (By.XPATH, "//div[@class='br-dialog-body-actions']//button")
    CLICK_CONFIRM = (By.XPATH, "//button[text()='Подтверждаю']")
    CLICK_CLOSE = (By.XPATH, "//button[text()='Закрыть']")
    PAGE_DOWN_ELEMENT = (By.CSS_SELECTOR, "div[class='br-dash-box-content br-dash-box-key _UNIQ_br_dash_box_draw_brc"
                                          " hide-BLOCKED hide-CLOSED hide-PAID dash-style-line hide-hidden']")
