from playwright.sync_api import Page

from pages.pages_obj.basepage import BasePage


class Homepage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
