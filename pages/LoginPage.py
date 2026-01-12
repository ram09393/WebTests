import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    BUTTON_ENTER = (By.XPATH, "//a[@title='Вход']")
    BUTTON_ENTER_QR = (By.XPATH, "//a[@title='QR-код']")

    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')

    LOGIN_BUTTON_ENTER = (
        By.XPATH, "//button[contains(@class, 'vkuiButton__host')][@type='submit'][contains(.,'Войти')]")
    LOGIN_BUTTON_ENTER_QR = (By.XPATH, "//button[contains(.,'Войти по QR-коду')]")
    BUTTON_NO_ENTER = (By.XPATH, "// button[text() = 'Не получается войти?']")

    BUTTON_REGISTRATION = (By.XPATH, "//button[@type='button' and .//*[contains(text(), 'Зарегистрироваться')]]")
    BUTTON_VK = (By.XPATH, "//a[contains(@class, '__vk_id')]")
    BUTTON_Mail = (By.XPATH, "//a[contains(@class, '__mailru')]")
    BUTTON_Yandex = (By.XPATH, "//a[contains(@class, '__yandex')]")
    ERROR_TEXT_LOGIN = (By.XPATH, "//span[.='Введите логин']")
    ERROR_TEXT_PASSWORD = (By.XPATH, "//span[.='Введите пароль']")


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.BUTTON_ENTER)
        self.find_element(LoginPageLocators.BUTTON_ENTER_QR)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_ENTER)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_ENTER_QR)
        self.find_element(LoginPageLocators.BUTTON_NO_ENTER)
        self.find_element(LoginPageLocators.BUTTON_REGISTRATION)
        self.find_element(LoginPageLocators.BUTTON_VK)
        self.find_element(LoginPageLocators.BUTTON_Mail)
        self.find_element(LoginPageLocators.BUTTON_Yandex)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON_ENTER).click()

    @allure.step('Заполняем поле с логином"')
    def send_keys_login_field(self, value):
        self.attach_screenshot()
        field = self.find_element(LoginPageLocators.LOGIN_FIELD)
        field.send_keys(value)

    @allure.step('Поле с паролем не заполнено')
    def password_field_empty(self):
        self.find_element(LoginPageLocators.PASSWORD_FIELD)

    @allure.step('Получаем текст ошибки')
    def get_error_text_login(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT_LOGIN).text

    @allure.step('Получаем текст ошибки')
    def get_error_text_password(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT_PASSWORD).text
