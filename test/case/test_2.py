# --coding: utf-8--
import unittest

from selenium import webdriver
from time import sleep

URL = "https://lanrenao.com/"


class LanRen2(unittest.TestCase):
    """懒人导航关于测试"""

    def setUp(self):
        self.driver = webdriver.Edge()
        sleep(2)
        self.driver.get(URL)

    def tearDown(self):
        self.driver.quit()

    def test_GuanYu(self):
        #  关于本站测试
        self.driver.find_element(by="id", value="menu-item-10").click()
        sleep(2)
        self.assertEqual(self.driver.title, "关于本站 | 懒人导航网", "title错误")


if __name__ == "__main__":
    unittest.main(verbosity=2)
