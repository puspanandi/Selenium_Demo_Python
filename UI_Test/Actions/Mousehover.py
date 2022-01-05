import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

#browser=webdriver.firefox("C://Users//admin//PycharmProjects//Selenium_Training//Python_Demo//Browser_Driver//geckodriver.exe")
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
browser.find_element_by_name("txtUsername").send_keys("Admin")
browser.find_element_by_name("txtPassword").send_keys("admin123")
browser.find_element_by_xpath("//input[@type='submit']").click()
wait=WebDriverWait(browser,10)
#time.sleep(10)
page_title=browser.title
#assert page_title=="OrangeHRM"
action=ActionChains(browser)
action.move_to_element(browser.find_element_by_xpath("//p[@id='result']")).perform()
browser.find_element_by_link_text("Dashboard").is_displayed()
browser.find_element_by_xpath("//a[@id='welcome']").click()
time.sleep(5)
browser.find_element_by_link_text("Logout").click()
browser.find_element_by_id("logInPanelHeading").is_displayed()

browser.close()