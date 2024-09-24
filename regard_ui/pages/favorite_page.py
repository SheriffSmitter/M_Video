import allure
from selene import browser, have


class FavoritePage:
    def add_product_to_favorite(self):
        with allure.step('Добавить товар в корзину.'):
            browser.element('.IconRectangle_favorite__AyzcN').click()

    def move_to_favorite(self):
        with allure.step('Перейти в избранное.'):
            browser.all('.IconButton_text__B2OHa').element_by(have.text('Избранное')).click()

    def check_product_in_favorite(self, product_name):
        with allure.step('Проверить продукт в избранном.'):
            browser.element('.CardText_link__C_fPZ').should(have.text(product_name))


favorite_page = FavoritePage()
