import allure
from selene import browser, have


class CartPage:
    def add_product_to_cart(self):
        with allure.step('Добавить товар в корзину.'):
            browser.element('.Card_buyButton__iJIAi').click()

    def move_to_cart(self):
        with allure.step('Перейти в корзину.'):
            browser.element('.Card_buyButton__iJIAi').click()

    def remove_product_from_cart(self):
        with allure.step('Удалить продукт из корзины.'):
            browser.all('.Icons_delete__VMin6').element(have.text('Удалить')).click()

    def clear_cart(self):
        with allure.step('Очистить корзину.'):
            browser.element('.Checkout_deleteIcon__VI7Fk').click()
            browser.element('.Confirmation_button__oMQax').click()

    def check_product_in_cart(self, product_name):
        with allure.step('Проверить продукт в корзине.'):
            browser.element('.BasketItem_link__qYvgV').should(have.text(product_name))

    def check_empty_cart(self):
        with allure.step('Проверить, что корзина пустая.'):
            browser.all('.BasketEmpty_black__QhefV').first.should(have.exact_text("В корзине пока ничего нет"))


cart_page = CartPage()
