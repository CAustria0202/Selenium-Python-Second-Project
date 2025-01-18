import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from utils import take_screenshot

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

@pytest.mark.parametrize("username,password",
    [("test","test"),
     ("user1","pass2"),
     ("user3","pass3"),
    ])

def test_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(2)
    login_page.enter_username(username)
    time.sleep(2)
    login_page.enter_password(password)
    time.sleep(2)

    # Take a screenshot before clicking the login button
    take_screenshot(driver, username, prefix="before_submit")

    login_page.click_login()

    assert "Successful" in driver.page_source
    time.sleep(2)