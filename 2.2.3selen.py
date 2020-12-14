from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    elements = browser.find_elements_by_css_selector("input[type=text]")
    letters = string.ascii_lowercase
    for element in elements: #заполяем поля рандомными буквами
        random_word = ''.join(random.choice(letters) for i in range(8))
        element.send_keys(random_word)

    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого скрипта 2.2.3selen.py
    file_name = "file_example.txt"  # имя файла, который будем загружать на сайт
    file_path = os.path.join(current_dir, file_name)  # получаем путь к file_example.txt
    element2 = browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path) # отправляем файл

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла type="text"

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
