import allure
from selene import browser, have


class LoginPage:
    def click_on_login(self):
        with (allure.step('Кликнуть на кнопку "Авторизуйтесь, чтобы применить Бонусные рубли".')):
            browser.element('.text ng-star-inserted').element(
                have.text('Авторизуйтесь, чтобы применить Бонусные рубли')).click()

    def check_login_page(self):
        with allure.step('Проверить, что отображается страница авторизации.'):
            browser.element('.login-form__header').should(have.exact_text('Вход или регистрация'))


login_page = LoginPage()
