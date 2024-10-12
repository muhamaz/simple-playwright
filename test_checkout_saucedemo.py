from playwright.sync_api import Page, expect
import pytest
from time import sleep
import allure
from allure_commons.types import AttachmentType


def test_example(page: Page) -> None:
    # go to page
    page.goto("https://www.saucedemo.com/")
    
    # Fill username and password
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    sleep(1)
    
    # Click login button
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"inventory-container\"]").click()
    sleep(1)
    
    # Assertion
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator("[data-test=\"inventory-container\"]")).to_be_visible()
    
    # Click add to cart button
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    sleep(1)
    
    # Click cart icon
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    sleep(1)
    
    # Assertion
    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Backpack")
    expect(page.locator("[data-test=\"inventory-item\"]")).to_be_visible()
    
    # Click checkout button
    page.locator("[data-test=\"checkout\"]").click()
    sleep(1)
    
    # Assertion
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    
    # Fill the firstName field
    page.locator("[data-test=\"firstName\"]").fill("test_user")
    
    # Fill the lastName field
    page.locator("[data-test=\"lastName\"]").fill("user_12345")
    
    # Fill the postalCode field
    page.locator("[data-test=\"postalCode\"]").fill("5638923")
    sleep(1)
    
    # Click continue button
    page.locator("[data-test=\"continue\"]").click()
    sleep(1)
    
    # Assertion
    expect(page.locator("[data-test=\"inventory-item\"]")).to_be_visible()
    
    subtotal = page.locator("[data-test='subtotal-label']").text_content()
    split_text = subtotal.split(':')
    getText_subtotal_price = split_text[1].strip().replace('$', '')
    
    sub_total_price = float(getText_subtotal_price)
    
    tax = page.locator("[data-test='tax-label']").text_content()
    split_text = tax.split(':')
    getText_tax = split_text[1].strip().replace('$', '')
    
    tax_price = float(getText_tax)
    
    total = page.locator("[data-test='total-label']").text_content()
    split_text = total.split(':')
    getText_total= split_text[1].strip().replace('$', '')
    
    total_price = float(getText_total)
    
    assert total_price == sub_total_price + tax_price
    sleep(1)
    
    # Click Finish button
    page.locator("[data-test=\"finish\"]").click()
    sleep(1)
    
    # Assertion
    expect(page.locator("[data-test='back-to-products']")).to_be_enabled()
    
    # Click Back Button
    page.locator("[data-test=\"back-to-products\"]").click()
    sleep(1)
    
    # Assertion
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    page.close()
