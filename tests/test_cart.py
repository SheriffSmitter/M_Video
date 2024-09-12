import allure
from allure_commons.types import Severity

from m_video_ui.pages.main_page import main_page
from m_video_ui.pages.search_page import search_page
from m_video_ui.pages.cart_page import cart_page


@allure.epic('Cart')
@allure.feature('Products in cart')
@allure.link('https://www.mvideo.ru/', name='M.Video')
class TestCart:
    @allure.title('Add product to the cart')
    @allure.story('Add product')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'Vadim Korolev')
    def test_add_game_to_cart(self):
        main_page.open_main_page()

        search_page.click_on_search()
        search_page.find_product_in_search(product_name="Iphone")
        search_page.click_on_first_product_in_search_row()
        cart_page.add_product_to_cart()
        cart_page.move_to_cart()

        cart_page.check_product_in_cart(product_name="Iphone")

    @allure.title('Remove product from the cart')
    @allure.story('Remove product')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'Vadim Korolev')
    def test_remove_game_from_cart(self):
        main_page.open_main_page()

        search_page.click_on_search()
        search_page.find_product_in_search(product_name="Iphone 15 pro max")
        #search_page.click_on_first_product_in_search_row()
        cart_page.add_product_to_cart()
        cart_page.move_to_cart()
        cart_page.remove_product_from_cart()

        cart_page.check_empty_cart()

    @allure.title('Full clear of the cart')
    @allure.story('Clear cart')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'Vadim Korolev')
    def test_clear_cart(self):
        main_page.open_main_page()

        search_page.click_on_search()
        search_page.find_product_in_search(product_name="Iphone")
        #search_page.click_on_first_product_in_search_row()
        cart_page.add_product_to_cart()
        search_page.click_on_search()
        search_page.find_product_in_search(product_name="15 pro max")
        #search_page.click_on_first_product_in_search_row()
        cart_page.add_product_to_cart()
        cart_page.move_to_cart()
        cart_page.clear_cart()

        cart_page.check_empty_cart()
