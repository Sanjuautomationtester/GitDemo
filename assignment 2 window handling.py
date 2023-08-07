import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.wait import WebDriverWait

"""webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")"""

service_obj = Service(r"C:\Users\sanfr\Downloads\chromedriver-win64")
driver = webdriver.Chrome(service=service_obj,#options=chrome_options)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CLASS_NAME,"blinkingText").click()
windowOpened = driver.window_handles

driver.switch_to.window(windowOpened[1])
message = driver.find_element(By.CSS_SELECTOR, ".red").text
var = message.split("at")[1].strip().split(" ")[0]
driver.close()
driver.switch_to.window(windowOpened[0])

driver.find_element(By.ID,"username").send_keys("rahulshetty")
driver.find_element(By.ID,"password").send_keys("123456")
driver.find_element(By.XPATH,"//span[@class='checkmark'][1]").click()
driver.find_element(By.XPATH,"//input[@class='btn btn-info btn-md']").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.XPATH,"//div[@class='alert alert-danger col-md-12']").text)
#driver.execute_script("window.scrollBy(0,Document.Body.scrollHeight);")


