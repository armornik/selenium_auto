# for marks need use fixtures as @pytest.mark.mark_name, where mark_name — sting.
# command run: pytest -s -v -m smoke test_fixture_marks1.py
# pytest.ini - in root - registration marks (delete warning)
# pytest -s -v -m "not smoke" test_fixture_marks1.py -> not run smoke
# pytest -s -v -m "smoke or regression" test_fixture_marks1.py -> run some tests
# pytest -s -v -m "smoke and win10" test_fixture_marks1.py -> run test only for Windows10
import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
