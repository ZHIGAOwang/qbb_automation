from Base.web_base_driver import WebBaseDriver
from page.Admin import Admin
from page.Basics import Basics
from page.Qbb_front import Qbb_Front
from page.Qbb_pa_front import Qbb_Pafront
from page.create_borrow import create_borrow


def qbb_test():
    QBB_URL = "http://192.168.10.135:8080/logout.html"  # 测试地址
    driver = WebBaseDriver("Chrome")
    driver.implicitly_wai(5)
    driver.maximize_window()
    pa_qb = Qbb_Pafront(driver)
    qd = Qbb_Front(driver)
    # 登录
    user_name = '322289qbb'
    user_pwd = '654321'
    qd.login(QBB_URL, user_name, user_pwd)

    # 注册，注册不需要登录
    phone = qd.get_basics.random_phone()  # 手机号码  随机生成
    rg_pwd = 'a1234567'                   # 注册密码，注册成功之后会改成654321
    # user_id = qd.qbb_register_tzr(QBB_URL, phone, rg_pwd, rg_pwd)

    #############################################################
    money = 5000                          # 金额（投资，充值提现）
    success = 'pass'                      # 成功还是失败，除了pass都是失败
    card = 6226602900000009               # 银行卡号
    pa_ts_pwd = 'a12345'                  # 存管交易密码，默认a12345
    #############################################################

    # 存管开户
    # pa_qb.pa_account(card, phone, pa_ts_pwd)

    # 充值/存管充值
    # qd.recharge(money, success, bank_card=card)
    pa_qb.pa_recharge(money, pa_ts_pwd, success)

    # 投资/存管投资
    investment_hj = 'test'                # 投资环境，pre=准生产，test=测试
    bid = 20180628000011                  # 标的号
    # qd.bid_investment(money, investment_hj, '654321', bid=bid)
    # pa_qb.pa_bid_investment(money, investment_hj, pa_ts_pwd, bid=bid)

    # 提现/存管提现
    # qd.withdraw(1, money, '654321', success)
    # pa_qb.pa_withdraw(money, pa_ts_pwd, success)

    driver.sleep(50)
    driver.quit_browser()


def create_bid():
    driver = WebBaseDriver("Chrome")
    qb = Basics()
    ad = Admin(driver)
    driver.implicitly_wai(5)
    driver.maximize_window()
    bid = create_borrow()
    hj = 135
    sh1 = "181"
    sh2 = "184"
    qb.scheduler_zx(135,41)
    ad.admin_login(hj)
    ad.enter_bid_sh(hj)
    ad.bid_sh(sh1, hj, bid)
    ad.bid_sh(sh2, hj, bid)
    qb.scheduler_zx(135, 51)
    qb.scheduler_zx(135, 34)


def zts_test():
    """直投式修改用户"""
    qb = Basics()
    db = 'pre'                    # 连接的数据库
    bid = 20180612000003          # 标的号
    user_name = "426385qbb"       # 修改后的user_name
    user_phone = "13790384826"    # 修改后的手机号码
    qb.bid_info_alter(db, bid, user_name, user_phone)


def get_pa_yzm():
    qb = Basics()
    user_id = 322271              # 通过user_id获取平安验证码
    jh = 'pre'
    phone = qb.get_pa_phone(jh, user_id)
    line = qb.get_yzm(phone)
    print(line)


if __name__ == '__main__':
    qbb_test()
    # zts_test()
    # get_pa_yzm()




