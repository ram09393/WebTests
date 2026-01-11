from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    BUTTON_ENTER = (By.XPATH, "//a[@title='Вход']")
    BUTTON_ENTER_QR = (By.XPATH, "//a[@title='QR-код']")

    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')

    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiButton__host')][@type='submit'][contains(.,'Войти')]")
    LOGIN_BUTTON_QR = (By.XPATH, "//button[contains(.,'Войти по QR-коду')]")
    BUTTON_NO_ENTER = (By.XPATH, "// button[text() = 'Не получается войти?']")

    BUTTON_REGISTRATION = (By.XPATH, "//button[@type='button' and .//*[contains(text(), 'Зарегистрироваться')]]")
    BUTTON_VK = (By.XPATH, "//a[contains(@class, '__vk_id')]")
    BUTTON_Mail = (By.XPATH, "//a[contains(@class, '__mailru')]")
    BUTTON_Yandex = (By.XPATH, "//a[contains(@class, '__yandex')]")
    ERROR_TEXT = (By.XPATH, "//span[text()='Введите логин']")


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.BUTTON_ENTER)
        self.find_element(LoginPageLocators.BUTTON_ENTER_QR)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_QR)
        self.find_element(LoginPageLocators.BUTTON_NO_ENTER)
        self.find_element(LoginPageLocators.BUTTON_REGISTRATION)
        self.find_element(LoginPageLocators.BUTTON_VK)
        self.find_element(LoginPageLocators.BUTTON_Mail)
        self.find_element(LoginPageLocators.BUTTON_Yandex)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

