import json
from Base.Connect_mysql import ConnectMysql
from Base.basepage import BasePage
from Base.web_base_driver import WebBaseDriver


class Zts_Operate():
    Cn_db = ConnectMysql()

    def bid_info_alter(self, db, bid, user_name, user_phone):
        sql = '''SELECT context FROM bid_receive_info WHERE borrow_sq = %s;''' % bid
        old_text = self.Cn_db.connect_db(db, sql)
        now_text = json.loads(old_text[0][0])
        now_text["borrow_username"] = "%s" % user_name
        now_text["user_phone"] = "%s" % user_phone
        now_text = json.dumps(now_text)
        sql1 = '''UPDATE bid_receive_info SET context=%r ,status=0 WHERE borrow_sq = %d;''' % (now_text, bid)
        print('修改成功')
        self.Cn_db.connect_db('pre', sql1)
        self.Cn_db.commitDB()
        self.Cn_db.disconnectDB()

    def admin(self):
        pass


if __name__ == '__main__':

    db = 'pre'
    bid = 20180612000003
    user_name = "426385qbb"
    user_phone = "13790384826"
    zts = Zts_Operate()
    zts.bid_info_alter(db, bid, user_name, user_phone)


