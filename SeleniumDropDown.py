import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select as WebDriverSelect

class DropDown(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()
    
    def test_example_1(self):
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/dropdown')
        dropdown_list = driver.find_element_by_id('dropdown')
        options = dropdown_list.find_elements_by_tag_name('option')
        for opt in options:
            if opt.text == 'Option 1':
                opt.click()
                break
        for opt in options:
            if opt.is_selected():
                selected_option = opt.text
                break
        assert selected_option == 'Option 1', "Selected option should be Option 1"
    
    def test_example_2(self):
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/dropdown')
        dropdown = driver.find_element_by_id('dropdown')
        select_list = WebDriverSelect(dropdown)
        select_list.select_by_visible_text('Option 1')
        selected_option = select_list.first_selected_option.text
        assert selected_option == 'Option 1', "Selected option should be Option 1"

if __name__ == "__main__":
    unittest.main()
