from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import service
import pytest
import time

driver = webdriver.Chrome()

driver.implicitly_wait(10)


def test_open_webpage(start_test):
    print(start_test)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    print(driver.title)
    print(driver.current_url)

def test_checklogin():
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
    time.sleep(10)


