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

time.sleep(5)
save_cookies(chrome, cookies_location)
chrome.quit()

# Click login button
# chrome.find_element_by_css_selector('#main-content #submit').click()
# chrome.find_element_by_css_selector('#submit').click()
# chrome.find_element_by_xpath("//form[@id='signup_form']/section/input[3]").click()
# chrome.find_element_by_xpath("//input[@type='submit']").click()
# chrome.find_element_by_xpath("//input[@id='submit']").click()
# chrome.find_element_by_xpath("//input[@id='submit'][@type='submit']").click()
# chrome.find_element_by_xpath(
#     "//input[contains(@class,'buttonBase create_account_button_disabled')]").submit()
# chrome.find_element_by_xpath(
# "//form[@id='signup_form']/section[@class='formStepOne']/input[@id='submit']").click()
# chrome.find_element_by_id('submit').click()
# chrome.find_element_by_xpath("/html/body/div[6]/div/div[3]/section/div/div[2]/form/section/input[3]").click()
# login_button = chrome.find_element_by_xpath("//input[@id='submit'and @type='submit']")
# login_button = chrome.find_element_by_xpath("//input[@id='submit'and @type='submit' and @class='buttonBase create_account_button_disabled big orangeButton light js-loginSubmit']")
# login_button = chrome.find_element_by_class_name('buttonBase create_account_button_disabled big orangeButton light js-loginSubmit')
# print(login_button)
# login_button.click()
# chrome.find_element_by_xpath("//input[@id='submit']").send_keys('\n')
# chrome.find_element_by_xpath("//input[@id='submit']").submit()
# chrome.find_element_by_xpath("//input[@id='submit']").send_keys('Keys.ENTER')
# chrome.find_element_by_id("submit").click()

# Load of the page you cant access without cookies, this one will fail
# chrome = webdriver.Chrome('./chromedriver')
# chrome.get("https://www.pornhub.com")

# Load of the page you cant access without cookies, this one will go through
# chrome = webdriver.Chrome('./chromedriver')
# load_cookies(chrome, cookies_location)
# chrome.get("https://www.pornhub.com")
# time.sleep(5)
# chrome.quit()

# chrome = webdriver.Chrome()
# chrome.get("https://google.com")
# time.sleep(2)
# pprint.pprint(chrome.get_cookies())
# print "=========================\n"
#
# delete_cookies(chrome, domains=["www.google.com"])
# pprint.pprint(chrome.get_cookies())
# print "=========================\n"
#
# delete_cookies(chrome)
# pprint.pprint(chrome.get_cookies())