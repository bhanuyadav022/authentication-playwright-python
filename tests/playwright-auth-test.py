import pytest 
import time
from pages.index_page import IndexPage
from config_manager import load_config

config_data = load_config()

def test_goto_dashboard (auth_context, page_after_loggedIn):
    index_page = IndexPage(page_after_loggedIn, config_data['hostname'])
    index_page.navigate_index()


def test_goto_admin_page (page_after_loggedIn):
    index_page = IndexPage(page_after_loggedIn, config_data['hostname'])
    index_page.navigate_pim()


def test_goto_recruitment_page ():
    pass