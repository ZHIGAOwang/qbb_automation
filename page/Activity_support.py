from Base.Connect_mysql import ConnectMysql
from Base.web_base_driver import WebBaseDriver
from page.Basics import Basics
from page.Qbb_pa_front import Qbb_Pafront


class Activity(Qbb_Pafront):
    Cn_db = ConnectMysql()
    get_basics = Basics()
    hj = "http://192.168.10.%d:8080/login.html"
    hj_url = None

    def invite_friends(self, rg_url, user_phone, user_pwd):
        self.qbb_register_tzr(rg_url, user_phone, user_pwd, user_pwd)

    def at_recharge(self, hj, is_host, user, money, result):
        login_url = self.hj % self.judge_hj(hj)
        self.login(login_url, '%sqbb' % user, '654321')
        if is_host == '2':
            self.pa_recharge(money, 'a12345', result)
        elif is_host == '0':
            self.recharge(money, result)
        else:
            print("please enter is_host again")

    def at_withdraw(self, hj, is_host, user, money, result):
        login_url = self.hj % self.judge_hj(hj)
        self.login(login_url, '%sqbb' % user, '654321')
        print(user)
        if is_host == '2':
            pa_user_phone = self.get_basics.get_pa_phone(hj, user)
            self.pa_withdraw(money, 'a12345', pa_user_phone, result)
        elif is_host == '0':
            self.withdraw(1, money, '654321', result)
        else:
            print("please enter is_host again")

    def at_investment(self, hj, is_host, user, money, bid):
        login_url = self.hj % self.judge_hj(hj)
        self.login(login_url, '%sqbb' % user, '654321')
        print(user)
        if is_host == '2':
            pa_user_phone = self.get_basics.get_pa_phone(hj, user)
            self.pa_bid_investment(money, hj, pa_user_phone, 'a12345', bid=bid)
        elif is_host == '0':
            self.bid_investment(money, hj, '654321', bid=bid)
        else:
            print("please enter is_host again")

    def judge_hj(self, hj):
        if hj == 'test':
            self.hj_url = 31
        elif hj == 'pre':
            self.hj_url = 135
        else:
            print("%s,Input error，Please enter the correct environment" % hj)
        return self.hj_url


if __name__ == '__main__':
    url = 'http://192.168.10.31:8080/userCenter/register.html'
    db = 'pre'
    driver = WebBaseDriver("Chrome")
    driver.implicitly_wai(5)
    driver.maximize_window()
    ac = Activity(driver)
    user_phone = ac.get_basics.random_phone()
    # ac.at_recharge('pre', 0, '322271', 200, 'passs')
    ac.invite_friends('test', user_phone, 'a1234567')
    driver.sleep(10)
    driver.quit_browser()



