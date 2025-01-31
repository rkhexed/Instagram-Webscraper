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

# Delay for a few seconds to allow the page to load
time.sleep(5)

# Close the driver after use
driver.quit()


