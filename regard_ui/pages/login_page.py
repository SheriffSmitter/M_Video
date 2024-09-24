import allure
from selene import browser, have


class LoginPage:
    def click_on_login(self):
        with (allure.step('Кликнуть на кнопку "Кабинет".')):
            browser.all('.IconButton_text__B2OHa').element_by(have.text('Кабинет')).click()

    def check_login_page(self):
        with allure.step('Проверить, что отображается страница авторизации.'):
            browser.element('.Authorization_title__68tWs').should(have.exact_text('Личный кабинет'))


login_page = LoginPage()
