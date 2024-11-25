from selenium import webdriver
import pytest

def test_sql_injection():
    driver = webdriver.Chrome()
    driver.get("http://zero.webappsecurity.com/login.html")

    username = driver.find_element("id", "user_login")
    password = driver.find_element("id", "user_password")
    
    username.send_keys("' OR '1'='1")
    password.send_keys("' OR '1'='1")
    driver.find_element("name", "submit").click()

    assert "error" in driver.page_source.lower(), "SQL Injection succeeded!"


    driver.quit()