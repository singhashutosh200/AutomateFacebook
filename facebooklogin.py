import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C://chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com")
print(driver.current_url)
print(driver.title)
time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='Email address or phone number']").send_keys("XXXXXX")  #please enter the valid email address or phone number.
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("XXXXXX")  #please enter the valid password
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print(driver.title)
print(driver.current_url)
time.sleep(5)
print(driver.title)
