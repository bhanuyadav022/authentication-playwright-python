import pytest
from config_manager import load_config
from playwright.sync_api import sync_playwright
from pages.index_page import IndexPage
from pages.login_page import LoginPage
import time

config_data = load_config()

@pytest.fixture()
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture()   
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture()
def login_fixture (page):
    login_page = LoginPage(page,config_data)
    login_page.navigate_login()
    login_page.authenticate()

@pytest.fixture()   
def auth_context(browser):
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page, config_data)
    login_page.navigate_login()
    login_page.authenticate()
    storage = context.storage_state(path="state.json")
     
@pytest.fixture() 
def page_after_loggedIn (browser):
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    yield page
    page.close()
