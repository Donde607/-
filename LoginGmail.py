from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

#this is not a real gmail account (you can use you owm gmail account)
#이것은 실제 Gmail 계정이 아닙니다(자신의 Gmail 계정을 사용할 수 있음).
username = "AutoTestssk@gmail.com"
password = "AutoTestSK12."

url = "https://accounts.google.com/AccountChooser/identifier?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser"

driver = webdriver.Chrome(r"C:\Users\user\Documents\Selenium Codes\chromedriver.exe")

driver.get(url)
driver.maximize_window()
driver.find_element(By.ID, "identifierId").send_keys(username)
sleep(3)
driver.find_element(By.ID, "identifierNext").click()
sleep(3)
driver.find_element(By.NAME, "password").send_keys(password)
sleep(3)
driver.find_element(By.ID, "passwordNext").click()

print("Logged is Successfully")