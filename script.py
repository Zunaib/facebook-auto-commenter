from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PAGE_URL = "**** PAGE URL ****"
EMAIL = "**** EMAIL ****"
PASSWORD = "**** PASSWORD ****"
CHROME_DRIVER_PATH = "**** CHROME DRIVER PATH ****"
NUMBER_OF_COMMENTS = 0


driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get(PAGE_URL)
time.sleep(3)
email = driver.find_element_by_id("email")
email.send_keys(EMAIL)
pwd = driver.find_element_by_id("pass")
pwd.send_keys(PASSWORD)
login = driver.find_element_by_id("loginbutton")
login.click()
time.sleep(3)

con = ""
while not con == "yes":
    con = input("ENTER YES WHEN PAGE IS READY\n")
    if con == "yes":
        comments = driver.find_elements_by_class_name("_666h")
        comments[1].click()
        time.sleep(3)
        i = 0
        while i <= NUMBER_OF_COMMENTS:
            textbox = driver.switch_to_active_element()
            textbox.send_keys("It is a comment.")
            textbox.send_keys(Keys.ENTER)
            time.sleep(2)
            i = i + 1
print("DONE\n")
