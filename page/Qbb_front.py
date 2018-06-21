from selenium.webdriver.common.keys import Keys
from Base.Connect_mysql import ConnectMysql
from Base.basepage import BasePage
from Base.web_base_driver import WebBaseDriver


class Qbb_Front(BasePage):
    MV_WDZH = 'myzh'
    XZ_YHK = 'select_card'
    BID_URL = 'https://www.qian88.com/userCenter/queryInvestmentDetail.html?paramMap.id=%d&paramMap.fristLogin=-1'
    CS_BID_URL = 'http://192.168.10.32:8081/userCenter/queryInvestmentDetail.html?paramMap.id=%d&paramMap.fristLogin=-1'
    PRO_BID_URL = 'http://192.168.10.135:8080/userCenter/queryInvestmentDetail.html?paramMap.id=%d&paramMap.fristLogin=-1'
    DL_URL = "https://www.qian88.com/logout.html"
    sql = 'SELECT reserve from sys_sms_mt mt WHERE mt.mobile =%d ORDER BY create_time DESC LIMIT 1;'
    Cn_db = ConnectMysql()
###########################
    C_RG = 'l,立即注册'
    USER_PHONE = 'u_phone'
    C_YZM = 'sendBtnA'
    YZM = 'txcode'
    C_FS = 'sendcodebtn'
    C_GB = 'x,//*[@id="code_div"]/div[1]/div[1]/i'
    P_YZM = 'u_phone_code'
    PWD = 'pwdText'
    SD_PWD = 'pwd'
    PWD_QR = 'repwdText'
    SD_QRPWD = 'repwd'
    BM = 'c_value'
    C_TK = 'fwtk'
    C_ZC = 'l,立即注册'

###########################
    USER_NAME = 'userName'
    PASSWOED = 'password'
    C_LJDL = 'l,立即登录'

###########################
    C_LJCZ = 'l,立即充值'
    CZJE = 'fast_money'
    BK_CARD = 'fast_bank_card'
    C_MSCZ = 'l,马上充值'
    C_WCCZ = 'l,已完成充值'

###########################
    C_TX = 'l,提 现'
    HD_CK = 'x,/html/body/div[16]/div'
    C_TXTS = 'actTxClose'
    TXJE = 'txtmoney'
    JYMM = 'tradekey'
    C_TXSQ = 'drawBtn'
    C_QD = 'l,确定'
    C_TXJL = 'l,提现记录'

###########################
    BID_CG = 'x,//i[contains(text(),"庆存管")]'
    BID_TITLE = 'l,%s'
    TZJE = 'investmentMoney1'
    MV_CKGD = 'l,查看更多 >'
    TS_PWD = 'tradePassword'
    TZLB = 'x,/html/body/div[7]/div[4]/div/div[2]/div[%d]/div[1]/a'
    C_TSS = 'checkbox'
    C_LJCJ = 'btn_save btn'
    C_CJJL = 'l,查看我的出借记录'

    def qbb_register_tzr(self, user_phone, database, user_pwd, user_repwd, bm=1836):
        """
        投资人注册
        :param user_phone:注册手机号码
        :param database:注册的数据库pre=准生产，test=测试
        :param user_pwd:注册密码
        :param user_repwd:确认注册密码
        :param bm:服务编码
        :return:
        """
        driver = self.basepage
        try:
            driver.click(self.C_RG)
        except Exception:
            pass
        driver.type(self.USER_PHONE,user_phone)
        driver.click(self.C_YZM)
        driver.click(self.C_YZM)
        driver.type(self.YZM, 1234)
        driver.click(self.  C_FS)
        yzm = self.Cn_db.connect_db(database, self.sql % user_phone)
        print(yzm[0][0])
        self.Cn_db.disconnectDB()
        driver.type(self.P_YZM, yzm[0][0])
        driver.click(self.C_GB)
        driver.click(self.PWD)
        driver.type(self.SD_PWD, user_pwd)
        driver.click(self.PWD_QR)
        driver.type(self.SD_QRPWD, user_repwd)
        driver.type(self.BM, bm)
        driver.click(self.C_TK)
        driver.click(self.C_ZC )

    def qbb_register_jkr(self, user_phone, user_pwd, yzm):
        driver = self.basepage
        pass

    def login(self, dl_url, user_name, user_pwd):
        """
        登录
        :param dl_url: 登录网址
        :param user_name: 用户名
        :param user_pwd: 用户密码
        :return:
        """
        driver = self.basepage
        driver.navigate(dl_url)
        driver.type('userName', user_name + Keys.TAB)
        driver.type('password', user_pwd)
        driver.click('l,立即登录')
        driver.sleep(2)
        driver.navigate(dl_url.split('/l')[0])

    def recharge(self, money, result, user_no='old',  bank_card=0):
        """
        普通充值
        :param money: 充值金额
        :param result: 充值结果
        :param user_no: 是否是新用户
        :param bank_card: 充值银行卡
        :return:
        """
        driver = self.basepage
        driver.driver.refresh()
        driver.move_to(self.MV_WDZH)
        driver.click(self.C_LJCZ)
        if user_no == 'new':
            self.new_user()
        driver.type(self.CZJE, money)
        try:
            driver.type(self.BK_CARD, bank_card)
        except Exception:
            pass
        old_handle = driver.current_window_handle()
        driver.open_new_window(self.C_MSCZ)
        driver.type('iptMobile', 17300000001)
        driver.click('btnSms')
        driver.type('iptSmscode', '111111')
        if result != 'pass':
            pass
        else:
            driver.click('btnPay')
            driver.sleep(1)
        driver.close_browser()
        driver.driver.switch_to_window(old_handle)
        driver.click(self.C_WCCZ)

    def withdraw(self, bank_num, money, ts_pwd, result):
        '''
        普通提现
        :param bank_num: 选择提现银行卡
        :param money: 提现金额
        :param ts_pwd: 交易密码
        :return:
        '''
        driver = self.basepage
        driver.driver.refresh()
        driver.move_to(self.MV_WDZH)
        driver.click(self.MV_WDZH)
        driver.sleep(1)
        try:
            driver.click('x,/html/body/div[15]/div')
        except Exception:
            pass
        try:
            driver.click(self.HD_CK)
        except Exception:
            pass
        driver.click(self.C_TX)
        driver.click(self.C_TXTS)
        driver.select_by_index(self.XZ_YHK, bank_num)
        driver.type(self.TXJE, str(money) + Keys.TAB)
        if result != 'pass':
            ts_pwd = '1234'
            driver.type(self.JYMM, ts_pwd)
            driver.click(self.C_TXSQ)
            driver.sleep(1)
            driver.accept_alert()
        else:
            driver.type(self.JYMM, ts_pwd)
            driver.click(self.C_TXSQ)
            driver.click(self.C_QD)
        driver.click(self.C_TXJL)

    def bid_investment(self, money, hj, ts_pwd, bid=None, bid_title=None):
        '''
        普通投资
        :param money: 投资金额
        :param hj: 投资环境
        :param ts_pwd: 交易密码
        :param bid: 标的号(直接访问页面)
        :param bid_title: 标的标题(点击链接)
        :return:
        '''
        driver = self.basepage
        driver.driver.refresh()
        driver.click('indexTo')
        if bid is not None:
            if hj == 'test':
                driver.navigate(self.CS_BID_URL % bid)
            elif hj == 'pre':
                driver.navigate(self.PRO_BID_URL % bid)
            else:
                driver.navigate(self.BID_URL % bid)
        else:
            driver.sleep(3)
            driver.move_to(self.MV_CKGD)
            if bid_title is not None:
                driver.open_new_window(self.BID_TITLE % bid_title)
            driver.move_to(self.TZLB % 1)
            driver.open_new_window(self.TZLB % 1)
        driver.type(self.TZJE, money)
        if len(str(ts_pwd)) <= 5:
            print('This ts_pwd is error')
        else:
            driver.click(self.SD_PWD)
            driver.type(self.TS_PWD, ts_pwd)
        driver.click(self.C_TSS)
        driver.click(self.C_LJCJ)
        driver.click(self.C_CJJL)

    def new_user(self):
        """新用户风险测评"""
        driver = self.basepage
        driver.click('toFxTest')
        driver.sleep(2)
        for i in range(1, 11):
            l = driver.get_elements('x,//*[@id="q_%d"]/label/input' % i)
            l[3].click()
        driver.click('l,提交')
        driver.driver.back()
        driver.driver.refresh()

    def invest_read(self):
        """新用户投资须知"""
        driver = self.basepage
        driver.click('contiRead')
        driver.click('agreeRead')

if __name__ == '__main__':
    CS_URL = 'http://192.168.10.31:8080/logout.html'
    driver = WebBaseDriver("Chrome")
    card = 6222000200124846333
    qd = Qbb_Front(driver)
    driver.implicitly_wai(5)
    driver.maximize_window()
    money = 200
    bid = 20180509000359
    qd.login(CS_URL, '322277qbb', '654321')
    ####################################################
    qd.recharge(200, 'pass', 'new1', bank_card=card)
    # qd.withdraw(1, money, '654321', 'pass1')
    # qd.qbb_register_tzr(15173125421, 'test', 'a1234567', 'a1234567')
    # qd.bid_investment(money, 'PRO', '654321', bid=bid)
    # qd.new_user()
    # qd.invest_read()
    driver.sleep(10)
    driver.quit_browser()
