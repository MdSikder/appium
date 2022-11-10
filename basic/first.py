from appium import webdriver

desired_cap = {
    "deviceName": "DEAAPJ9DCA45AQEE",
    "platformName": "Android",
    "app": "C:\\Users\\shabr\\OneDrive\\Desktop\\need\\App\\General-Store.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
