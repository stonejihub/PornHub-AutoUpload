# Source code:
# https://github.com/ArturSpirin/YouTube-WebDriver-Tutorials/blob/master/Cookies.py
import pickle
import pprint
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def save_cookies(driver, location):

    pickle.dump(driver.get_cookies(), open(location, "wb"))

# Path where you want to save/load cookies to/from aka
cookies_location = "./cookies.txt"
username = 'your_pornhub_username'
password = 'your_pornhub_password'

# Initial load of the domain that we want to save cookies for
chrome = webdriver.Chrome('./chromedriver')
chrome.get("https://www.pornhub.com/login")
chrome.find_element_by_xpath("//input[@id='username']").send_keys(
    username)
chrome.find_element_by_xpath("//input[@id='password']").send_keys(password)
# chrome.find_element_by_xpath("//input[@id='remember_me']").click()

# IMPORTANT: need wait some time to click!!!!
# chrome.find_element_by_xpath("//input[@id='submit']").click()
# time.sleep(1)
# Click login button
element = WebDriverWait(chrome,10).until(EC.element_to_be_clickable((By.ID, "submit")))
element.click()

# sleep to sleep you have login
time.sleep(5)
save_cookies(chrome, cookies_location)
chrome.quit()
