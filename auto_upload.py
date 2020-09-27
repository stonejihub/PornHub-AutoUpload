import time
import pickle
from selenium import webdriver


def load_cookies(driver, location, url=None):

    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()
    # have to be on a page before you can add any cookies, any page - does not matter which
    driver.get("https://google.com" if url is None else url)
    for cookie in cookies:
        if isinstance(cookie.get('expiry'),
                      float):  #Checks if the instance expiry a float
            cookie['expiry'] = int(
                cookie['expiry'])  # it converts expiry cookie to a int
        driver.add_cookie(cookie)

# your cookies location
cookies_location = "./cookies.txt"
chrome = webdriver.Chrome('./chromedriver')
load_cookies(chrome, cookies_location)
chrome.get("https://www.pornhub.com")

chrome.find_element_by_id("headerUploadBtn").click()
time.sleep(1)
chrome.find_element_by_xpath("//*[@id='videoUploadLink']/span[2]").click()

# video path
video_path = 'absolute_path_of_your_video'
time.sleep(1)
chrome.find_element_by_id("fileUploadField").send_keys(video_path)
file_name = 'tests'
chrome.find_element_by_xpath("//*[@id='titleTmplField_0']").send_keys(file_name)
time.sleep(1)
tag1 = 'tag1'
tag2 = 'tag2'
chrome.find_element_by_xpath("//*[@id='tagsList_0']").send_keys(tag1)
time.sleep(2)
chrome.find_element_by_xpath("//*[@id='submitNewTag_0']").click()
time.sleep(2)
chrome.find_element_by_xpath("//*[@id='tagsList_0']").send_keys(tag2)
time.sleep(2)
chrome.find_element_by_xpath("//*[@id='submitNewTag_0']").click()
time.sleep(2)
chrome.find_element_by_xpath("//*[@id='js-validContentConfirmation_0']/div/label/span[1]").click()
time.sleep(1)
# For some reason the element is considered invisible when interacting with selenium by clicking it
categorybox = chrome.find_element_by_xpath("//*[@id='categoryId_13_0']/span[1]")
chrome.execute_script("arguments[0].click();", categorybox)
chrome.find_element_by_xpath("//*[@id='uploaderSaveButton_0']").click()
time.sleep(5)
chrome.quit()
