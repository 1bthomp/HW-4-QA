from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_target_main(context):
    # open target
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com")
    sleep(4)
    click_sign_in = context.find_element(By.CSS_SELECTOR, 'div.styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3')
    click_sign_in.click()
    sleep(4)


def user_clicks_signin(context):
    # By tag.class
    signin_nav = context.driver.find_element(By.CSS_SELECTOR, 'div.styles__StyledLink-sc-vpsldm-0 styles__ListLink-sc-diphzn-2 fkwerm gcgPXN')
    signin_nav.click()


def signin_page(context):
    verify_text = context.driver.find_element(By.CSS_SELECTOR, 'div.styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa').text

    sleep(2)

    assert verify_text == "Sign into your account", f'Expected Sign into your account but got verify_text'
