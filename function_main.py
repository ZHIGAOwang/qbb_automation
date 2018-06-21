from Base.web_base_driver import WebBaseDriver
from page.Basics import Basics
from page.Qbb_front import Qbb_Front
from page.Qbb_pa_front import Qbb_Pafront
from page.Zts_operate import Zts_Operate


def qbb_test():
    QBB_URL = "http://192.168.10.31:8080/logout.html"  # 测试地址
    driver = WebBaseDriver("Chrome")
    driver.implicitly_wai(5)
    driver.maximize_window()
    pa_qb = Qbb_Pafront(driver)
    qd = Qbb_Front(driver)
    user_name = '333384qbb'
    user_pwd = '654321'
    investment_hj = 'pre'  # 投资环境，pre=准生产，test=测试
    money = 200             # 金额（投资，充值提现）
    phone = 18333384123     # 手机号码
    card = 6226602900000009  # 银行卡号
    bid = 20180509000359    # 标的号
    pa_ts_pwd = 'a12345'  # 存管交易密码，默认a12345
    if_new = 'new'  # 是否新用户，除了new都是老用户（如果是新用户的话就会操作一些新用户的操作）
    success = 'pass'   # 成功还是失败，除了pass都是失败
    qd.login(QBB_URL, user_name, user_pwd)  # 这里是用户
    bank = '中国光大银行'
    ########################################### 非存管功能
    # recharge / if_new='new'，就会进行风险测评操作
    # qd.recharge(money, success, if_new, bank_card=card)
    # qd.withdraw(1, money, '654321', success)
    # qd.qbb_register_tzr(phone, 'test', 'a1234567', 'a1234567')
    # qd.bid_investment(money, investment_hj, '654321', bid=bid)
    # qd.new_user()
    # qd.invest_read()
    ##########################################  存管功能
    pa_qb.pa_account(card, bank, phone, pa_ts_pwd)
    # pa_recharge / if_new='new'，就会进行风险测评操作,并且添加pa快捷充值银行卡
    # pa_qb.pa_recharge(money, pa_ts_pwd, success, if_new=if_new)
    # pa_qb.pa_withdraw(money, pa_ts_pwd, phone, success)
    # pa_qb.pa_bid_investment(money, investment_hj, phone, pa_ts_pwd, bid=bid)

    driver.sleep(10)
    driver.quit_browser()


def zts_test():
    """直投式修改用户"""
    db = 'pre'                    # 连接的数据库
    bid = 20180612000003          # 标的号
    user_name = "426385qbb"       # 修改后的user_name
    user_phone = "13790384826"    # 修改后的手机号码
    zts = Zts_Operate()
    zts.bid_info_alter(db, bid, user_name, user_phone)


def get_pa_yzm():
    qb = Basics()
    user_id = 426420               # 通过user_id获取平安验证码
    jh = 'pre'
    phone = qb.get_pa_phone(jh, user_id)
    line = qb.get_yzm(phone)
    print(line)


if __name__ == '__main__':
    # qbb_test()
    # zts_test()
    get_pa_yzm()





