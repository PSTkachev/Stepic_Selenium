from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_id("answer").send_keys(y)

    browser.execute_script("window.scrollBy(0, 150);") #скролл на заданное число пикселей

    #button = driver.find_element_by_css_selector("button.btn")  # Скроллим до кнопки "Отправить"
    #driver.execute_script("return arguments[0].scrollIntoView(true);", button)

    for selector in ('#robotCheckbox', '#robotsRule', '.btn'):
        browser.find_element(By.CSS_SELECTOR, selector).click()

    alert = browser.switch_to_alert() #скопировать текст высплывающего окна
    print(alert.text)


finally:
    time.sleep(10) # успеваем скопировать код за 30 секунд
    browser.quit()  # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла





#button = browser.find_element_by_tag_name("button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#button.click()
#assert True