import requests, re
from Base.Connect_mysql import ConnectMysql


class Basics:
    Cn_db = ConnectMysql()
    headers = {"User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64)Apple",
               "Content-Type": "application/x-www-form-urlencoded",
               "Accept": "*/*",
               "Connection": "keep-alive"}
    host = 'https://my-st1.orangebank.com.cn/corporbank/otp.jsp'
    pa_user_phone = "SELECT pa_user_phone  FROM cnp_user  WHERE user_id =%r ;"
    ###########################################
    hy_id_sql = "SELECT luckcd,userId,relevanceId FROM l_prize_log WHERE  relevanceId=(SELECT user_id from cnp_user WHERE user_phone=%d) and  functp='hy' ;"
    hy_chance_sql = "SELECT functp,luckcd,typeName,userId,relevanceId FROM l_prize_log WHERE  relevanceId=(SELECT user_id from cnp_user WHERE user_phone=%d) and  functp!='hy' ;"
    cz_wb_sql = "SELECT luckcd,functp,typeName,userid,relevanceId,rmoney from l_prize_log where userId=%s and luckcd=%s and  typeName REGEXP'充值' ORDER BY crtime DESC;"
    tx_wb_sql = "SELECT luckcd,functp,typeName,userid,relevanceId,rmoney from l_prize_log where userId=%s and luckcd=%s and typeName REGEXP'提现'  ORDER BY crtime DESC;"

    ############################################
    if_head =['url', 'userid/relevanceId', 'luckcd', '邀请好友是否给活动机会']
    at_recharge_head = ["用户id", "充值金额（是否存管）", "获得旺币数量,游戏机会", "旺币和游戏机会是否正确"]
    at_withdraw_head = ["用户id", "提现金额（是否存管）", "获得旺币数量,游戏机会", "旺币和游戏机会是否正确"]
    at_investment_head = ["用户id", "投资金额（是否存管）", "投资金额,红包金额,红包记录", "红包的使用情况", "邀请人是否有发送红包"]

    def get_yzm(self, phone):
        http_response =requests.post(self.host+'?mobile='+str(phone)+'', headers=self.headers)
        html = http_response.text
        out = re.split('<td>(.*)</td>', html)
        return out[9]

    def get_pa_phone(self, hj, user):
        pa_user_phone = self.Cn_db.connect_db(hj, self.pa_user_phone % user)
        self.Cn_db.disconnectDB()
        return pa_user_phone[0][0]


if __name__ == '__main__':
    qb = Basics()
    # user_id = 322271
    # jh = 'pre'
    # phone = qb.get_pa_phone(jh, user_id)
    line = qb.get_yzm(18355551123)
    print(line)
