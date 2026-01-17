import allure
from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelperHelper, HelpPageLocators
from pages.MarketingCabinetHelpPage import MarketingCabinetHelper, MarketingCabinetHelplocators

BASE_URL = 'https://ok.ru/help'


@allure.suite('Проверка страницы "Помощь"')
@allure.title('Проверка элементов на странице и скролла страницы до элемента с кнопкой "Рекламный кабинет ')
def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelperHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.MARKETING_CABINET)
