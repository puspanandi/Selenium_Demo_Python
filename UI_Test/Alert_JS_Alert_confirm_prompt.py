import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://the-internet.herokuapp.com/javascript_alerts")
#Click for JS Alert
browser.find_element_by_xpath("//button[normalize-space()='Click for JS Alert']").click()
alert1=browser.switch_to.alert
alert1_text=alert1.text
assert alert1_text=="I am a JS Alert"
alert1.accept()
message1=browser.find_element_by_xpath("//p[@id='result']").text
print(message1)
assert message1=="You successfully clicked an alert"
#browser.close()

#Click on JSConfirm
browser.find_element_by_xpath("//button[text()='Click for JS Confirm']").click()
alert2=browser.switch_to.alert
alert2_text=alert2.text
assert alert2_text=="I am a JS Confirm"
time.sleep(4)
alert2.accept()
message2=browser.find_element_by_xpath("//p[@id='result']").text
print(message2)
assert message2=='You clicked: Ok'
#browser.close

#Click for JS Prompt
browser.find_element_by_xpath("//button[text()='Click for JS Prompt']").click()
alert3=browser.switch_to.alert
alert3_text=alert3.text
assert alert3_text=="I am a JS prompt"
messagetobesent="Selenium/Python"
alert3.send_keys(messagetobesent)
time.sleep(3)
alert3.accept()
message3=browser.find_element_by_xpath("//p[@id='result']").text
print(message3)
split_text=message3.split(':')
st=split_text[1].strip()
assert st=="Selenium/Python"
print("Text matched")
browser.quit()