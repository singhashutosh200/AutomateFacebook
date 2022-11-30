import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C://chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com")
print(driver.current_url)
print(driver.title)
time.sleep(5)
driver.find_element(By.XPATH, "//*[text()='Create New Account']").click()  # Click on Create New Account
time.sleep(2)
driver.find_element(By.NAME, "firstname").send_keys("XXXX")  # Enter first name
driver.find_element(By.NAME, "lastname").send_keys("XXXX")  # Enter Last name
driver.find_element(By.NAME, "reg_email__").send_keys("XXXXXX@gmail.com")  # Enter e-mail address
driver.find_element(By.NAME, "reg_email_confirmation__").send_keys("XXXXXX@gmail.com")  # Re-Enter e-mail address
driver.find_element(By.ID, 'password_step_input').send_keys("XXXXX")  # Enter password
# select your Date of Birth
day = Select(driver.find_element(By.NAME, "birthday_day"))  # Enter your date of Birth
day.select_by_visible_text('24')
time.sleep(3)
month = Select(driver.find_element(By.NAME, "birthday_month"))  # Enter your month of Birth
month.select_by_visible_text("Feb")
time.sleep(3)
year = Select(driver.find_element(By.NAME, "birthday_year"))  # Enter your year of Birth
year.select_by_visible_text('1995')
time.sleep(5)
# select your gender
driver.find_element(By.XPATH, "//input[@value='2']").click()  # select your gender Male/Female
time.sleep(3)
driver.find_element(By.NAME, "websubmit").click()  # click on submit to Create Account
time.sleep(3)
