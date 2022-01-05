import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

#browser=webdriver.firefox("C://Users//admin//PycharmProjects//Selenium_Training//Python_Demo//Browser_Driver//geckodriver.exe")
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
browser.get("https://www.testandquiz.com/selenium/testing.html")
browser.find_element_by_xpath("//input[@id='fname']").send_keys("Selenium")
browser.find_element_by_xpath("//input[@id='female']").click()
browser.find_element_by_xpath("//input[@value='Automation']").click()
dropdown=Select(browser.find_element_by_xpath("//select[@id='testingDropdown']"))
dropdown.select_by_index(2)

actions=ActionChains(browser)
actions.double_click(browser.find_element_by_xpath("//button[normalize-space()='Double-click to generate alert box']")).perform()
time.sleep(2)
alert=browser.switch_to.alert
assert alert.text=="hi, JavaTpoint Testing"
alert.accept()

browser.close()