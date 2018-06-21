from selenium.webdriver.common.keys import Keys
from Base.Bd_AipOcr import Bd_AipOcr
from Base.web_base_driver import WebBaseDriver
from page.Basics import Basics
from page.Qbb_front import Qbb_Front


class Qbb_Pafront(Qbb_Front):
    get_phone = Basics()
###########################
    C_CGZH = 'l,存管账户'
    PA_TS_PWD = 'keyboards'
    C_QJZF = 'quickPayRadio'
    C_DXYZM = 'l,发送短信验证码'
    DXYZM = 'bindedCode'
    C_NTT = 'nextBtn'
    C_KTCG = 'pa_opdepoist'
    C_QRTK = 'optBtn'
    PA_CARD = 'accountNo'
    PA_TXYZM = 'verifyImg'
    PA_BANK = 'bankTypeSelect0'

###########################
    C_TJSQ = 'l,提交申请'
    C_HQYZM ='queryButton'
    TX_YZM = 'mobilePwd'
    C_DJ = 'submitButton'

    def pa_account(self, card, bank, phone, pa_ts_pwd):
        """平安存管开户"""
        judge = True
        bd = Bd_AipOcr()
        d = self.basepage
        d.driver.refresh()
        d.move_to(self.MV_WDZH)
        d.click(self.MV_WDZH)
        zh_url = d.get_url()
        d.sleep(1)
        try:
            d.click('x,/html/body/div[15]/div')
        except Exception:
            pass
        try:
            d.click(self.HD_CK)
        except Exception:
            pass
        d.click(self.C_KTCG)
        d.sleep(1)
        d.click(self.C_QRTK)
        # d.switch_to_frame('mainFrame')
        d.type(self.PA_CARD, card)
        d.move_to(self.PA_TXYZM)
        d.select_by_visible_text(self.PA_BANK, bank)
        d.type('phone', phone)
        while judge:
            yzm_mig = d.screenshot(self.PA_TXYZM, 2)
            d.sleep(1)
            yzm = bd.mig_get_yzn(yzm_mig)
            print(yzm)
            d.type('checkCodeText', yzm)
            d.sleep(2)
            d.click(self.C_HQYZM)
            aa = d.get_text('showMessage')
            # aa = d.get_text('mobilePwdNo')
            if len(aa) >= 1:
                judge = False
        d.type(self.TX_YZM, self.get_phone.get_yzm(phone) + Keys.TAB)
        d.type(self.PA_TS_PWD, pa_ts_pwd)
        d.type(self.PA_TS_PWD+'2', pa_ts_pwd)
        d.click('isRead')
        d.sleep(1)
        d.click(self.C_DJ)
        d.navigate(zh_url)

    def pa_recharge(self, money, pa_ts_pwd, result, if_new='old', dx_yzm=111111):
        '''
        存管充值
        :param money: 充值金额
        :param pa_ts_pwd: 存管交易密码
        :param dx_yzm: 短信验证码默认六个1
        :return:
        '''
        driver = self.basepage
        driver.driver.refresh()
        driver.move_to(self.MV_WDZH)
        driver.click(self.C_LJCZ)
        if if_new == 'new':
            self.new_user()
        driver.click(self.C_CGZH)
        driver.type(self.CZJE, money)
        now_handle = driver.current_window_handle()
        driver.open_new_window(self.C_MSCZ)
        driver.type(self.PA_TS_PWD, pa_ts_pwd)
        driver.sleep(1)
        driver.click(self.C_DJ)
        if if_new == 'new':
            self.pa_first_recharge()
        driver.click(self.C_QJZF)
        driver.click(self.C_DXYZM)
        driver.type(self.DXYZM, dx_yzm)
        if result != 'pass':
            pass
        else:
            driver.click(self.C_NTT)
        driver.close_browser()
        driver.driver.switch_to_window(now_handle)
        driver.click(self.C_WCCZ)

    def pa_withdraw(self, money, pa_ts_pwd, pa_phone, result, bk_num=0):
        '''
        存管提现
        :param bk_num: 第几张银行卡
        :param money: 提现金额
        :param pa_ts_pwd: 存管交易密码
        :param pa_phone: 存管手机号码
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
        try:
            driver.click(self.C_TXTS)
        except Exception:
            pass
        driver.click('l,存管提现')
        try:
            driver.click(self.C_TXTS)
        except Exception:
            pass
        driver.select_by_index(self.XZ_YHK, bk_num)
        driver.type(self.TXJE, str(money) + Keys.TAB)
        driver.click(self.C_TJSQ)
        try:
            driver.dismiss_alert()
        except Exception:
            pass
        driver.click(self.C_QD)
        driver.click(self.C_HQYZM)
        driver.type(self.TX_YZM, self.get_phone.get_yzm(pa_phone))
        driver.type(self.PA_TS_PWD, pa_ts_pwd)
        if result != 'pass':
            pass
        else:
            driver.click(self.C_DJ)
            driver.sleep(2)
            driver.driver.back()
        driver.driver.back()
        try:
            driver.click(self.C_TXTS)
        except Exception:
            pass
        driver.click(self.C_TXJL)

    def pa_bid_investment(self, money, hj, pa_phone, pa_ts_pwd, bid=None, bid_title=None):
        '''
        存管投资
        :param money: 投资金额
        :param hj: 投资环境
        :param pa_phone: 平安手机号码
        :param pa_ts_pwd: 存管交易密码
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
            driver.open_new_window(self.BID_CG)
        driver.type(self.TZJE, money)
        driver.click(self.C_TSS)
        driver.click(self.C_LJCJ)
        driver.click(self.C_HQYZM)
        driver.type(self.TX_YZM, self.get_phone.get_yzm(pa_phone))
        driver.type(self.PA_TS_PWD, pa_ts_pwd)
        driver.click(self.C_DJ)

    def pa_first_recharge(self):
        d = self.basepage
        d.click('addCard')
        d.click('x,//*[@id="unionPay"]/div')
        now_handle = d.current_window_handle()
        d.open_new_window('x,//*[@id="quickUnion"]/div/div')
        d.sleep(1)
        d.open_last_window()
        d.type('cardNumber', '6226602900000009')
        d.sleep(3)
        d.click('cellPhoneNumber')
        d.sleep(1)
        d.type('realName', '杰士塔威')
        d.type('credentialNo', '330100199005301551')
        d.type('cellPhoneNumber', 18100000003)
        d.click('btnGetCode')
        d.type('smsCode', '111111')
        d.click('btnCardPay')
        d.sleep(5)
        d.click('btnBack')
        d.driver.switch_to_window(now_handle)
        d.driver.refresh()


if __name__ == '__main__':
    QBB_PAURL = "http://192.168.10.31:8080/logout.html"
    driver = WebBaseDriver("Chrome")
    driver.implicitly_wai(5)
    driver.maximize_window()
    qd = Qbb_Pafront(driver)
    money = 200
    phone = 18355551123
    card = 6226602900000009
    bank = '中国光大银行'
    qd.login(QBB_PAURL, '355552qbb', '654321')
    ######################################################
    # qd.pa_recharge(money, 'a12345')
    # qd.pa_withdraw(money, 'a12345', phone,'pass')
    qd.pa_bid_investment(money, 'PRO', phone, 'a12345')
    # qd.pa_account(card, bank, phone, 'a12345')
    driver.sleep(10)
    driver.quit_browser()
