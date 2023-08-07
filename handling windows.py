import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"C:\Users\sanfr\Downloads\chromedriver-win64")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowOpened = driver.window_handles

driver.switch_to.window(windowOpened[1])
print(driver.find_element(By.XPATH,"//h3").text)
driver.close()

driver.switch_to.window(windowOpened[0])
assert "Opening a new window" == driver.find_element(By.XPATH,"//h3").text
