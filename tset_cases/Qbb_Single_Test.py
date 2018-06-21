import unittest
import time
from selenium.webdriver.common.keys import Keys
from Base.web_base_driver import WebBaseDriver
from page.Qbb_front import Qbb_Front
from page.Qbb_pa_front import Qbb_Pafront
from tset_cases.Data_treating import Data_Treating


class QbbSingleTest(unittest.TestCase):
    result = None
    QBB_HTURL = "http://192.168.10.31:8084/qian88_admin/tologin.action"
    QBB_URL = "http://192.168.10.32:8081"
    DL_URL = "http://192.168.10.32:8081/login.html"
    PRO_URL = "http://192.168.10.135:8080"
    PRO_DLURL = "http://192.168.10.135:8080/logout.html"
    QBB_JT = "picture\\ QBB_%s_%s.png"
    filename = 'zhuc_Result_06.07-09.52.23'
    sheet_name = 'result'
    head_list = ['url（注册网址）','userid/relevanceId','luckcd',	'邀请好友是否给活动机会']
###############
    user_name = '311152qbb'
    user_pwd = '654321'
    pa_name = '322228qbb'
    pa_pwd = '654321'
###############
    user_phone = '17302646415'
    yzm = '123456'
    pwd = 'a1234567'
    repwd = 'a1234567'
    ts_pwd = '654321'
    pa_ts_pwd = 'a12345'
###############
    recharge_money = 200
    withdraw_money = 200
    bank_mun = 1
    band_card = 6217680304046050
    pa_phone = 17302646411
###############
    bid_title = 'ZADB20180411000059'
    bid = 20180411000059
    pa_bid = 20180529000007
    investment_money = 500

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
        """登录"""
        data = self.data_Treat.read_content(self.filename, self.sheet_name)
        self.a = 0
        dl_list = []
        self.data_Treat.create_table('登录')
        for i in data:
            self.front.login(self.DL_URL, i.split('-')[0], i.split('-')[1])
            url = self.driver.get_url()
            print(url, self.DL_URL)
            if url == self.DL_URL:
                self.result = 'error'
            else:
                self.result = 'pass'
                # self.driver.click('logout')
                self.driver.navigate(self.DL_URL)
            self.a = self.a+1
            print(self.a)
            dl_list.extend([i.split('-')[0],
                            i.split('-')[0] + ' ,' + i.split('-')[1],
                            i.split('-')[1]])
            self.data_Treat.write_head(self.head_list)
            self.data_Treat.write_content(dl_list,
                                          self.result,
                                          self.a)
            dl_list.clear()
        self.data_Treat.close()

    def test_02(self):
        """注册用户"""
        self.front.qbb_register_tzr(self.user_phone, self.yzm, self.pwd, self.repwd)

    def test_03(self):
        """普通充值"""
        self.front.login(self.DL_URL, self.user_name, self.user_pwd)
        self.driver.navigate(self.QBB_URL)
        self.front.recharge(self.recharge_money, 'pass')

    def test_04(self):
        """普通提现"""
        self.front.login(self.DL_URL, self.user_name, self.user_pwd)
        self.driver.navigate(self.QBB_URL)
        self.front.withdraw(self.bank_mun, self.withdraw_money, self.ts_pwd)

    def test_05(self):
        """普通投资"""
        self.front.login(self.DL_URL, self.user_name, self.user_pwd)
        self.driver.navigate(self.QBB_URL)
        self.front.bid_investment(self.investment_money, 'CS', self.ts_pwd, bid=self.bid)

    def test_06(self):
        """存管充值"""
        self.pa_front.login(self.PRO_DLURL, self.pa_name, self.pa_pwd)
        self.driver.navigate(self.PRO_URL)
        self.pa_front.pa_recharge(self.recharge_money, self.pa_ts_pwd, 'pass')

    def test_07(self):
        """存管提现"""
        self.pa_front.login(self.PRO_DLURL, self.pa_name, self.pa_pwd)
        self.driver.navigate(self.PRO_URL)
        self.pa_front.pa_withdraw(self.withdraw_money, self.pa_ts_pwd, self.pa_phone)

    def test_08(self):
        """存管投资"""
        self.pa_front.login(self.PRO_DLURL, self.pa_name, self.pa_pwd)
        self.driver.navigate(self.PRO_URL)
        self.pa_front.pa_bid_investment(self.investment_money, 'PRO', self.pa_phone, self.pa_ts_pwd, bid=self.pa_bid)


if __name__ == '__main__':
    unittest.main()


