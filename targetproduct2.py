from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('User can navigate to the target circle page')
def open_target_main(context):
    # open target
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com/l/target-circle/-/N-pzno9")
    sleep(4)


@when('open target circle page')
def user_opens_target_circle(context):
    # By tag.class
    target_circle = context.driver.find_element(By.CSS_SELECTOR, 'div.styles_baseCell__LIwYV')
    target_circle.click()

    sleep(4)


@then('verify there are 10 benefit cells')
def verify_circle_cells(context):
    # Verify 10 circle cells on page
    verify_1 = context.driver.find_element(By.XPATH, 'div[data-component-type="Cells"')
    sleep(2)

    verify_2 = context.driver.find_element(By.XPATH, 'div[styles__CellsComponentContainer-sc-3f68hg-0 dIIpte]')
    sleep(2)

    verify_3 = context.driver.find_element(By.XPATH, 'div[styles__CellsComponentContainer-sc-3f68hg-0 dIIpte]')
    sleep(2)

    if verify_1 == "Join Target Circle" & "See today's Target Circle deals" & "Target Circle Bonuses" & "Target Circle Partners" & "Community support votes" & "Frequently asked questions":
        print("test passed")

    if verify_2 == "Find a card right for you" & "Frequently asked questions":
        print("test passed")

    if verify_3 == "Save time with Same Day Delivery" & "Frequently asked questions":
        print("test passed")

    context.quit()

