from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Tools\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="D:\\Tools\\geckodriver.exe")
getUrl = "https://rahulshettyacademy.com/"
driver.maximize_window()

driver.get(getUrl)
print(driver.title)
print(driver.current_url)
getUrl = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(getUrl)
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()