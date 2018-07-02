import unittest
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
    rg_pwd = 'a1234567'
###############
    pa_ts_pwd = 'a12345'
###############
    recharge_money = 200
    withdraw_money = 200
    order_status = 'x,//*[@id="context"]/div/table/tbody/tr[2]/td[7]'
    bank_mun = 1
###############
    bid_title = 'ZADB20180411000059'
    investment_money = 200
    result = 'pass'

    def setUp(self):
        self.rg_phone = self.front.get_basics.random_phone()
        self.driver = WebBaseDriver("Chrome")
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
        """普通注册充值投资提现流程"""
        self.front.qbb_register_tzr(self.DL_URL, self.rg_phone, self.rg_pwd, self.rg_pwd)
        self.front.login(self.DL_URL, self.rg_phone, self.rg_pwd)
        self.front.recharge(self.recharge_money, self.result)
        self.front.bid_investment(self.investment_money, 'PRO', self.rg_pwd)
        self.front.withdraw(self.bank_mun, self.withdraw_money, self.rg_pwd, self.result)

    def test_02(self):
        """存管注册开户充值投资提现流程"""
        self.front.qbb_register_tzr(self.DL_URL, self.rg_phone, self.rg_pwd, self.rg_pwd)
        self.front.login(self.DL_URL, self.rg_phone, self.rg_pwd)
        self.pa_front.pa_recharge(self.recharge_money, self.pa_ts_pwd, self.result)
        self.pa_front.pa_bid_investment(self.investment_money, 'PRO', self.pa_ts_pwd)
        self.driver.driver.back()
        self.driver.driver.back()
        self.pa_front.pa_withdraw(self.withdraw_money, self.pa_ts_pwd, self.pa_phone, self.result)

    def test_03(self):
        """用户普通充值投资提现流程"""
        pass

    def test_04(self):
        """用户存管开户充值投资提现流程"""
        pass


if __name__ == '__main__':
    unittest.main()
