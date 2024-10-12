from playwright.sync_api import Page, expect
import pytest
from time import sleep
import allure
from allure_commons.types import AttachmentType

def test_successLogin(page: Page):   
    page.goto("https://saucedemo.com")
    
    page.locator('//input[@placeholder="Username"]').fill('standard_user')
    page.locator('[data-test="password"]').fill('secret_sauce')
    page.locator('[id="login-button"]').click()
    
    expect(page).to_have_title("Swag Labs")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    inventory_page_title = page.locator("//div[@class='app_logo']").text_content()
    assert inventory_page_title == 'Swag Labs'
    allure.attach(page.screenshot(),name="success login", attachment_type=AttachmentType.PNG)
    sleep(2)
    
    page.close()

test = [
        ('standar_user','','Epic sadface: Password is required'),
        ('','secret_sauce','Epic sadface: Username is required'),
        ('standar_user','invalid','Epic sadface: Username and password do not match any user in this service'),
        ('invalid','secret_sauce','Epic sadface: Username and password do not match any user in this service'),
        ('','','Epic sadface: Username is required')
        ]

@pytest.mark.parametrize('username, password, error' , test)    
def test_invalid_login(page: Page,username, password, error_message):
    page.goto("https://saucedemo.com")
    
    page.locator('//input[@placeholder="Username"]').fill(username)
    page.locator('[data-test="password"]').fill(password)
    page.locator('[id="login-button"]').click()    
    
    get_error_message_text = page.locator('[data-test="error"]').inner_text()
    
    assert get_error_message_text == error_message
    allure.attach(page.screenshot(),name="invalid login", attachment_type=AttachmentType.PNG)
    sleep(2)
    
    page.close()