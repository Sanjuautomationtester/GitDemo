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

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    Title = driver.find_element(By.XPATH, "//div/h4/a").text
    if Title == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()
        time.sleep(2)

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()

driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("India")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div/input[@id='checkbox2']").click()
driver.find_element(By.XPATH,"//form/input[@type='submit']").click()
successText = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")


assert "Success! Thank you!" in successText




