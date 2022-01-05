
'''
Created on Mar 20, 2020
@author: adixit
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

# Step 1) Open Firefox
browser = webdriver.Chrome(ChromeDriverManager().install())
# Step 2) Navigate to Yatra
browser.get("https://www.yatra.com/")
browser.maximize_window()
action = ActionChains(browser)

parent_level_menu = browser.find_element_by_xpath("//a[contains(text(),'My Account')]")
action.move_to_element(parent_level_menu).perform()

child_level_menu = browser.find_element_by_id("signInBtn")
child_level_menu.click()
#ssleep(5000)
ExpTitle = "Yatra Account"
ActTitle = browser.title
print(ActTitle)
assert ExpTitle == ActTitle
browser.close()




