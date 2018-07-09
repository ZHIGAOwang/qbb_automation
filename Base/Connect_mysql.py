import pymysql


class ConnectMysql(object):

    def connect_db(slef, db_name, sql):
        if db_name == 'test' or db_name == 31:
              slef.mysql_connect = pymysql.connect(host='192.168.10.36',
                                               user='db_test',
                                               passwd='TEST788qbb',
                                               db='web_qbb_test',
                                               port=3306,
                                               charset='utf8')
              slef.mysql_cursor=slef.mysql_connect.cursor()
              slef.mysql_cursor.execute(sql)
              sql_data =slef.mysql_cursor.fetchall()
              return  sql_data

        elif db_name == 'pre' or db_name == 135:
            slef.mysql_connect = pymysql.connect(host='192.168.10.26',
                                              user='db_test',
                                              passwd='TEST788qbb',
                                              db='web_qbb_ready',
                                              port=3306,
                                              charset='utf8')
            slef.mysql_cursor = slef.mysql_connect.cursor()
            slef.mysql_cursor.execute(sql)
            sql_data = slef.mysql_cursor.fetchall()
            return sql_data
        else:
            print('Please enter the correct database name')

    def disconnectDB(self):
        self.mysql_connect.close()#关闭数据库连接
        self.mysql_cursor.close()#关闭游标

    def commitDB(self):
        self.mysql_connect.commit()


if __name__ == '__main__':
    Cndb=ConnectMysql()
    # sql = "SELECT *, mt.content FROM sys_sms_mt mt WHERE mt.mobile = 15173125421;"
    # print(Cndb.connect_db('pre',sql))
    Cndb.disconnectDB()
