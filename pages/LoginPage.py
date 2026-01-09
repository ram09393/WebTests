from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    BUTTON_Enter = (By.XPATH, "//a[@title='Вход']")
    BUTTON_Enter_QR = (By.XPATH, "//a[@title='QR-код']")

    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')

    LOGIN_BUTTON_Enter = (By.XPATH, "//button[contains(.,'Войти')]")
    LOGIN_BUTTON_Enter_QR = (By.XPATH, "//button[contains(.,'Войти по QR-коду')]")
    BUTTON_NO_Enter = (By.XPATH, "// button[text() = 'Не получается войти?']")

    BUTTON_REGISTRATION = (By.XPATH, "//button[@type='button' and .//span/span[text()='Зарегистрироваться']")
    BUTTON_VK = (By.XPATH, "//a[contains(@class, '__vk_id')]")
    BUTTON_Mail = (By.XPATH, "//a[contains(@class, '__mailru')]']")
    BUTTON_Yandex = (By.XPATH, "//a[contains(@class, '__yandex')]']")


class LoginPageHelper(BasePage):
    pass
