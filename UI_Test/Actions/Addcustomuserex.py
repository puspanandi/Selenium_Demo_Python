import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
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
action.move_to_element(browser.find_element_by_xpath("//b[normalize-space()='PIM']")).perform()
browser.find_element_by_xpath("//a[@id='menu_pim_Configuration']").click()
browser.find_element_by_xpath("//a[normalize-space()='Custom Fields']").click()
#add custom
browser.find_element_by_xpath("//a[normalize-space()='Custom Fields']").click()
#enter field name
browser.find_element_by_xpath("//input[@id='customField_name']").send_keys("Test")
dropdown1=Select(browser.find_element_by_xpath("//select[@id='customField_screen']"))
dropdown1.select_by_index(5)
#select dropdown2
dropdown2=Select(browser.find_element_by_xpath("//select[@id='customField_type']"))
dropdown2.select_by_index((1))
browser.find_element_by_xpath("//input[@id='btnSave']").click()
