import allure
from allure_commons.types import Severity

from m_video_ui.pages.main_page import main_page
from m_video_ui.pages.login_page import login_page


@allure.epic('Login page')
@allure.feature('Elements on login page')
@allure.link('https://www.mvideo.ru/', name='M.Video')
class TestLoginPage:
    @allure.title('Open login page')
    @allure.story('Login button')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'Vadim Korolev')
    def test_open_login_page(self):
        main_page.open_main_page()

        login_page.click_on_login()

        login_page.check_login_page()
