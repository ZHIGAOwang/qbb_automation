import unittest
import datetime
from Base.html_test_runner import HtmlTestRunner
from tset_cases.Activity_test import Activity_test
from tset_cases.Qbb_Scene_Test import QbbSceneTest
from tset_cases.Qbb_Single_Test import QbbSingleTest


class QbbTestRunner(object):

    def run_single(self):
        """
        创建测试套件和生成测试报告
        :return: 
        """
        time_stamp = datetime.datetime.now()
        time = time_stamp.strftime('%Y.%m.%d-%H.%M.%S')
        # 实例化Testsuite类，切记不要漏掉后面的括号
        test_suite = unittest.TestSuite()
        # 添加类下面的测试用例
        test_suite.addTest(QbbSingleTest("test_01"))
        test_suite.addTest(QbbSingleTest("test_02"))
        test_suite.addTest(QbbSingleTest("test_03"))
        test_suite.addTest(QbbSingleTest("test_04"))
        test_suite.addTest(QbbSingleTest("test_05"))
        test_suite.addTest(QbbSingleTest("test_06"))
        test_suite.addTest(QbbSingleTest("test_07"))
        # 创建测试报告文件
        report_path = "report\\qbb_single_report_%s.html" % time
        report_file = open(report_path, mode="wb")
        # 实例化生成测试报告的HtmlTestRunner类
        test_runner = HtmlTestRunner(stream=report_file,
                                     title="qbb自动化测试报告",
                                     description="测试详情")
        # 运行套件内的测试用例
        test_runner.run(test_suite)


    def run_scene(self):
        """
        创建测试套件和生成测试报告
        :return:
        """
        time_stamp = datetime.datetime.now()
        time = time_stamp.strftime('%Y.%m.%d-%H.%M.%S')
        # 实例化Testsuite类，切记不要漏掉后面的括号
        test_suite = unittest.TestSuite()
        # 添加类下面的测试用例
        test_suite.addTest(QbbSceneTest("test_01"))
        test_suite.addTest(QbbSceneTest("test_02"))
        # 创建测试报告文件
        report_path = "report\\qbb_scene_report_%s.html" % time
        report_file = open(report_path, mode="wb")
        # 实例化生成测试报告的HtmlTestRunner类
        test_runner = HtmlTestRunner(stream=report_file,
                                     title="qbb-自动化测试报告",
                                     description="测试详情")
        # 运行套件内的测试用例
        test_runner.run(test_suite)

    def run_activity(self):
        """
        创建测试套件和生成测试报告
        :return:
        """
        time_stamp = datetime.datetime.now()
        time = time_stamp.strftime('%Y.%m.%d-%H.%M.%S')
        # 实例化Testsuite类，切记不要漏掉后面的括号
        test_suite = unittest.TestSuite()
        # 添加类下面的测试用例
        test_suite.addTest(Activity_test("test_01"))
        test_suite.addTest(Activity_test("test_02"))
        test_suite.addTest(Activity_test("test_03"))
        test_suite.addTest(Activity_test("test_04"))
        # 创建测试报告文件
        report_path = "report\\qbb_test_activity_%s.html" % time
        report_file = open(report_path, mode="wb")
        # 实例化生成测试报告的HtmlTestRunner类
        test_runner = HtmlTestRunner(stream=report_file,
                                     title="qbb自动化测试报告",
                                     description="测试详情")
        # 运行套件内的测试用例
        test_runner.run(test_suite)