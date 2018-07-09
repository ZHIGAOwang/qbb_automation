import json
from Base.Id_card import *
import string
import requests
from Base.Connect_mysql import ConnectMysql


class Basics:
    jd_user = "SELECT * FROM ( SELECT IF (count(1) > 0, 1, 0) AS isRisk FROM user_risk_log AS log WHERE log.user_id = %s ) AS t1 LEFT JOIN ( SELECT IF (count(1) > 0, 1, 0) AS isEval FROM question_user_answer AS ans WHERE ans.user_id = %s ) AS t2 ON 1 = 1;"
    n_user_id = "SELECT user_id FROM cnp_user WHERE user_name = '%s';"
    p_user_id = "SELECT user_id FROM cnp_user WHERE user_phone = '%s' ORDER BY register_time DESC LIMIT 1;"
    user_class = "SELECT user_class from	cnp_user WHERE user_id =%s;"
    pa_user_phone = "SELECT pa_user_phone  FROM cnp_user  WHERE user_id =%r ;"
    dx_yzm = "SELECT reserve from sys_sms_mt mt WHERE mt.mobile =%s ORDER BY create_time DESC LIMIT 1;"
    user_accredit = "SELECT pa_authflag FROM cnp_user  WHERE user_id = %r;"
    sql = '''SELECT context FROM bid_receive_info WHERE borrow_sq = %s;'''
    limit_get = "SELECT limit_type,borrow_limit,limit_day from bid_borrow WHERE borrow_sq = %s;"
    ##########################################
    user_update = "UPDATE cnp_user SET user_name = '%rqbb', login_pwd = '3e9a73fac9a7b2477589161a7d0f960c', tran_pwd = '3e9a73fac9a7b2477589161a7d0f960c' WHERE user_id = %r;"
    vip_up_card = "UPDATE cnp_user_vip SET idcard=%s, vip_name='%s' WHERE user_id=%r;"
    sql1 = '''UPDATE bid_receive_info SET context=%r ,status=0 WHERE borrow_sq = %d;'''
    bid_up = "SELECT borrow_sq FROM bid_borrow WHERE borrow_sq != %s and	is_hosting=%s  AND `status`>=5 AND `status`<=11 and product_type=%d and borrow_limit>%d borrow_limit<=%d;"
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
    #############################################
    Cn_db = ConnectMysql()
    headers = {"User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64)Apple",
               "Content-Type": "application/x-www-form-urlencoded",
               "Accept": "*/*",
               "Connection": "keep-alive"}
    host = 'https://my-st1.orangebank.com.cn/corporbank/otp.jsp'

    def get_yzm(self, phone):
        """获取平安短信验证码"""
        http_response =requests.post(self.host+'?mobile='+str(phone)+'', headers=self.headers)
        html = http_response.text
        out = re.split('<td>(.*)</td>', html)
        return out[9]

    def scheduler_zx(self, hj, id):
        """定时器执行"""
        if hj == 31 or hj == 'test':
            url = "http://192.168.10.31:8078/scheduler/runnow.action"
        else:
            url = "http://192.168.10.149:8078/scheduler/runnow.action"
        http_response = requests.post(url + '?id=' + str(id) + '', headers=self.headers)
        html = http_response.text
        html = json.loads(html)
        msg = html["message"]
        time_stamp = datetime.now()
        time = time_stamp.strftime('%Y-%m-%d %H:%M:%S')
        if msg == "执行成功":
            print('%d定时器执行成功' % id, time)
        else:
            print('%d定时器执行失败,%s' % (id, html["message"]))

    def scheduler_core_zx(self, hj, id):
        """定时器执行"""
        if hj == 31 or hj == 'test':
            url = "http://192.168.10.31:8078/scheduler/runnow.action"
        else:
            url = "http://192.168.10.149:8092/scheduler/runnow.action"
            print(1)
        http_response = requests.post(url + '?id=' + str(id) + '', headers=self.headers)
        html = http_response.text
        html = json.loads(html)
        time_stamp = datetime.now()
        time = time_stamp.strftime('%Y-%m-%d %H:%M:%S')
        msg = html["message"]
        if msg == "执行成功":
            print('%d定时器执行成功' % id, time)
        else:
            print('%d定时器执行失败,%s' % (id, html["message"]))

    def get_pa_phone(self, hj, user):
        """获取平安手机"""
        pa_user_phone = self.Cn_db.connect_db(hj, self.pa_user_phone % user)
        self.Cn_db.disconnectDB()
        return pa_user_phone[0][0]

    def get_user_id(self, hj, user_name=None, user_phone=None):
        """通过user_name获取用户user_id"""
        if user_phone is not None:
            user_id = self.Cn_db.connect_db(hj, self.p_user_id % user_phone)
            self.Cn_db.disconnectDB()
            return user_id[0][0]
        else:
            user_id = self.Cn_db.connect_db(hj, self.n_user_id % user_name)
            self.Cn_db.disconnectDB()
            return user_id[0][0]

    def judge_user(self, hj, user):
        """判断是否新用户名"""
        get_user = self.Cn_db.connect_db(hj, self.jd_user % (user, user))
        self.Cn_db.disconnectDB()
        return get_user[0]

    def get_user_class(self, hj, user):
        """是否借款人"""
        user_type = self.Cn_db.connect_db(hj, self.user_class % user)
        self.Cn_db.disconnectDB()
        return user_type[0][0]

    def get_dx_yzm(self, database, user_phone):
        """获取注册短信验证码"""
        dx_yzm = self.Cn_db.connect_db(database, self.dx_yzm % user_phone)
        self.Cn_db.disconnectDB()
        return dx_yzm[0][0]

    def get_pa_authflag(self, database, user_id):
        """获取平安存管开通状态"""
        user_accredit = self.Cn_db.connect_db(database, self.user_accredit % user_id)
        self.Cn_db.disconnectDB()
        return user_accredit[0][0]

    def random_phone(self):
        """随机生成手机号码"""
        num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187',
                     '188',
                     '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']

        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 8))
        random_phone = start + end
        return random_phone

    def new_user_update(self, database, user_id):
        """更新用户信息"""
        print(user_id)
        self.Cn_db.connect_db(database, self.user_update % (user_id, user_id))
        self.Cn_db.commitDB()
        self.Cn_db.disconnectDB()
        print("更新用户信息成功")

    def bid_info_alter(self, db, bid, user_name, user_phone):
        """修改合作商借款人"""
        old_text = self.Cn_db.connect_db(db, self.sql % bid)
        now_text = json.loads(old_text[0][0])
        now_text["borrow_username"] = "%s" % user_name
        now_text["user_phone"] = "%s" % user_phone
        now_text = json.dumps(now_text)
        self.Cn_db.connect_db('pre', self.sql1 % (now_text, bid))
        self.Cn_db.commitDB()
        self.Cn_db.disconnectDB()
        print('修改成功')

    def vip_approve(self, result, database, user_id):
        """vip认证"""
        if "认证" in result:
            id_card = get_id_card()
            user_name = get_user_name()
            user_vip1 = ("set @vipID='';")
            user_vip2 = ("call pkg_getseq('userVip_sq',DATE_FORMAT(now(),'%Y%m%d'),@vipID,@i,@j);")
            user_vip3 = """ insert into user_vip_init (vip_id, user_id, create_time, vip_name, exam_id, iden_time, over_time, card_type, idcard, posi_path, nega_path, face_path, channel)   
                        values ( @vipID, """ + str(user_id) + """, SYSDATE(), '""" + str(user_name) + """', null, null, null, 1, '""" + str(id_card) + """', 'vipImages/20170104/posi_1483494474876.jpg', 
                        'vipImages/20170104/nega_1483494481917.jpg', 'vipImages/20170104/face_1483494483794.jpg', 'WEB');"""
            user_vip4 = """insert into cnp_user_vip (vip_id, user_id, create_time, vip_name, recruitment, domicile, status, exam_id, iden_time, over_time, card_type,idcard, 
                        posi_path, nega_path, face_path, channel, vip_count, remark)   
                        values (@vipID, """ + str(user_id) + """, SYSDATE(), '""" + str(user_name) + """', null, null, 1, null, null, null, 1, '""" + str(id_card) + """',
                         'vipImages/20170104/posi_1483494474876.jpg', 'vipImages/20170104/nega_1483494481917.jpg', 'vipImages/20170104/face_1483494483794.jpg', 'WEB', 1, null);"""
            self.Cn_db.connect_db(database, user_vip1)
            self.Cn_db.mysql_cursor.execute(user_vip2)
            self.Cn_db.mysql_cursor.execute(user_vip3)
            self.Cn_db.mysql_cursor.execute(user_vip4)
            self.Cn_db.commitDB()
            self.Cn_db.disconnectDB()
            print("vip认证成功")
        else:
            print("已vip认证，或者没有找到元素")

    def vip_update(self,  database, user_id):
        id_card = get_id_card()
        user_name = get_user_name()
        self.Cn_db.connect_db(database, self.vip_up_card % (id_card, user_name, user_id))
        self.Cn_db.commitDB()
        self.Cn_db.disconnectDB()
        print('修改证件号码成功')

    def bid_update(self, database, bid):
        limit = self.Cn_db.connect_db(database, self.limit_get % bid)
        self.Cn_db.disconnectDB()
        limit = limit[0]
        if limit[0] == "M":
            if limit[1] <= 3:
                pass
            elif limit[1] > 3 & limit[1] <= 6:
                pass
            elif limit[1] > 6 & limit[1] <= 12:
                pass
        elif limit[0] == "D":
            if limit[1] <= 3:
                pass
            elif limit[1] > 3 & limit[1] <= 6:
                pass
            elif limit[1] > 6 & limit[1] <= 12:
                pass


if __name__ == '__main__':
    qb = Basics()
    user_name2 = 'qbb3228439010'
    jh = 'pre'
    # user_phone2 = 13424523235
    # qb.scheduler_zx(jh, 51)
    # status = qb.judge_user(jh, user_id)
    # print(status[0])
    # phone = qb.get_pa_phone(jh, user_id)
    # line = qb.get_yzm(18355551123)
    # print(line)
    # aa = qb.get_dx_yzm(jh, 13573548692)
    # print(aa)
    user_id = qb.get_user_id(jh, user_phone=15173125426)
    qb.new_user_update(jh, user_id)
    result2 = '认证'
    # qb.vip_update(jh, 426432)
    # qb.vip_approve(result2, jh, 382356)