from selenium import webdriver
import os
from selenium.webdriver.common.by import By


os.environ['PATH'] += r'C:\Users\dell\PycharmProjects\webDriver'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.wikipedia.org/')
driver.implicitly_wait(5)
search = driver.find_element(By.XPATH, '//*[@id="searchInput"]')
search.send_keys('malayalam')
button = driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
button.click()
while True:
    pass
