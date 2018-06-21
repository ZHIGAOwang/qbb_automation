import unittest
import time
from selenium.webdriver.common.keys import Keys
from Base.web_base_driver import WebBaseDriver
from page.Qbb_front import Qbb_Front
from page.Qbb_pa_front import Qbb_Pafront
from tset_cases.Data_treating import Data_Treating


class QbbSceneTest(unittest.TestCase):
    QBB_HTURL = "http://192.168.10.31:8084/qian88_admin/tologin.action"
    DL_URL = "http://192.168.10.31:8080/tologin.html"
    PRO_DLURL = "http://192.168.10.135:8080/logout.html"
    QBB_JT = "picture\\ QBB_%s_%s.png"
    filename = 'zhuc_Result_06.07-09.52.23'
    sheet_name = 'result'
###############
    user_name = '322272qbb'
    user_pwd = '654321'
###############
    user_phone = '17302646415'
    ts_pwd = '654321'
    pa_ts_pwd = 'a12345'
###############
    recharge_money = 200
    withdraw_money = 200
    order_status = 'x,//*[@id="context"]/div/table/tbody/tr[2]/td[7]'
    bank_mun = 1
    pa_phone = 18322272123
###############
    bid_title = 'ZADB20180411000059'
    investment_money = 200
    result = 'pass'

    def setUp(self):
        self.driver = WebBaseDriver("Chrome")
        self.driver.navigate(self.DL_URL)
        self.driver.implicitly_wai(5)
        self.driver.maximize_window()
        self.front = Qbb_Front(self.driver)
        self.pa_front = Qbb_Pafront(self.driver)
        self.data_Treat = Data_Treating()

    def tearDown(self):
        print('###############################################')
        self.driver.sleep(3)
        self.driver.quit_browser()

    def test_01(self):
        """普通登录充值投资提现流程"""
        self.front.login(self.PRO_DLURL, self.user_name, self.user_pwd)
        self.front.recharge(self.recharge_money, self.result)
        self.front.bid_investment(self.investment_money, 'PRO', self.ts_pwd)
        self.front.withdraw(self.bank_mun, self.withdraw_money, self.ts_pwd, self.result)

    def test_02(self):
        """存管登录充值投资提现流程"""
        self.front.login(self.PRO_DLURL, self.user_name, self.user_pwd)
        self.pa_front.pa_recharge(self.recharge_money,self.pa_ts_pwd, self.result)
        self.pa_front.pa_bid_investment(self.investment_money, 'PRO', self.pa_phone, self.pa_ts_pwd)
        self.driver.driver.back()
        self.driver.driver.back()
        self.pa_front.pa_withdraw(self.withdraw_money, self.pa_ts_pwd, self.pa_phone, self.result)

    def test_03(self):
        """新用户普通充值投资提现流程"""
        self.front.login(self.PRO_DLURL, self.user_name, self.user_pwd)
        self.front.recharge(self.recharge_money, self.result)
        self.front.bid_investment(self.investment_money, 'PRO', self.ts_pwd)
        self.front.withdraw(self.bank_mun, self.withdraw_money, self.ts_pwd, self.result)

    def test_04(self):
        """新用户存管开户充值投资提现流程"""
        pass


if __name__ == '__main__':
    unittest.main()
