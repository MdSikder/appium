import time
from telnetlib import EC

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

desired_cap = {
  "deviceName": "DEAAPJ9DCA45AQEE",
  "platformName": "Android",
  "app": "C:/Users/shabr/OneDrive/Desktop/need/App/General-Store.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
time.sleep(5)

try:
    ApplicationName = driver.find_element(AppiumBy.ID, "//*[@id='screenshotContainer']/div/div/div/div/div/div[41]")
    print("ApplicationName_box is visible")
    ApplicationName.click()
    time.sleep(5)

except NoSuchElementException as e:
    print("NoSuchElementException error", e)
except TimeoutException as e:
    print("TimeoutException error", e)
else:
    assert False
driver.quit()


