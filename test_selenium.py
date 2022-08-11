from dataclasses import replace
import time
import allure
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()

path = 'C:/geckodriver.exe'


def open()->None:
    "finction opens tha clothing store site"
    driver = webdriver.Firefox(executable_path=path) 
    driver.maximize_window()
    driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
    return driver


def test_correct_details()->None:
    "test for correct details"
    mylogger.info("test for correct details")
    driver = open()
    driver.find_element(By.NAME, "email").send_keys("vered@gmail.com")
    driver.find_element(By.NAME, "passwd").send_keys("123456")
    driver.find_element(By.NAME, "SubmitLogin").click()
    assert driver.title == 'My account - My Store'
    account = driver.find_element(By.CLASS_NAME, "account")
    span = account.find_element(By.TAG_NAME, "span").text
    assert span == 'Vered Aharonov'
    driver.close()


def test_empty_email()->None:
    "test for empty email"
    mylogger.info("test for empty email")
    driver = open()
    driver.find_element(By.NAME, "passwd").send_keys("123456")
    driver.find_element(By.NAME, "SubmitLogin").click()
    assert driver.title == 'Login - My Store'
    alert = driver.find_element(By.CLASS_NAME, "alert")
    tag = alert.find_element(By.TAG_NAME,"p")
    assert "error" in tag.text
    driver.close()

def test_empty_passwd()->None:
    "test for empty passwoed"
    mylogger.info("test for empty passwoed")
    driver = open()
    driver.find_element(By.NAME, "email").send_keys("vered@gmail.com")
    driver.find_element(By.NAME, "SubmitLogin").click()
    assert driver.title == 'Login - My Store'
    alert = driver.find_element(By.CLASS_NAME, "alert")
    tag = alert.find_element(By.TAG_NAME,"p")
    assert "error" in tag.text
    driver.close()

def test_empty_fildes()->None:
    "test for empty fields"
    mylogger.info("test for empty fields")
    driver = open()
    driver.find_element(By.NAME, "SubmitLogin").click()
    assert driver.title == 'Login - My Store'
    alert = driver.find_element(By.CLASS_NAME, "alert")
    tag = alert.find_element(By.TAG_NAME,"p")
    assert "error" in tag.text
    driver.close()


def test_worng_passwd()->None:
    "test for wrong password"
    mylogger.info("test for wrong password")
    driver = open()
    driver.find_element(By.NAME, "email").send_keys("vered@gmail.com")
    driver.find_element(By.NAME, "passwd").send_keys("123")
    driver.find_element(By.NAME, "SubmitLogin").click()
    assert driver.title == 'Login - My Store'
    alert = driver.find_element(By.CLASS_NAME, "alert")
    tag = alert.find_element(By.TAG_NAME,"p")
    assert "error" in tag.text
    driver.close()

def test_worng_email()->None:
    "test for wrong email"
    mylogger.info("test for wrong email")
    driver = open()
    driver.find_element(By.NAME, "email").send_keys("vered@gmail")
    driver.find_element(By.NAME, "passwd").send_keys("123456")
    driver.find_element(By.NAME, "SubmitLogin").click()
    assert driver.title == 'Login - My Store'
    alert = driver.find_element(By.CLASS_NAME, "alert")
    tag = alert.find_element(By.TAG_NAME,"p")
    assert "error" in tag.text
    driver.close()

def test_forgat_passwd()->None:
    "test for forget password"
    mylogger.info("test for forget password")
    driver = open()
    driver.find_element(By.LINK_TEXT, "Forgot your password?" ).click()
    assert driver.title == 'Forgot your password - My Store'
    driver.close()

def test_find_dress()->None:
    "test to buy cheapest dress"
    mylogger.info("test to buy cheapest dress")
    driver = open()
    driver.find_element(By.NAME, "email").send_keys("vered@gmail.com")
    driver.find_element(By.NAME, "passwd").send_keys("123456")
    driver.find_element(By.NAME, "SubmitLogin").click()
    assert driver.title == 'My account - My Store'
    time.sleep(5)
    prices = []
    driver.find_element(By.NAME, "search_query").send_keys("summer")
    driver.find_element(By.NAME, "submit_search").click()
    time.sleep(5)
    product_list = driver.find_element(By.CLASS_NAME,"product_list")
    product_containers = product_list.find_elements(By.CLASS_NAME,"product-container")
    for product_container in product_containers:
        right_block = product_container.find_element(By.CLASS_NAME,"right-block")
        content_price = right_block.find_element(By.CLASS_NAME,"content_price")
        span = content_price.find_element(By.TAG_NAME,"span").text
        prices.append(span.strip())
    low = min(prices)
    for product_container in product_containers:
        right_block = product_container.find_element(By.CLASS_NAME, "right-block")
        price = right_block.find_element(By.CLASS_NAME, "price").text
        if low == price:
            right_block.find_element(By.CLASS_NAME, "button-container")
            right_block.find_element(By.TAG_NAME, "a").click()
            driver.find_element(By.ID,"add_to_cart").click()
    driver = open()
    button_container = driver.find_element(By.CLASS_NAME, "button-container")
    button_container.find_element(By.TAG_NAME,"a").click()
    driver = open()
    driver.find_element(By.CSS_SELECTOR,"#center_column > p.cart_navigation.clearfix > a.button.btn.btn-default.standard-checkout.button-medium").click()
    driver.find_element(By.NAME,"processAddress").click()
    driver.find_element(By.ID,"uniform-cgv").click()
    time.sleep(5)
    driver.find_element(By.NAME,"processCarrier").click()
    driver.find_element(By.CLASS_NAME,"bankwire").click()
    right_pass = driver.find_element(By.ID,"cart_navigation")
    right_pass.find_element(By.TAG_NAME,"button").click()
    time.sleep(5)
    order = driver.find_element(By.CLASS_NAME,"box").text
    assert "Your order on My Store is complete." in order
    
   
   


    
