#модули
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest
import pytest


link = "http://suninjuly.github.io/simple_form_find_task.html" #ссылка

#простейшая конструкция try finally
try:
    browser = webdriver.Chrome()
    browser.get(link)

    #поиск элементов
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country").send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn").click() #нажатие кнопки
    button = browser.find_element_by_css_selector('[type="submit"]').click()
    button = browser.find_element(By.ID, "submit_button").click()
    button = browser.find_element_by_class_name('btn.btn-primary').click()
    button = browser.find_elements_by_xpath("//button[text()='Submit']").click()



    # Поиск элемента через точные селекторы "http://suninjuly.github.io/registration1.html"
    input1 = browser.find_element_by_css_selector(".first_block > .first_class > .form-control.first").send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block > .form-group.second_class > .form-control.second").send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".first_block > .form-group.third_class > .form-control.third").send_keys("asdf@smail.com")

    x_element = browser.find_element_by_id("num1").text #ищем текст на странице
    y_element = browser.find_element_by_id("num2").text
    sum = str(int(x_element)+int(y_element)) #переводим в инт и суммируем, возвращаем в стр
    select = Select(browser.find_element_by_tag_name("select"))  # находим выпадающий список
    select.select_by_value(sum)


finally:
    time.sleep(10) # успеваем скопировать код за 30 секунд
    browser.quit()  # закрываем браузер после всех манипуляций


text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
slink = browser.find_element_by_partial_link_text(text).click() #поиск элемента по совпадению текста


elements = browser.find_elements_by_css_selector("input[type=text]") #рандомно заполняем все возможные поля для текста "http://suninjuly.github.io/huge_form.html"
letters = string.ascii_lowercase
    for element in elements:
        random_word = ''.join(random.choice(letters) for i in range(8))
        element.send_keys(random_word)
    button = browser.find_element_by_css_selector("button.btn").click()


buttons = driver.find_elements_by_xpath("//button")  # решение где находим все кнопки сабмит
for button in buttons:
    if button.text == 'Submit':
        button.click()


welcome_text_elt = browser.find_element_by_tag_name("h1") # находим элемент, содержащий текст
welcome_text = welcome_text_elt.text # записываем в переменную welcome_text текст из элемента welcome_text_elt
assert "Congratulations! You have successfully registered!" == welcome_text # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта


click_checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']").click()
click_radiobutton = browser.find_element_by_id("robotsRule").click()


#проверяем значение атрибута checked у people_radio
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"


#проверяем значение атрибута disabled у кнопки Submit
    button = browser.find_element_by_css_selector('.btn')
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit: ", button_disabled)
    assert button_disabled is None


x_element = browser.find_element_by_id("treasure") #берем атрибут в изменяющемся элементе
x_checked = x_element.get_attribute("valuex")


for selector in ('#robotCheckbox', '#robotsRule', '.btn'): #прощёлкаем несколько селекторов за цикл
    browser.find_element(By.CSS_SELECTOR, selector).click()


alert = browser.switch_to_alert()  # скопировать текст высплывающего окна
confirm = browser.switch_to.alert.accept()  #для отказа на всплывающих окнах .dismiss()
print(alert.text)


browser.execute_script("window.scrollBy(0, 150);") #скролл на заданное число пикселей


button = driver.find_element_by_css_selector("button.btn")
driver.execute_script("return arguments[0].scrollIntoView(true);", button) # Скроллим до кнопки


#подгружаем файл
current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого скрипта selen_combined.py
file_name = "file_example.txt"  # имя файла, который будем загружать на сайт
file_path = os.path.join(current_dir, file_name)  # получаем путь к file_example.txt
element2 = browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)  # отправляем файл

""" 2. задать с помощью переменных

# указывая директорию,где лежит файлу.txt
# в конце должен быть /
directory = "/home/user/stepik/Chapter2/"

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# собираем путь к файлу
file_path = os.path.join(directory, file_name)
# отправляем файл
element.send_keys(file_path) """


new_window = browser.window_handles[1]
browser.switch_to.window(new_window)  # переходим на новую вкладку


time.sleep(1) # пауза на 2 секунды

button1 = browser.find_element_by_id("book")
WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"),"100")) # явное ожидание в течении 12 сек, вылавливаем нужное нам значение
button1.click()


# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text
exemplar_text = "Congratulations! You have successfully registered!"
self.assertEqual(str(welcome_text), str(exemplar_text), "Window with welcome text did not open") #сравниваем ожидание/реальность


# не забываем оставить пустую строку в конце файла