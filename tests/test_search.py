import allure
from selene import browser, have
from allure_commons.types import Severity

from m_video_ui.pages.main_page import main_page
from m_video_ui.pages.search_page import search_page


@allure.epic('Search')
@allure.feature('Search field')
@allure.link('https://www.mvideo.ru/', name='M.Video')
class TestSearch:
    @allure.title('Find game via search field')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'Vadim Korolev')
    def test_search_field(self):
        main_page.open_main_page()

        search_page.click_on_search()
        search_page.find_game_in_search(product_name="Dyson")
        with (allure.step('Проверить, что загрузилась страница Dyson.')):
            browser.element('.m-banner__title').first.should(
                have.text("Откройте для себя устройства для ухода за волосами"))
