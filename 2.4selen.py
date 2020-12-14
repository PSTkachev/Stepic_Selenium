from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"


try:
    browser = webdriver.Chrome()
    #browser.implicitly_wait(10)  # неявное ожидание, ждем подгрузку элементов
    browser.get(link)

    button1 = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100")) #явное ожидание, вылавливаем нужное нам значение
    button1.click()

    #browser.execute_script("window.scrollBy(0, 150);")  # скролл на заданное число пикселей

    x_element = browser.find_element_by_id("input_value").text
    y = calc(int(x_element))
    print("input value: ", x_element)

    input = browser.find_element_by_id("answer").send_keys(y)
    button2 = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2) # скролл на до видимости элемента
    button2.click()

    alert = browser.switch_to_alert()  # скопировать текст высплывающего окна
    print(alert.text)

finally:
    time.sleep(2) # успеваем скопировать код за 2 секунд
    browser.quit()  # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
