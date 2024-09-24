import allure
from allure_commons.types import Severity
from regard_ui.pages.main_page import main_page
from regard_ui.pages.search_page import search_page
from regard_ui.pages.favorite_page import favorite_page


@allure.epic('Favorite')
@allure.feature('Products in favorite')
@allure.link('https://www.regard.ru/', name='Regard')
class TestFavorite:
    @allure.title('Add product to the favorite')
    @allure.story('Add product')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'Vadim Korolev')
    def test_add_product_to_favorite(self):
        main_page.open_main_page()

        search_page.click_on_search()
        search_page.find_product_in_search(product_name="iPhone 15 Pro Max")
        favorite_page.add_product_to_favorite()
        favorite_page.move_to_favorite()
        favorite_page.check_product_in_favorite(product_name="iPhone 15 Pro Max")
