import pytest
import logging
from playwright.sync_api import sync_playwright


#I couldn't run the tests to see if they work because playwrghit does not work on my computer

logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()

def open():
 "finction opens the clothing store site"
 with sync_playwright() as p :
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("http://automationpractice.com/index.php?controller=authentication&back=my-account")
    return page

def test_correct_details():
    "test for correct details"
    mylogger.info("test for correct details")
    page = open()
    page.locator('id=email').fill('vered@gmail.com')
    page.locator('id=passwd').fill('123456')
    page.locator('id=SubmitLogin').click()
    assert page.title() == 'My account - My Store'


def test_empty_email():
    "test for empty email"
    mylogger.info("test for empty email")
    page = open()
    page.locator('id=passwd').fill('123456')
    page.locator('id=SubmitLogin').click()
    assert page.title() == 'Login - My Store'

def test_empty_passwd():
    "test for empty passwoed"
    mylogger.info("test for empty passwoed")
    page = open()
    page.locator('id=email').fill('vered@gmail.com')
    page.locator('id=SubmitLogin').click()
    assert page.title() == 'Login - My Store'

def test_empty_fildes():
    "test for empty fields"
    mylogger.info("test for empty fields")
    page = open()
    page.locator('id=SubmitLogin').click()
    assert page.title() == 'Login - My Store'


def test_worng_passwd():
    "test for wrong password"
    mylogger.info("test for wrong password")
    page = open()
    page.locator('id=email').fill('vered@gmail.com')
    page.locator('id=passwd').fill('12')
    page.locator('id=SubmitLogin').click()
    assert page.title() == 'Login - My Store'

def test_worng_email():
    "test for wrong email"
    mylogger.info("test for wrong email")
    page = open()
    page.locator('id=email').fill('ve@gmail.com')
    page.locator('id=passwd').fill('123456')
    page.locator('id=SubmitLogin').click()
    assert page.title() == 'Login - My Store'

def test_forgat_passwd():
    "test for forget password"
    mylogger.info("test for forget password")
    page = open()
    page.locator('text="Forgot your password?"').click()
    assert page.title() == 'Forgot your password - My Store'


def test_find_dress():
    "test to buy cheapest dress"
    mylogger.info("test to buy cheapest dress")
    driver = open()
    page = open()
    page.locator('id=email').fill('vered@gmail.com')
    page.locator('id=passwd').fill('123456')
    page.locator('id=SubmitLogin').click()
    page.wait_for_timeout(15)
    assert driver.title == 'My account - My Store'
    page.locator('id=search_query').fill('summer')
    page.locator('id="submit_search"').click()
    page.wait_for_timeout(15)
    product_list = page.query_selector_all(".product-container")
    price = {}
    for product in product_list:
        price = product.query_selector(".product-price").text_content().strip()
        price[price] = product
    low = min(price.keys())
    price[low].dblclick()
    price[low].query_selector('.ajax_add_to_cart_button').click()
    page.wait_for_timeout(3)
    page.locator("text=Proceed to checkout").click()
    page.locator('id=cgv').click()
    page.locator('text=Proceed to checkout').last.click()
    page.locator('text=Pay by bank wire').last.click()
    page.locator('text=Proceed to checkout').last.click()
    page.locator('.cart_navigation').click()
    page.locator('xpath=//*[@id="cart_navigation"]/button').click()
    assert page.title()=="Order confirmation - My Store" 

