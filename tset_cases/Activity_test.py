import unittest
from Base.web_base_driver import WebBaseDriver
from page.Activity_support import Activity
from page.Basics import Basics
from tset_cases.Data_treating import Data_Treating
from Base.Connect_mysql import ConnectMysql


class Activity_test(unittest.TestCase):
    result = None
    sheet_name = 'result'
    DL_URL = "http://192.168.10.32:8081/login.html"
    Cn_db = ConnectMysql()
    get_basics = Basics()
    #################################################
    act_num = 1042

    def setUp(self):
        self.driver = WebBaseDriver("Chrome")
        self.driver.implicitly_wai(5)
        self.driver.maximize_window()
        self.act = Activity(self.driver)
        self.data_Treat = Data_Treating()

    def tearDown(self):
        print('###############################################')
        self.driver.sleep(3)
        self.driver.quit_browser()

    def test_01(self):
        """invite_friends"""
        self.rg_pwd = 'a1234567'
        data = self.data_Treat.read_content('活动邀请好友', self.sheet_name)
        self.a = 0
        self.if_list = []
        self.data_Treat.create_table('邀请好友')
        for i in data:
            rg_phone = self.get_basics.random_phone()
            array = i.split('-')
            self.act.invite_friends(array[0], rg_phone, self.rg_pwd)
            if array[3] == 1:
                self.result = 'error'
            else:
                self.result = 'pass'
            id_sql = self.get_basics.hy_id_sql % rg_phone
            chance_sql = self.get_basics.hy_chance_sql % rg_phone
            id_result = self.Cn_db.connect_db(self.act.login_hj(), id_sql)
            chance_result = self.Cn_db.connect_db(self.act.login_hj(), chance_sql)
            self.if_list.extend([array[0],
                                 id_result.__str__(),
                                 chance_result.__str__(),])
            self.data_Treat.write_head(self.get_basics.if_head)
            self.data_Treat.write_content(self.if_list,
                                          self.result,
                                          self.a)
            self.if_list.clear()
        self.data_Treat.close()

    def test_02(self):
        """at_recharge"""
        ######################  读取
        data = self.data_Treat.read_content('活动充值', self.sheet_name)
        self.a = 0
        self.if_list = []
        self.data_Treat.create_table('活动充值')
        for i in data:
            print(i)
            self.a = self.a + 1
            array = i.split('-')
            self.act.at_recharge(array[0], array[1], array[2], array[3], array[4])
            if array[4] == 'pass':
                self.result = 'pass'
            else:
                self.result = 'error'
            cz_wb_sql = self.get_basics.cz_wb_sql % (array[2], self.act_num)
            cz_wb_result = self.Cn_db.connect_db(array[0], cz_wb_sql)
            ######################  写入
            self.if_list.extend([array[2],
                                 array[3]+'(%r)' % array[1],
                                 cz_wb_result.__str__(),
                                 ])
            self.data_Treat.write_head(self.get_basics.at_recharge_head)
            self.data_Treat.write_content(self.if_list,
                                          self.result,
                                          self.a)
            self.if_list.clear()
        self.data_Treat.close()

    def test_03(self):
        """at_withdraw"""
        ######################  读取
        data = self.data_Treat.read_content('活动提现', self.sheet_name)
        self.a = 0
        self.if_list = []
        self.data_Treat.create_table('活动提现')
        for i in data:
            self.a = self.a + 1
            array = i.split('-')
            self.act.at_withdraw(array[0], array[1], array[2], array[3], array[4])
            if array[4] == 'pass':
                self.result = 'pass'
            else:
                self.result = 'error'
            tx_wb_sql = self.get_basics.tx_wb_sql % (array[2], self.act_num)
            tx_wb_result = self.Cn_db.connect_db(array[0], tx_wb_sql)
        ######################  写入
            self.if_list.extend([array[2],
                                 array[3] + '(%r)' % array[1],
                                 tx_wb_result.__str__(),
                                 ])
            self.data_Treat.write_head(self.get_basics.at_withdraw_head)
            self.data_Treat.write_content(self.if_list,
                                          self.result,
                                          self.a)
            self.if_list.clear()
        self.data_Treat.close()

    def test_04(self):
        """investment"""
        ######################  读取
        data = self.data_Treat.read_content('活动投资', self.sheet_name)
        self.a = 0
        self.if_list = []
        self.data_Treat.create_table('活动投资')
        for i in data:
            self.a = self.a + 1
            array = i.split('-')
            self.act.at_investment(array[0], array[1], array[2], array[3], array[4])
            if array[4] == 'pass':
                self.result = 'pass'
            else:
                self.result = 'error'
            tx_wb_sql = self.get_basics.tx_wb_sql % (array[2], self.act_num)
            tx_wb_result = self.Cn_db.connect_db(array[0], tx_wb_sql)
        ######################  写入
            self.if_list.extend([array[2],
                                 array[3] + '(%r)' % array[1],
                                 tx_wb_result.__str__(),
                                 ])
            self.data_Treat.write_head(self.get_basics.at_investment_head)
            self.data_Treat.write_content(self.if_list,
                                          self.result,
                                          self.a)
            self.if_list.clear()
        self.data_Treat.close()

