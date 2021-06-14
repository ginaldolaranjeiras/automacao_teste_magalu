from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from behave.formatter import null
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

class MagaluPage:
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.driver = webdriver.Chrome(path)

    def open_page(self, url):
        page = self.driver.get(url)
        self.driver.maximize_window()
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

    def click_element(self, xpath):
        btn = self.driver.find_element_by_xpath(xpath)
        btn.click()
        return btn

    def wait_visible(self, xpath):
        element_present = EC.presence_of_element_located((By.XPATH, xpath))
        WebDriverWait(self.driver, 5).until(element_present)
        return element_present

    def click_element_class(self, e_class):
        self.driver.find_element_by_class_name(e_class).click()

    def check_element(self, xpath):
        self.driver.find_element_by_xpath()