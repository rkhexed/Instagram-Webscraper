from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager

# Setup ChromeDriver properly
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Instagram
driver.get("https://www.instagram.com/")

#login
time.sleep(5)
username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
username.clear()
password.clear()
username.send_keys("adyeshaha")
password.send_keys("Kaddu28$%")
login = driver.find_element(By.CSS_SELECTOR, ("button[type='submit']"))
login.click()