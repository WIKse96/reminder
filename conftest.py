import pytest
from playwright.sync_api import Page
from pages.pages_obj.homepage import Homepage

@pytest.fixture()
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        # 'storage_state': './state.json',
        'viewport': {
            'width': 1200,
            'height': 1080,
        },


    }
@pytest.fixture()
def home_page(page: Page):
    return Homepage(page)