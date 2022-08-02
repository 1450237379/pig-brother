from selenium import webdriver


class BasePage(object):
    """page对象都继承的基类
    基础page层、封装一些常用方法"""

    def __init__(self, driver):
        self.driver = driver

    # 打开页面，如果为None，则继承子类的url，否则用url
    def open_url(self, url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    # id定位
    def by_id(self, id):
        return self.driver.find_element(by="id", value=id)

    # class定位
    def by_class(self, classname):
        return self.driver.find_element(by="class_name", value=classname)

    # name定位
    def by_name(self, name):
        return self.driver.find_element(by="name", value=name)

    # XPath定位
    def by_xpath(self, xpath):
        return self.driver.find_element(by="xpath", value=xpath)

    # 获取title
    def get_title(self):
        return self.driver.title

    # 切换新窗口
    def switch_new_window(self):
        all_window = self.driver.window_handles
        self.driver.switch_to.window(all_window[1])
