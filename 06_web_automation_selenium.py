from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# define target url
URL = "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"

# instantiate the browser
driver = webdriver.Chrome()

# open the page
driver.get(URL)
# make it full screen or adjust screen size
driver.fullscreen_window()
# find the first and last name and type the content
driver.find_element(By.ID, "input-firstname").send_keys("Drimus")
driver.find_element(By.ID, "input-lastname").send_keys("Beniamin")
# find the email field and type the content
driver.find_element(By.ID, "input-email").send_keys("test@testing.com")
# find the telephone field and type the content
driver.find_element(By.ID, "input-telephone").send_keys("+4066666666")
# find the pass related fields and type the content
driver.find_element(By.ID, "input-password").send_keys("testpass123")
driver.find_element(By.ID, "input-confirm").send_keys("testpass123")
# find the subscribe box and click it
driver.find_element(By.XPATH, "//*[@id='content']/form/fieldset[3]/div/div/div[1]/label").click()
# find the read and agree box and click it
driver.find_element(By.XPATH, "//*[@id='content']/form/div/div/div/label").click()
# find the continue button and click it
driver.find_element(By.XPATH, "//*[@id='content']/form/div/div/input").click()

time.sleep(3)

driver.quit()
