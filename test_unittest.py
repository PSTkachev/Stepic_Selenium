from selenium import webdriver
import time
import unittest
import pytest



class TestAbs(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block > .first_class > .form-control.first").send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block > .form-group.second_class > .form-control.second").send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block > .form-group.third_class > .form-control.third").send_keys("asdf@smail.com")
        time.sleep(1)
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться, ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        exemplar_text = "Congratulations! You have successfully registered!"

        self.assertEqual(str(welcome_text), str(exemplar_text), "Window with welcome text did not open")


    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block > .first_class > .form-control.first").send_keys(
            "Ivan")
        input2 = browser.find_element_by_css_selector(
            ".first_block > .form-group.second_class > .form-control.second").send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(
            ".first_block > .form-group.third_class > .form-control.third").send_keys("asdf@smail.com")
        time.sleep(1)
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться, ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        exemplar_text = "Congratulations! You have successfully registered!"

        self.assertEqual(str(welcome_text), str(exemplar_text), "Window with welcome text did not open")


if __name__ == "__main__":
    unittest.main()
