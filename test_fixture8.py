#Маркировка тестов часть 1
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


class TestMainPage1():

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.skip #чтобы пропустить тест, его отмечают в коде как @pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.xfail(reason="fixing this bug right now") #XFail: помечать тест как ожидаемо падающий #XPASS (“unexpectedly passing” — неожиданно проходит)
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        #browser.find_element_by_css_selector("button.favorite") #не рабочий селектор
        browser.find_element_by_css_selector("input.btn.btn-default") #рабочий селектор

#pytest -rx -v test_fixture8.py #-rx для reason xfail

#Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку:
#pytest -s -v -m smoke test_fixture8.py

#Инверсия
#pytest -s -v -m "not smoke" test_fixture8.py

#Объединение тестов с разными маркировками
#pytest -s -v -m "smoke or regression" test_fixture8.py

#Чтобы запустить только smoke-тесты для Windows 10, нужно использовать логическое И:
#pytest -s -v -m "smoke and win10" test_fixture8.py