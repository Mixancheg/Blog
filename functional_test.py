from selenium import webdriver
import unittest

class BasicInstallTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Edge()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Блог Михаила Егошина', self.browser.title)
        # self.fail('Finish the test!')

    def test_home_page_header(self):
        browser = self.browser.get('http://127.0.0.1:8000')
        header = browser.find_elements_by_tag_name('h1')[0]
        self.assertIn('Михаил Егошин', header)
        # self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()