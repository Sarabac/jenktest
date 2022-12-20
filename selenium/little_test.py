from selenium import webdriver
import unittest

class GoogleTest(unittest.TestCase):
    def setUp(self) -> None:
        remote_url = "http://selenium-hub:4444/wd/hub"
        print(remote_url)
        self.browser = webdriver.Remote("http://selenium-hub:4444/wd/hub", options=webdriver.ChromeOptions())
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn("Google", self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)