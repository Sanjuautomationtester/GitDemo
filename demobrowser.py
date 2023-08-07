import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\Users\sanfr\Downloads\chromedriver-win64")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(10)
print(driver.title)
print(driver.current_url)
driver.close()