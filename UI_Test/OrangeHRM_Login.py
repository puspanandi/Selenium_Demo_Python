from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

browser=webdriver.firefox("C://Users//admin//PycharmProjects//Selenium_Training//Python_Demo//Browser_Driver//geckodriver.exe")
browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
browser.find_element_by_name("txtUsername").send_keys("Admin")
browser.find_element_by_name("txtPassword").send_keys("admin123")
browser.find_element_by_xpath("//input[@type='submit']").click()
wait=WebDriverWait(browser,10)
#time.sleep(10)
page_title=browser.title
#assert page_title=="OrangeHRM"
browser.find_element_by_link_text("Dashboard").is_displayed()

browser.close()