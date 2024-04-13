from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('User can navigate to the target circle page')
def open_target_main(context):
    # open target
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com")
    sleep(4)


@when('Click on an item and add to cart')
def user_clicks_item(context):
    # By tag.class
    target_shop_household = context.driver.find_element(By.CSS_SELECTOR, 'a[@href = "/c/household-essentials/-/N-5xsz1"')
    target_shop_household.click()
    sleep(4)

    target_laundry = context.driver.find_element(By.CSS_SELECTOR, 'a[@href = "/c/laundry-care-household-essentials/-/N-5xsyr"')
    target_laundry.click()
    sleep(4)

    target_item = context.driver.find_element(By.CSS_SELECTOR, 'id["addToCartButtonOrTextIdFor87469578"]')
    target_item.click()
    sleep(4)


@then('Go to cart')
def go_to_cart(context):
    cart = context.driver.find_element(By.XPATH, 'a[@href"/cart"]')
    cart.click()
    sleep(4)

@then('Verify item in cart')
def verify_item(context):
    verify_1 = context.driver.find_element(By.XPATH, 'div[data-test="collapsibleContentDiv"]')
    if verify_1 == "Total":
        print("test passed")
    sleep(2)
    context.quit()

