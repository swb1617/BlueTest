# 导包
import unittest

from unittestreport import TestRunner


# 构建测试集
def suite():
    # 创建一个测试套件
    suites = unittest.TestSuite()
    # 将测试用例加载到测试套件中
    loader = unittest.TestLoader()  # 创建一个用例加载对象
    # suites.addTest(loader.loadTestsFromTestCase(TestUI))
    return suites


if __name__ == '__main__':
    report = TestRunner(suite())
    report.run()
