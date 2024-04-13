from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main(context):
    # open target
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com")
    sleep(4)


@when('click on circle to open target circle page')
def user_clicks_circle(context):
    # By tag.class
    target_circle = context.driver.find_element(By.CSS_SELECTOR, 'div.styles_baseCell__LIwYV')
    target_circle.click()
    sleep(4)


@then('verify on target circle page')
def verify_circle(context):
    verify_text = context.driver.find_element(By.XPATH, 'div[styles__StyledHeading-sc-1xmf98v-0]')
    sleep(2)

    if verify_text == "The free & easy way to get the most deals at Target":
        print("test passed")

    context.quit()