from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("headless")
chromeOptions.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="D:\\Tools\\chromedriver.exe",options=chromeOptions)
getUrl = "https://rahulshettyacademy.com/angularpractice/"

driver.get(getUrl)
print(driver.title)