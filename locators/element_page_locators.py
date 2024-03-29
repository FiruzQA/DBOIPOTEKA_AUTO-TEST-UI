from selenium.webdriver.common.by import By


class LogInLocators:

    NUMBER = (By.CSS_SELECTOR, "input[placeholder='Телефон']")
    PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Пароль'")
    SIGNIN = (By.CSS_SELECTOR, "button[class='br-button pri br-login-click-enter']")
    TEXT = (By.CSS_SELECTOR, "//div[text()='Неверно указано имя пользователя или пароль']")
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
    CHECK_STORY = (By.XPATH, "//div[text()='История']")
    UPDATE = (By.CSS_SELECTOR, "div[class='br-action-hover br-dash-action br-dash-action-with-icon-br_icon_repeat br_"
                               "icon_repeat has-icon hide-right-icon br-history-tabs-generic-refresh br-accept-dp BR_"
                               "tab_history_refresh _action_BR_tab_history_refresh']")


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
    CHECK_STORY = (By.XPATH, "//div[text()='История']")
    UPDATE = (By.CSS_SELECTOR, "div[class='br-action-hover br-dash-action br-dash-action-with-icon-br_icon_repeat br_"
                               "icon_repeat has-icon hide-right-icon br-history-tabs-generic-refresh br-accept-dp BR_"
                               "tab_history_refresh _action_BR_tab_history_refresh']")


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
    PAGE_DOWN = (By.XPATH, "//td[@class='br-dash-box-alter-menu br-popup-toggle'][1]")
    CHECK_STORY = (By.XPATH, "//div[text()='История']")
    UPDATE = (By.CSS_SELECTOR, "div[class='br-action-hover br-dash-action br-dash-action-with-icon-br_icon_repeat br_"
                               "icon_repeat has-icon hide-right-icon br-history-tabs-generic-refresh br-accept-dp BR_"
                               "tab_history_refresh _action_BR_tab_history_refresh']")


class BondWithBankLocators:
    NUMBER = (By.CSS_SELECTOR, "input[placeholder='Телефон']")
    PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Пароль'")
    SIGNIN = (By.CSS_SELECTOR, "button[class='br-button pri br-login-click-enter']")

    CLICK_CHAT_BANK = (By.XPATH, "//div[text()='Чат с Банком']")


class NegativeLogInLocators:
    NUMBER = (By.CSS_SELECTOR, "input[placeholder='Телефон']")
    PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Пароль'")
    SIGNIN = (By.CSS_SELECTOR, "button[class='br-button pri br-login-click-enter']")
    TEXT = (By.CSS_SELECTOR, "div[class='br-message']")
    CLOSE_ERROR = (By.CSS_SELECTOR, "button[class='br-button br-dialog-button-cancel']")


class ChangePhotoLocators:
    NUMBER = (By.CSS_SELECTOR, "input[placeholder='Телефон']")
    PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Пароль'")
    SIGNIN = (By.CSS_SELECTOR, "button[class='br-button pri br-login-click-enter']")

    CLICK_UP_PONEL = (By.CSS_SELECTOR, "div[class='br-dash-top-ava-letter br-personal-ava has-photo']")
    CLICK_TO_MY_PROFILE = (By.XPATH, "//div[@class='br-popup-action-icon br-icons-lib br_icon_home']"
                                     "//following-sibling::div")
    CLICK_ON_PHOTO = (By.CSS_SELECTOR, "div[class='br-personal-ava has-photo']")
    CLICK_TO_DOWNLOAD = (By.XPATH, "//div[text()='Загрузить']")


class DepositsLocators:
    NUMBER = (By.CSS_SELECTOR, "input[placeholder='Телефон']")
    PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Пароль'")
    SIGNIN = (By.CSS_SELECTOR, "button[class='br-button pri br-login-click-enter']")
    PRODUCTS_AND_SERVICE = (By.XPATH, "//div[text()='Продукты и услуги']")
    DEPOSITS = (By.XPATH, "//*[@id='brt_deposits']/table[1]/tbody/tr/td[2]/div/div[2]")
    OFORMIT_QULAY = (By.XPATH, "//div[@id='brv_deposit_offers_action_3']/button[text()='Оформить']")
    ISTOCHNIK = (By.CSS_SELECTOR, "input[placeholder='Источник открытия вклада']")
    WALLET = (By.XPATH, "//div[text()='Текущий счёт']")
    PERCENT_TO_WALLET = (By.CSS_SELECTOR, "input[placeholder='Зачисление процентов']")
    PERCENT_TO_WALLET_SECOND = (By.XPATH, "//td[text()='Зачислить проценты на текущий счет']")
    TAG_SUMMA = (By.CSS_SELECTOR, "input[id='brv_deposit_amount']")
    BUTTON_OPEN_DEP = (By.XPATH, "//button[text()='Открыть вклад']")
    BUTTON_CLOSE = (By.XPATH, "//button[text()='Закрыть']")
    CHECK_STORY = (By.XPATH, "//div[text()='История']")
    REQUESTS = (By.XPATH, "//div[text()='Заявки']")
    UPDATE = (By.CSS_SELECTOR, "div[class='br-action-hover br-dash-action br-dash-action-with-icon-br_icon_repeat br_"
                               "icon_repeat has-icon hide-right-icon br-history-tabs-generic-refresh br-accept-dp BR_"
                               "tab_history_refresh _action_BR_tab_history_refresh']")
    OFORMIT_NIHOL_3 = (By.CSS_SELECTOR, "span[id='deposits_action_0'] button[class='br-button brt-product-button-dark']")
    OFORMIT_NIHOL_6 = (By.XPATH, "//span[@id='deposits_action_1']//button")
    OFORMIT_NIHOL_12 = (By.XPATH, "//span[@id='deposits_action_2']//button")


class CreditLocators:
    # Оформление кредита
    NUMBER = (By.CSS_SELECTOR, "input[placeholder='Телефон']")
    PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Пароль'")
    SIGNIN = (By.CSS_SELECTOR, "button[class='br-button pri br-login-click-enter']")
    PRODUCTS_AND_SERVICE = (By.XPATH, "//div[text()='Продукты и услуги']")
    CHOOSE_CREDIT = (By.XPATH, "//span[@id='credits_action_0']//button")
    CLICK_TERM_OF_CREDIT = (By.CSS_SELECTOR, "input[placeholder='Срок кредита (мес.)']")
    TERM_OF_CREDIT = (By.XPATH, "//td[text()='36']")
    RADIO_BUTTON_ANNUITE = (By.XPATH, "//tr[@class='br-input-list-tr br-input-list-multi-value-ANNUITE']")
    CHECK_BOX_OFERTA = (By.XPATH, "/html/body/div/div[2]/div/div[4]/div/div/table/tbody/tr/td/div/div/table/tbody/tr/"
                                  "td[2]/div[4]/table/tr[11]/td[2]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr"
                                  "/td/table/tbody/tr/td[1]/table/tbody/tr/td/div")
    CLICK_BUTTON_SEND = (By.XPATH, "//button[text()='Отправить']")
    PUSH_SMS = (By.CSS_SELECTOR, "input[placeholder='Код из PUSH/SMS']")
    CLICK_NEXT_SECOND = (By.CSS_SELECTOR, "button[class='br-button br-dialog-button-ok pri']")
    BUTTON_CLOSE = (By.XPATH, "//button[text()='Закрыть']")
    CHECK_STORY = (By.XPATH, "//div[text()='История']")
    REQUESTS = (By.XPATH, "//div[text()='Заявки']")
    UPDATE = (By.CSS_SELECTOR, "div[class='br-action-hover br-dash-action br-dash-action-with-icon-br_icon_repeat br_"
                               "icon_repeat has-icon hide-right-icon br-history-tabs-generic-refresh br-accept-dp BR_"
                               "tab_history_refresh _action_BR_tab_history_refresh']")
    # Пополнение и погашение кредита
    CHOOSE_EXIST_CREDIT = (By.XPATH, "//div[text()='Не погашен']")
    REPAY_BUTTON = (By.XPATH, "//div[text()='Погасить']")
    ISTOCHNIK = (By.CSS_SELECTOR, "input[placeholder='Источник']")
    CHOOSE_WALLET = (By.XPATH, "//div[text()='Текущий счёт']")
    CHOOSE_UZCARD_IPOTEKA = (By.XPATH, "//div[text()='MY UZCARD CARD SALARY']")
    CHOOSE_UZCARD_OTHER = (By.XPATH, "//div[text()='капитал']")
    CHOOSE_HUMO_IPOTEKA = (By.XPATH, "//div[text()='HUMO CARD PHYSICAL']")
    CHOOSE_HUMO_OTHER = (By.XPATH, "//div[@class='br-product-sel-text-name product-name product-wid-name-giyhYTZi"
                                   "AtNuekYE1Hhhs5amCx9qQgsgYOlLBMOM9FaDePQ0KuqeO5NZQf0T']")
    TAG_SUMMA = (By.CSS_SELECTOR, "input[style='text-align: right;']")
    TAG_SUMMA_SECOND = (By.CSS_SELECTOR, "input[placeholder='Сумма']")
    CLICK_NEXT = (By.XPATH, "//div[@class='br-dialog-body-actions']//button")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Продолжить']")
    PAGE_DOWN = (By.XPATH, "//td[text()='Остаток на счете для погашения']")

    LOAN_REPAYMENT_BUTTON = (By.XPATH, "//div[text()='Досрочное погашение']")






