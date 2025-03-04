from playwright.sync_api import Page
# from pages.locators.base_page_locators import BasePageLocators


class BasePage:
    URL: str
    URL = 'https://www.meestpost.com/'

    def __init__(self, page: Page) -> None:
        self.page = page

    def load(self, path: str = '') -> None:
        full_url = f'{self.URL}/{path}'  # Pełny adres URL
        self.page.goto(full_url)
