import pytest 
from pages.index_page import IndexPage
from config_manager import load_config

config_data = load_config()

def test_goto_dashboard (page, login_fixture):
    index_page = IndexPage(page, config_data['hostname'])
    index_page.navigate_index()


def test_goto_admin_page (page, login_fixture):
    index_page = IndexPage(page, config_data['hostname'])
    index_page.navigate_pim()
