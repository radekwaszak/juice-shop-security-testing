from selenium import webdriver
import pytest

def test_xss():

    driver = webdriver.Chrome()
    driver.get("http://zero.webappsecurity.com/feedback.html")

    name = driver.find_element("id", "name")
    email = driver.find_element("id", "email")
    subject = driver.find_element("id", "subject")
    comment = driver.find_element("id", "comment")
    
    name.send_keys("<script>alert('XSS')</script>")
    email.send_keys("test@test.com")
    subject.send_keys("Test")
    comment.send_keys("Testing XSS payload")
    driver.find_element("name", "submit").click()

    assert "<script>" not in driver.page_source, "XSS vulnerability detected!"

    driver.quit()