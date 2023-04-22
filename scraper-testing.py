from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import os

load_dotenv('.env')

userName = os.environ.get("TIKTOK_USERNAME")
password = os.environ.get("TIKTOK_PASSWORD")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://tiktok.com")

try:
    wrapper = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.tiktok-1anes8e-StyledIcon'))
    )
    print("Element found")
except TimeoutException:
    print("Element not found")

driver.find_element(By.CSS_SELECTOR, '.tiktok-1anes8e-StyledIcon').click()

try:
    driver.find_element(By.CSS_SELECTOR, 'div.tiktok-1nncbiz-DivItemContainer:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > h3:nth-child(1)')
    print("Element found")
except NoSuchElementException:
    print("Element not found")

top_video_creator = driver.find_element(By.CSS_SELECTOR, 'div.tiktok-1nncbiz-DivItemContainer:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > h3:nth-child(1)')
print(top_video_creator.text)

driver.close()