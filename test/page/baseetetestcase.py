import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    """用来给我们提供setUp和tearDown两种方法"""
    def setUp(self) -> None:
        # 打开EDGE浏览器
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # 访问网址
        self.driver.get("https://lanrenao.com/")

    def tearDown(self) -> None:
        # 闭浏览器
        self.driver.quit()
