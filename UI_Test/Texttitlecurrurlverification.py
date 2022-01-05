import time

from selenium import webdriver
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
assert page_title=="OrangeHRM"
browser.find_element_by_link_text("Dashboard").is_displayed()
actual_text=browser.find_element_by_xpath("//h1[text()='Dashboard']").text
expected_text='Dashboard'
assert actual_text==expected_text
exp_url="https://opensource-demo.orangehrmlive.com/index.php/dashboard"
browser.current_url==exp_url
browser.find_element_by_xpath("//a[@id='welcome']").click()
time.sleep(5)
browser.find_element_by_link_text("Logout").click()
browser.current_url=="https://opensource-demo.orangehrmlive.com/index.php/auth/login"