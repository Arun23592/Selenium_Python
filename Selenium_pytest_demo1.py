import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(10)
        yield driver
        driver.close()
        driver.quit()

def test_google_search(driver):

        driver.get("https://www.google.co.in/")
        googleSearchBox = driver.find_element(By.ID, "APjFqb")
        googleSearchBox.send_keys("selenium python")
        driver.find_element(By.NAME, "btnK").click()
        time.sleep(2)
        print("Test completed")