import unittest
from test.case.test_2 import LanRen2
from test.case.test_lanrenao import TestLanrenao
from XTestRunner import HTMLTestRunner

# LanRen1_test = unittest.TestLoader().loadTestsFromTestCase(LanRen1)
# LanRen2_test = unittest.TestLoader().loadTestsFromTestCase(LanRen2)
lanren_test = unittest.TestLoader().loadTestsFromTestCase(TestLanrenao)
all_test = unittest.TestSuite(lanren_test)

outfile = open("./report/selenium_result.html", "wb")

runner = HTMLTestRunner(stream=outfile,
                        verbosity=2,
                        title="测试",
                        tester="张子龙",
                        description="测试罢了",
                        save_last_run=True,
                        language="zh-CN"
                        )
runner.run(all_test,rerun=2,save_last_run=True)
# unittest.TextTestRunner(verbosity=2).run(all_test)
