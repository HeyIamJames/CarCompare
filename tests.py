import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver("/chromedriver.exe"
        self.assertIn("none", driver.title)
        elem.send_keys("Ads")
        elem.send_keys(Keys.RETURN)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
