import allure
from allure_commons.types import Severity

from m_video_ui.pages.main_page import main_page


@allure.feature('Elements on main page')
@allure.epic('Main page')
@allure.link('https://www.mvideo.ru/', name='M.Video')
class TestMainPage:

    @allure.title('Switch on tab "Установка и ремонт»"')
    @allure.story('Tabs')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'Vadim Korolev')
    def test_switch_tab(self):
        main_page.open_main_page()

        main_page.switch_navigation_tab(tab_name='Установка и ремонт')

        main_page.check_tab_title()

    @allure.title('Change the city on the main page to Saint-Petersburg')
    @allure.story('Global actions')
    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.label('owner', 'Vadim Korolev')
    def test_change_city(self):
        main_page.open_main_page()

        main_page.click_on_list_of_cities()
        main_page.choose_city(city="Санкт-Петербург")

        main_page.check_city_tab_title()
