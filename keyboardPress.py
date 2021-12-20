# filename: keyboard_keys.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class KeyboardKeys(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()
        
    def test_example_1(self):
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/key_presses')
        driver.find_element_by_class_name('example').send_keys(Keys.SPACE)
        assert driver.find_element_by_id('result').text == 'You entered: SPACE'
        ActionChains(driver).send_keys(Keys.TAB).perform()
        assert driver.find_element_by_id('result').text == 'You entered: TAB'
        
    def action_builder(self):
        # ...
        ActionChains(driver).send_keys(Keys.TAB).perform()
        assert driver.find_element_by_id('result').text == 'You entered: TAB'


if __name__ == "__main__":
    unittest.main()
