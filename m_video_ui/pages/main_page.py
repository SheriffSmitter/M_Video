import allure
from selene import browser, have


class MainPage:
    def open_main_page(self):
        with allure.step('Открыть главную страницу "М.Видео".'):
            browser.open('/')

    def switch_navigation_tab(self, tab_name):
        with allure.step(f'Переключиться на вкладку "{tab_name}".'):
            browser.all('.top-navbar-link').element_by(have.text(tab_name)).click()

    def click_on_list_of_cities(self):
        with allure.step('Кликнуть на список доступных городов.'):
            browser.element('.location-text').click()

    def choose_city(self, city):
        with allure.step(f'Выбрать город "{city}".'):
            browser.element('.location-select__location').element(have.text(city)).click()

    def check_tab_title(self):
        with allure.step('Проверить названия вкладки.'):
            browser.element('.fl-h1').should(have.exact_text(("М.Мастер")))

    def check_city_tab_title(self, city):
        with allure.step(f'Проверить названия города "{city}".'):
            browser.element('.location-text').element(have.text(city))


main_page = MainPage()
