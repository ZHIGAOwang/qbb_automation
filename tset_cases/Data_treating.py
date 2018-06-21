import datetime
import xlsxwriter
import os, xlrd

from Base.Connect_mysql import ConnectMysql


class Data_Treating():

    def create_table(self, name):
        # 新建Excel表格
        time_stamp = datetime.datetime.now()
        time = time_stamp.strftime('%y.%m.%d-%H')
        self.xl = xlsxwriter.Workbook(os.path.dirname(os.getcwd())+'\\Test_result\\'+str(name)+'_Result%s.xlsx' % time)
        self.table = self.xl.add_worksheet(name)  # 新建一个名为result的页签
        # 设置格式：行高、列宽、底色、字号等格式
        self.blue = self.xl.add_format({'font_name': 'Arial', 'font_size': 11,'color': 'blue'})
        self.red = self.xl.add_format({'font_name': 'Arial', 'font_size': 11,'color': 'red'})
        self.black = self.xl.add_format({'font_name': 'Arial', 'font_size': 12,'color': 'black'})
        # 设置第一行的行高为30
        self.table.set_row(0, 20)
        # 设置第1列到第4列的列宽为25
        self.table.set_column(0, 4, 25)

    def write_head(self, head_list):
        # 往第一行第一列写入字符串数据
        self.a = 0
        for j in head_list:
            self.table.write_string(0, self.a, u'%s' % j, self.black)
            self.a = self.a + 1

    def write_content(self, data, result, num):
        self.a = 0
        for j in data:
            self.a = self.a + 1
            if result == 'pass':
                self.table.write_string(num, self.a, u'%s' % j, self.blue)
            else:
                self.table.write_string(num, self.a, u'%s' % j, self.red)
        self.table.write_string(num, self.a+1, u'%s' % result, self.red)

    def close(self):
        # 关闭Excel表格s
        self.xl.close()

    def read_content(self, filename, sheet_name):
         """从Excel读取"""
         data = xlrd.open_workbook('E:\页面自动化\Data\%s.xlsx' % filename)
         tableGet = data.sheet_by_name(sheet_name)
         data = []
         data1 = []
         for i in range(1, tableGet.nrows):
             testData = tableGet.row_values(i)  # 读取第二行数据
             for j in range(0, tableGet.ncols):
                 data.append('%s' % testData[j])
             str1 = '-'
             data2 = str1.join(data)
             data1.append(data2)
             data.clear()
         return data1



if __name__ == '__main__':
    # a = 0
    # result = None
    dl_list = []
    head_list = ['url（注册网址）','userid/relevanceId','luckcd',	'邀请好友是否给活动机会']
    tr = Data_Treating()
    # data = tr.read_content('活动充值', 'result')
    # tr.create_table('登录')
    # for i in data:
    #     array = i.split('-')
    #     if array[2] == 'sss':
    #         result = 'pass'
    #     else:
    #         result = 'error'
    #     a = a + 1
    #     Cn_db = ConnectMysql()
    #     id_sql = "SELECT luckcd,userId,relevanceId FROM l_prize_log WHERE  relevanceId=(SELECT user_id from cnp_user WHERE user_phone=%d) and  functp='hy' ;"
    #     chance_sql = "SELECT functp,luckcd,typeName,userId,relevanceId FROM l_prize_log WHERE  relevanceId=(SELECT user_id from cnp_user WHERE user_phone=%d) and  functp!='hy' ;"
    #     sql = chance_sql % 17917171717
    #     id_result = Cn_db.connect_db('pre', sql)
    #     id_result = Cn_db.connect_db('pre', sql)
    #     Cn_db.disconnectDB()
    #     dl_list.extend([array[0],
    #                     array[0] + ' ,' + array[1],
    #                     array[1],
    #                     id_result.__str__(),])
    #     tr.write_head(head_list)
    #     tr.write_content(dl_list,
    #                      result,
    #                      a)
    #     dl_list.clear()
    # tr.close()
    tr.create_table('登录')
    tr.write_head(head_list)
    dl_list = [1,2,3,4]
    tr.write_content(dl_list,
                     'pass',
                     1)
    tr.close()

