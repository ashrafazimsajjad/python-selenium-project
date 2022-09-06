from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

ADMINSIGNIN_URL = "http://hirehub-admin.newroztech.com/"
PASSWD = "Hello@123"

driver = webdriver.Chrome(executable_path="D:\\Tools\\chromedriver.exe")
driver.maximize_window()
driver.get(ADMINSIGNIN_URL)



sleep(1)
signin_email = driver.find_element(by=By.XPATH, value="/html/body/div/div/main/div/form/div[1]/div/input")
signin_email.send_keys("admin@hirehub.com")

signin_pass = driver.find_element(by=By.XPATH, value="/html/body/div/div/main/div/form/div[2]/div/input")
signin_pass.send_keys(PASSWD)

login = driver.find_element(by=By.XPATH, value="/html/body/div/div/main/div/form/button")
login.submit()



sleep(3)
app_drawer = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[1]/div[1]/i")
app_drawer.click()
sleep(1)
job_list = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[3]/li[4]")
job_list.click()
sleep(1)
job_overview = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[4]/table/tr[1]/td[4]/button")
job_overview.click()

act = ActionChains(driver)
src = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[5]/div[1]/div")
dest = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[5]/div[2]/div")
act.drag_and_drop(src, dest).perform()
