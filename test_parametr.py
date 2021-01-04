import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('unique_link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestMainPage1():
    def test_n_link(self, browser, unique_link):
        link = f"https://stepik.org/lesson/{unique_link}/step/1"
        browser.get(link)
        answer = math.log(int(time.time()))
        text_area = browser.find_element_by_tag_name('textarea')
        text_area.send_keys(str(answer))
        #input = browser.find_element_by_css_selector('[placeholder="Type your answer here..."]')
        #input.send_keys(answer)
        button = browser.find_element_by_class_name('submit-submission').click()
        time.sleep(2)
        msg = browser.find_element_by_class_name('smart-hints__hint').text
        #exemplar_text = "Correct!"
        print(unique_link, "value: ", msg)
        assert "Correct!" == msg
        #assertEqual(str(msg), str(exemplar_text),"Текста не совпали")  # сравниваем ожидание/реальность


#pytest -s -v test_parametr.py
