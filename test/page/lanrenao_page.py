# coding = utf8

from test.page.base import BasePage


class LanrenaoPage(BasePage):
    """懒人导航首页，将首页封装操作到的元素"""

    url = "https://lanrenao.com/"

    # 输入的搜索的内容
    def search_input(self,search_key):
        self.by_id("search-text").clear()
        self.by_id("search-text").send_keys(search_key)

    def search_button(self):
        self.by_xpath('//*[@id="search"]/form/button').click()

    def guanyubenzhan_top_button(self):
        self.by_id("menu-item-10").click()

    def shenqingshoulu_top_button(self):
        self.by_id("menu-item-2152").click()

    def lanrenBlog_top_button(self):
        self.by_id("menu-item-751").click()

    def paihangbang_top_button(self):
        self.by_id("menu-item-915").click()

    def liuyanban_top_button(self):
        self.by_id("menu-item-2158").click()