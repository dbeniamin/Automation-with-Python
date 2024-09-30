import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://the-internet.herokuapp.com/dynamic_controls"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

# set the wait time to 10 seconds
wait = WebDriverWait(driver, 10)

enable_btn = driver.find_element(By.XPATH, "//*[@id='input-example']/button")
enable_btn.click()

time.sleep(3)
disable_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='input-example']/button")))
disable_btn.click()

remove_btn = driver.find_element(By.XPATH, "//*[@id='checkbox-example']/button")
remove_btn.click()
time.sleep(3)

add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='checkbox-example']/button")))
add_btn.click()
time.sleep(3)

check_box = driver.find_element(By.XPATH, "//*[@id='checkbox']")
check_box.click()
time.sleep(3)

driver.quit()
