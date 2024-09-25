import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"

driver = webdriver.Chrome()

# open the page
driver.get(URL)
# make it full screen or adjust screen size
driver.fullscreen_window()
action = ActionChains(driver)

# code that moves washington block over usa block
# --- Comment out the below code to use all drag and drop addition in the below block --- #
washington = driver.find_element(By.ID, "box3")
usa = driver.find_element(By.ID, "box103")
action.drag_and_drop(washington, usa).perform()


# addition to move all elements over the desired target
for number in range(1, 8):
    source_element = driver.find_element(By.ID, f"box{number}")
    if number:
        target_elem = driver.find_element(By.ID, f"box10{number}")
        action.drag_and_drop(source_element, target_elem).perform()

time.sleep(3)
driver.quit()
