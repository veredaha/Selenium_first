from dataclasses import replace
import time
from typing import Container
import allure
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

path = 'C:/geckodriver.exe'


def test_drag_and_drop()->None:
    "Test for dragging and dropping"
    driver = webdriver.Firefox(executable_path=path) 
    driver.get('https://demo.guru99.com/test/drag_drop.html')
    time.sleep(3)
    assert 'Drag and Drop' in driver.title 
    time.sleep(3)
    action = ActionChains(driver)
    source = driver.find_element(By.XPATH , "//*[@id='fourth']/a")
    target = driver.find_element(By.XPATH , "//*[@id='amt7']/li")
    action.drag_and_drop(source,target).perform()
    source = driver.find_element(By.XPATH , "//*[@id='fourth']/a")
    target = driver.find_element(By.XPATH , "//*[@id='amt8']/li")
    action.drag_and_drop(source,target).perform()
    source = driver.find_element(By.XPATH , "//*[@id='credit2']/a")
    target = driver.find_element(By.XPATH , "//*[@id='bank']")
    action.drag_and_drop(source,target).perform()
    source = driver.find_element(By.XPATH , "//*[@id='credit1']/a")
    target = driver.find_element(By.XPATH , "//*[@id='loan']/li")
    action.drag_and_drop(source,target).perform()
    time.sleep(3)
    sales = driver.find_element(By.XPATH, "//*[@id='loan']/li").text
    assert sales == 'SALES'
    amount = driver.find_element(By.XPATH, "//*[@id='amt7']/li").text
    assert amount == '5000'
    amount2 = driver.find_element(By.XPATH, "//*[@id='amt8']/li").text
    assert amount2 == '5000'
    bank = driver.find_element(By.XPATH, "//*[@id='bank']/li").text
    assert bank == 'BANK'
    time.sleep(3)
    driver.close()
    

def test_eye_icon()->None:
    "eye icon"
    driver = webdriver.Firefox(executable_path=path) 
    driver.set_window_size(800,800)
    driver.get('http://automationpractice.com/index.php')
    center= driver.find_element(By.ID, "center_column")
    product_containers = center.find_element(By.CLASS_NAME,"product-container")
    eye = product_containers.find_element(By.CLASS_NAME,"icon-eye-open").click()
    time.sleep(10)
    driver.maximize_window()
    time.sleep(10)
    my_frame =driver.find_element(By.CLASS_NAME,"fancybox-iframe")
    driver.switch_to.frame(my_frame)
    button =driver.find_element(By.ID,"add_to_cart").click()
    time.sleep(5)
    but = driver.find_element(By.PARTIAL_LINK_TEXT,"Proceed to checkout")
    time.sleep(5)
    but.click()
    time.sleep(5)
    but2 = driver.find_element(By.PARTIAL_LINK_TEXT,"Proceed to checkout")
    time.sleep(5)
    but2.click()
    time.sleep(5)
    driver.find_element(By.NAME, "email").send_keys("vered@gmail.com")
    driver.find_element(By.NAME, "passwd").send_keys("123456")
    driver.find_element(By.NAME, "SubmitLogin").click()
    but3 = driver.find_element(By.PARTIAL_LINK_TEXT,"Proceed to checkout")
    time.sleep(5)
    but3.click()
    driver.find_element(By.ID,"cgv").click()
    but4 = driver.find_element(By.PARTIAL_LINK_TEXT,"Proceed to checkout")
    time.sleep(5)
    but4.click()
    driver.find_element(By.CLASS_NAME,"bankwire").click()
    driver.find_element(By.PARTIAL_LINK_TEXT,"I confirm my order").click()
    text = driver.find_element(By.CLASS_NAME,"dark").text
    assert 'Your order on My Store is complete.' in text
    driver.close()
    


def alerts()->None:
    "alert test"
    driver = webdriver.Firefox(executable_path=path) 
    driver.get('http://the-internet.herokuapp.com/javascript_alerts')

    driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[1]/button").click()
    obj = driver.switch_to.alert
    obj.accept
    msg=obj.text
    assert msg == 'I am a JS Alert'
    
    
    driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/button").click()
    obj = driver.switch_to.alert
    obj.accept
    msg=obj.text
    assert msg == 'I am a JS Confirm'
    
    
    driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button").click()
    obj = driver.switch_to.alert
    obj.send_keys('vv')
    obj.accept
    msg=obj.text
    assert msg == 'I am a JS prompt'

    driver.close()
    

def selection()->None:
    "registration test"
    driver = webdriver.Firefox(executable_path=path) 
    driver.get('https://demo.guru99.com/test/newtours/register.php')
    driver.find_element(By.NAME, "firstName").send_keys("Vered")
    driver.find_element(By.NAME, "lastName").send_keys("Aharonov")
    driver.find_element(By.NAME, "phone").send_keys("0535226619")
    driver.find_element(By.ID, "userName").send_keys("vered@gmail.com")
    driver.find_element(By.NAME, "address1").send_keys("Levi 1")
    driver.find_element(By.NAME, "city").send_keys("HADERA")
    driver.find_element(By.NAME, "state").send_keys("LA")
    driver.find_element(By.NAME, "postalCode").send_keys("123456")
    country = driver.find_element(By.NAME, "country")
    select = Select(country)
    select.select_by_value('ARMENIA')
    driver.find_element(By.NAME, "email").send_keys("vered@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "confirmPassword").send_keys("123456")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(5)
    register = driver.find_elements(By.TAG_NAME, "b")[2]
    assert 'Vered Aharonov' in register
    driver.close()
    
    

    

