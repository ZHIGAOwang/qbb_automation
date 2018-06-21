from Base.Connect_mysql import ConnectMysql
from Base.basepage import BasePage
from Base.web_base_driver import WebBaseDriver
from page.Basics import Basics
from page.Qbb_front import Qbb_Front
from page.Qbb_pa_front import Qbb_Pafront



class Activity(BasePage):
    Cn_db = ConnectMysql()
    Pa_phone = Basics()
    hj = "http://192.168.10.%d:8080/login.html"
    hj_url = None

    def invite_friends(self, url, user_phone, db, user_pwd):
        driver = self.basepage
        qb_front = Qbb_Front(driver)
        driver.navigate(url)
        qb_front.qbb_register_tzr(user_phone, db, user_pwd, user_pwd)

    def at_recharge(self, hj, is_host, user, money, result):
        driver = self.basepage
        qb_front = Qbb_Front(driver)
        qb_pa_front = Qbb_Pafront(driver)
        if hj == 'test':
            self.hj_url = 31
        elif hj == 'pre':
            self.hj_url = 135
        login_url = self.hj % self.hj_url
        qb_front.login(login_url, '%sqbb' % user, '654321')
        if is_host == '2':
            qb_pa_front.pa_recharge(money, 'a12345', result)
        elif is_host == '0':
            qb_front.recharge(money, result)
        else:
            print("please enter is_host again")

    def at_withdraw(self, hj, is_host, user, money, result):
        driver = self.basepage
        qb_front = Qbb_Front(driver)
        qb_pa_front = Qbb_Pafront(driver)
        if hj == 'test':
            self.hj_url = 31
        elif hj == 'pre':
            self.hj_url = 135
        login_url = self.hj % self.hj_url
        qb_front.login(login_url, '%sqbb' % user, '654321')
        print(user)
        if is_host == '2':
            pa_user_phone = self.Pa_phone.get_pa_phone(hj, user)
            qb_pa_front.pa_withdraw(money, 'a12345', pa_user_phone, result)
        elif is_host == '0':
            qb_front.withdraw(1, money, '654321', result)
        else:
            print("please enter is_host again")

    def at_investment(self, hj, is_host, user, money, bid):
        driver = self.basepage
        qb_front = Qbb_Front(driver)
        qb_pa_front = Qbb_Pafront(driver)
        if hj == 'test':
            self.hj_url = 31
        elif hj == 'pre':
            self.hj_url = 135
        login_url = self.hj % self.hj_url
        qb_front.login(login_url, '%sqbb' % user, '654321')
        print(user)
        if is_host == '2':
            pa_user_phone = self.Pa_phone.get_pa_phone(hj, user)
            qb_pa_front.pa_bid_investment(money, hj, pa_user_phone, 'a12345', bid=bid)
        elif is_host == '0':
            qb_front.bid_investment(money, hj, '654321', bid=bid)
        else:
            print("please enter is_host again")


if __name__ == '__main__':
    url = 'http://192.168.10.31:8080/userCenter/register.html'
    user_phone = 15173125415
    db = 'pre'
    driver = WebBaseDriver("Chrome")
    driver.implicitly_wai(5)
    driver.maximize_window()
    ac = Activity(driver)
    ac.at_recharge('pre', 0, '322271', 200, 'passs')
    driver.sleep(10)
    driver.quit_browser()



