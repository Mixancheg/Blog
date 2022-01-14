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
        self.browser.get('http://127.0.0.1:8000')
        # тут ошибка
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Михаил Егошин', header.text)
        # self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()