import allure
from selene import browser, have
from allure_commons.types import Severity

from regard_ui.pages.main_page import main_page
from regard_ui.pages.search_page import search_page


@allure.epic('Search')
@allure.feature('Search field')
@allure.link('https://www.regard.ru/', name='Regard')
class TestSearch:
    @allure.title('Find product via search field')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'Vadim Korolev')
    def test_search_field(self):
        main_page.open_main_page()

        search_page.click_on_search()
        search_page.find_product_in_search(product_name="Dyson")
        with (allure.step('Проверить, что загрузилась страница Dyson.')):
            browser.element('.BrandPromo_title__rhMen').should(have.text("Dyson"))
