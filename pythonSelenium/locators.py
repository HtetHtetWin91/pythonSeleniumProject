import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/User/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)


driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(3)
driver.find_element(By.NAME, "email").send_keys("htethtetwin.minkin@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Htet")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

message = driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text

print(message)
assert "success" in message
driver.close()