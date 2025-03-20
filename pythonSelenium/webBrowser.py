import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#webdriver.chrome.webdriver =
service_obj = Service("/Users/User/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)

#driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(10)