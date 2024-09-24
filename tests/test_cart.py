import allure
from allure_commons.types import Severity
from regard_ui.pages.main_page import main_page
from regard_ui.pages.search_page import search_page
from regard_ui.pages.cart_page import cart_page


@allure.epic('Cart')
@allure.feature('Products in cart')
@allure.link('https://www.regard.ru/', name='Regard')
class TestCart:
    @allure.title('Add product to the cart')
    @allure.story('Add product')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'Vadim Korolev')
    def test_add_product_to_cart(self):
        main_page.open_main_page()

        search_page.click_on_search()
        search_page.find_product_in_search(product_name="iPhone 15 Pro Max")
        cart_page.add_product_to_cart()
        cart_page.move_to_cart()

        cart_page.check_product_in_cart(product_name="iPhone 15 Pro Max")

    @allure.title('Full clear of the cart')
    @allure.story('Clear cart')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'Vadim Korolev')
    def test_clear_cart(self):
        main_page.open_main_page()

        search_page.click_on_search()
        search_page.find_product_in_search(product_name="Xiaomi Poco")
        cart_page.add_product_to_cart()
        search_page.click_on_search()
        search_page.find_product_in_search(product_name="C65")
        cart_page.add_product_to_cart()
        cart_page.move_to_cart()
        cart_page.clear_cart()

        cart_page.check_empty_cart()
