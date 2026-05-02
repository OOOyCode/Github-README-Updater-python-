import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime

now = datetime.now()

driver = webdriver.Chrome()
driver.get("https://www.google.com")
wait = WebDriverWait(driver, 10)

driver.get("https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%253Cuser-name%253E%26source%3Dheader")

username = driver.find_element(By.ID, "login_field").send_keys("username")

mdp = driver.find_element(By.ID, "password").send_keys("password")

driver.find_element(By.NAME, "commit").click()

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "prc-Avatar-Avatar-0xaUi")))

driver.get("https://github.com/username/username/edit/main/README.md")

editor = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cm-content")))

editor.click()
time.sleep(1)

# select all (may or may not work depending on focus)
editor.send_keys(Keys.CONTROL, "a")
editor.send_keys(Keys.DELETE)

# load file content
with open("text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines() 
    for line in lines:
        editor.send_keys(line)
        editor.send_keys(Keys.CONTROL, "x")

 
editor.send_keys(f"Last updated: {now}")


time.sleep(2)
driver.find_element(By.CLASS_NAME, "BlobEditor-module__Button__RZ5_U").click()
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Commit changes']]")))
button.click()

time.sleep(10)
