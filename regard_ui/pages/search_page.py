import allure
from selene import browser, have


class SearchPage:
    def click_on_search(self):
        with allure.step('Кликнуть на поле поиска.'):
            browser.element('[id="searchInput"]').click()

    def find_product_in_search(self, product_name):
        with allure.step(f'Ввести в поле поиска "{product_name}".'):
            browser.element('[id="searchInput"]').type(product_name).press_enter()

    def click_on_first_product_in_search_row(self):
        with allure.step('Кликнуть на первый результат поиска.'):
            browser.all('.CardText_listing__6mqXC').first.click()

    def check_search_result(self, product_name):
        with allure.step(f'Проверить, что была найден продукт "{product_name}".'):
            browser.element('.Product_title__42hYI').should(have.text(product_name))


search_page = SearchPage()
