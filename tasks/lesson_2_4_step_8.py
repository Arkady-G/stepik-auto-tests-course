from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button_1 = browser.find_element_by_id('book').click()

    browser.execute_script("window.scrollBy(0, 100);")

    element_x = int(browser.find_element_by_id('input_value').text)

    solution = str(math.log(abs(12 * math.sin(element_x))))
    input_1 = browser.find_element_by_id('answer').send_keys(solution)

    button_2 = browser.find_element_by_id('solve').click()


finally:
    print(browser.switch_to.alert.text.split()[-1])
    browser.quit()
