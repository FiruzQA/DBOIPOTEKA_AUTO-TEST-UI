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
    HUMO_OTHER = (By.XPATH, "//div[text()='anor bank']")
    HUMO_OTHER_SECOND = (By.XPATH, "//div[text()='TBCBANK']")
    MY_WALLET = (By.XPATH, "//div[text()='Текущий счёт']")


class SmartMoneyTransferLocators:
    # login
    NUMBER = (By.CSS_SELECTOR, "input[placeholder='Телефон']")
    PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Пароль'")
    SIGNIN = (By.CSS_SELECTOR, "button[class='br-button pri br-login-click-enter']")

    # smart
    CHOOSE_CARD = (By.CSS_SELECTOR, "input[placeholder='Выберите источник']")
    UZ_CARD_IPOTEKA = (By.XPATH, "//div[text()='MY UZCARD CARD SALARY']")
    UZ_CARD_OTHER = (By.XPATH, "//div[text()='капитал']")
    HUMO_IPOTEKA = (By.XPATH, "//div[text()='HUMO CARD PHYSICAL']")
    HUMO_OTHER = (By.XPATH, "//div[text()='anor bank']")
    MY_WALLET = (By.XPATH, "//div[text()='Текущий счёт']")
    CHOOSE_RECEIVER = (By.CSS_SELECTOR, "input[placeholder='Выберите получателя']")
    TRANSFER_BETWEEN_CARDS = (By.XPATH, "//div[text()='Перевод по номеру карты']")
    BUTTON_NEXT = (By.CSS_SELECTOR, "div[class='brw-white-box-action br-pig-action']")
    CARD_NUMBER = (By.CSS_SELECTOR, "input[placeholder='Номер карты получателя']")
    TAG_SUMMA = (By.CSS_SELECTOR, "input[placeholder='Сумма']")
    PUSH_SMS = (By.CSS_SELECTOR, "input[placeholder='Код из PUSH/SMS']")
    CLICK_NEXT = (By.XPATH, "//button[text()='Далее']")
    CLICK_NEXT_SECOND = (By.CSS_SELECTOR, "button[class='br-button br-dialog-button-ok pri']")
    CLICK_CONFIRM = (By.XPATH, "//button[text()='Подтверждаю']")
    BUTTON_CLOSE = (By.XPATH, "//button[text()='Закрыть']")


class TransferWithNumberLocators:

    NUMBER = (By.CSS_SELECTOR, "input[placeholder='Телефон']")
    PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Пароль'")
    SIGNIN = (By.CSS_SELECTOR, "button[class='br-button pri br-login-click-enter']")

    CHOOSE_CARD = (By.CSS_SELECTOR, "input[placeholder='Выберите источник']")
    UZ_CARD_IPOTEKA = (By.XPATH, "//div[text()='MY UZCARD CARD SALARY']")
    UZ_CARD_OTHER = (By.XPATH, "//div[text()='капитал']")
    HUMO_IPOTEKA = (By.XPATH, "//div[text()='HUMO CARD PHYSICAL']")
    HUMO_OTHER = (By.XPATH, "//div[text()='anor bank']")
    MY_WALLET = (By.XPATH, "//div[text()='Текущий счёт']")
    CHOOSE_RECEIVER = (By.CSS_SELECTOR, "input[placeholder='Выберите получателя']")
    TRANSFER_NUMBER = (By.XPATH, "//div[text()='Перевод клиенту по телефону']")
    BUTTON_NEXT = (By.CSS_SELECTOR, "div[class='brw-white-box-action br-pig-action']")
    CLIENT_NUMBER = (By.CSS_SELECTOR, "input[placeholder='Номер телефона получателя']")
    TAG_SUMMA = (By.CSS_SELECTOR, "input[placeholder='Сумма']")
    CLICK_NEXT = (By.XPATH, "//button[text()='Далее']")
    PUSH_SMS = (By.CSS_SELECTOR, "input[placeholder='Код из PUSH/SMS']")
    CLICK_NEXT_SECOND = (By.CSS_SELECTOR, "button[class='br-button br-dialog-button-ok pri']")
    BUTTON_CLOSE = (By.XPATH, "//button[text()='Закрыть']")

class BondWithBankLocators:
    NUMBER = (By.CSS_SELECTOR, "input[placeholder='Телефон']")
    PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Пароль'")
    SIGNIN = (By.CSS_SELECTOR, "button[class='br-button pri br-login-click-enter']")

    CLICK_CHAT_BANK = (By.XPATH, "//div[text()='Чат с Банком']")
