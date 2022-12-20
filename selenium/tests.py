#!/usr/bin/env python3
"""Tests that the remote webdriver works."""
import unittest
from selenium import webdriver


class LocalGoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)


class RemoteGoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Remote(
            command_executor='http://chrome:4444/wd/hub')
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)


if __name__ == '__main__':
    
    unittest.main(verbosity=2)