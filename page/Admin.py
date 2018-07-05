from Base.Connect_mysql import ConnectMysql
from selenium.webdriver.common.keys import Keys
from Base.web_base_driver import WebBaseDriver
from page.Qbb_front import Qbb_Front


class Admin(Qbb_Front):
    Cn_db = ConnectMysql()

    def admin_login(self, hj):
        d = self.basepage
        url = 'http://192.168.10.%d:8084/qian88_admin' % hj
        d.navigate(url)
        d.type('userid', 'zuoyou' + Keys.TAB)
        d.type('password', 'a1234567')
        d.type('validateCode', '1111' + Keys.ENTER)
        d.sleep(1)

    def enter_bid_sh(self, hj):
        d = self.basepage
        if hj == 31:
            d.click('l,[1]借款管理')
            d.click('tree_389_switch')
        else:
            d.click('l,[1]借款管理')
            d.click('tree_354_switch')

    def bid_sh(self, sh, hj ,borrow_title):
        sh_id = None
        sh_frame = None
        d = self.basepage
        if sh == "181":
            sh_id = 'l,[181]风控初审'
            if hj == 31:
                sh_frame = 'frm_tree_391_a'
            else:
                sh_frame = 'frm_tree_356_a'
        elif sh == "182":
            sh_id = 'l,[182风控复审'
            if hj == 31:
                sh_frame = 'frm_tree_392_a'
            else:
                sh_frame = 'frm_tree_357_a'
        elif sh == "183":
            sh_id = 'l,[183]风控终审'
            if hj == 31:
                sh_frame = 'frm_tree_393_a'
            else:
                sh_frame = 'frm_tree_358_a'
        elif sh == "184":
            sh_id = 'l,[184]运营审核'
            if hj == 31:
                sh_frame = 'frm_tree_394_a'
            else:
                sh_frame = 'frm_tree_359_a'
        else:
            print("请输入正确的审核")
        d.click(sh_id)
        d.sleep(1)
        d.switch_to_frame(sh_frame)
        d.sleep(1)
        d.type('q_borrow_title', borrow_title)
        d.click('doqueryBtn')
        d.click('jqg_gridTable_1')
        d.click('selectallPass')
        d.accept_alert()
        text = d.alert_text()
        if '审核成功' in text:
            print(text)
            d.accept_alert()
            d.switch_to_parent_frame()
            return True
        else:
            print(text)
            return False


if __name__ == '__main__':
    driver = WebBaseDriver("Chrome")
    ad = Admin(driver)
    driver.implicitly_wai(5)
    driver.maximize_window()
    hj = 135
    sh1 = "181"
    sh2 = "184"
    bid = 20180703000003
    ad.admin_login(hj)
    ad.enter_bid_sh(hj)
    ad.bid_sh(sh1, hj, bid)
    ad.bid_sh(sh2, hj, bid)
    driver.sleep(10)
    driver.quit_browser()