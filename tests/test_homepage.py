import pytest
from pages.pages_obj.homepage import Homepage


def test_homepage(home_page: Homepage):
    home_page.load('')
