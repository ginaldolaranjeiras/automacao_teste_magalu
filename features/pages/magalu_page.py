from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from behave.formatter import null

class MagaluPage:
    def __init__(self, url, path):
        super().__init__()
        self.url = url
        self.path = path
        self.driver = webdriver.Chrome(path)

    def open_page(self):
        page = self.driver.get(self.url)
        return page

    def fill_search_text(self, id, text):
        element = self.driver.find_element_by_id(id)
        element.send_keys(text)
        return element

    def search_click(self, id):
        button = self.driver.find_element_by_id(id).click()
        return button

    def check_elements(self, xpath):
        elements = self.driver.find_elements_by_xpath(xpath)
        assert type(elements) is list
        assert elements is not null
        return elements
