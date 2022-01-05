from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#open the first window
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

#get the window handle after the window has opened
window_before = driver.window_handles[0]

window_before_title = driver.title
print(window_before_title)
assert "OrangeHRM" in window_before_title

#open a new window
driver.execute_script("window.open('https://the-internet.herokuapp.com/javascript_alerts', 'new window')")

#get the window handle after a new window has opened
window_after = driver.window_handles[1]

#switch on to new child window
driver.switch_to.window(window_after)
time.sleep(5)

window_after_title = driver.title
print(window_after_title)
assert "The Internet" in window_after_title
#Compare and verify that main window and child window title don't match
if window_before_title != window_after_title:
    print('Context switched to JS Script, so the title did not match')
else:
    print('Control did not switch to new window')

    #switch back to original window
driver.switch_to.window(window_before)

#Verify that the title now match
if window_before_title == driver.title:
    print('Context returned to parent window. Title now match')

print(driver.title)
driver.quit()