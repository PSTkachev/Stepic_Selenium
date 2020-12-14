from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1").text #ищем текст на странице
    y_element = browser.find_element_by_id("num2").text
    sum = str(int(x_element)+int(y_element)) #переводим в инт и суммируем, возвращаем в стр
    print (x_element, y_element, sum)

    #browser.find_element_by_tag_name("select").click()
    select = Select(browser.find_element_by_tag_name("select")) #находим выпадающий список
    select.select_by_value(sum)

    button = browser.find_element_by_css_selector(".btn.btn-default").click()

    alert = browser.switch_to_alert() #скопировать текст высплывающего окна
    print(alert.text)




finally:
    time.sleep(10) # успеваем скопировать код за 30 секунд
    browser.quit()  # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
