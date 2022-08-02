# coding = utf8
from test.page.lanrenao_page import LanrenaoPage
import unittest
from selenium import webdriver
from time import sleep


class TestLanrenao(unittest.TestCase):
    """懒人导航测试"""
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Edge()

    def test_search_key(self):
        """懒人导航首页搜索"""
        page = LanrenaoPage(self.driver)
        page.open_url()
        page.search_input("青岛")
        page.search_button()
        page.switch_new_window()
        sleep(2)
        self.assertEqual(page.get_title(), "“青岛”的搜索结果 | 懒人导航网", "title错误")

    def test_guanyubenzhan_top(self):
        """顶部关于本站"""
        page = LanrenaoPage(self.driver)
        page.open_url()
        page.guanyubenzhan_top_button()
        sleep(2)
        self.assertEqual(page.get_title(), "关于本站 | 懒人导航网", "title错误")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
