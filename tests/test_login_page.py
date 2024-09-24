import allure
from allure_commons.types import Severity

from regard_ui.pages.main_page import main_page
from regard_ui.pages.login_page import login_page


@allure.epic('Login page')
@allure.feature('Elements on login page')
@allure.link('https://www.regard.ru/', name='Regard')
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
