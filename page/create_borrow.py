import random

from Base import Connect_mysql, get_date


def create_borrow(hj, is_host, bid_money):
    Cndb = Connect_mysql.ConnectMysql()
    #连接数据库 （1-测试，2-准生产）
    connect = hj
    #标的类型配置
    #1.借款方式(1-直投式，2-债权式)
    tran_type = 1
    #2.计息方式（0-核保计息，1-加入即计息，2-满标计息）
    inteaccr_methd = 0
    #3.计息类型(1-等额本息，2-先息后本，3-余额计息，4-等本等息，5-一次性还本付息，6-按天计息，到期还款)
    inteaccr_type = 2
    if is_host == 0:
        #4.供应商代码
        bid_code = '014'
        #5.借款项目类型->注意bid_code与item_type的关系，查询code_operative表
        item_type = '41'
    elif is_host == 2:
        bid_code = '014'
        item_type = '42'
    #6.借款人姓名 测试企借-275044 个人-311171 |准生产 存管个人-380455 企业-380450 托管-270001qbb  132qbb
    if connect == 31:
        borrow_username = '333382qbb'
        name = '依依'
    elif connect == 135:
        borrow_username = '322289qbb'
        name = '兮兮'
    #7.借款金额
    borrow_money = bid_money
    #8.借款期限 D-借款期限为[天]选择此项 M-借款期限为[月]时选择此项
    limit_type = 'M'
    borrow_limit = random.randint(1, 12)
    limit_day = 1
    #9。借款开始时间与结束时间
    begin_date = get_date.today()
    if limit_type == 'D':
        end_date = get_date.get_day_of_day(borrow_limit)
        limit_day = 0
    elif limit_type == 'M':
        end_date = get_date.get_today_month(borrow_limit)
        limit_day = 0
    elif limit_type == 'F':
        end_date = get_date.get_day_of_day(limit_day)
        end_date = get_date.get_allday_month(borrow_limit,str(end_date))
    else:
        raise TypeError('D-借款期限为[天]，M-借款期限为[月]，F-借款期限为[月加天]')
    sql =("set @borrow_sq = fn_getSq('borrowsq');")
    insert = '''INSERT INTO `bid_receive_info` (
        `uid`,
        `borrow_batch`,
        `contract_flow`,
        `borrow_sq`,
        `context`,
        `bid_code`,
        `status`,
        `remark`,
        `create_time`,
        `file_status`,
        `is_response`,
        `resp_msg`,
        `response_time`
    )
    VALUES
        (
             UUID(),
            '014201706270005',
            UUID(),
            @borrow_sq,
            '{"borrow_username":'''+'"'+str(borrow_username)+'"'''',"borrow_money":'''+str(borrow_money)+''',"item_type":'''+'"'+str(item_type)+'"'''',
            "tran_type":'''+str(tran_type)+''',"inteaccr_methd":'''+str(inteaccr_methd)+''',"inteaccr_type":'''+str(inteaccr_type)+''',
            "limit_type":'''+'"'+str(limit_type)+'"'''',"borrow_limit":'''+str(borrow_limit)+''',"limit_day":'''+'"'+str(limit_day)+'"'''',
            "bid_xxbegintime":'''+'"'+str(begin_date)+'"'''',"bid_xxendtime":'''+'"'+str(end_date)+'"'''',"back_date":'''+'"'+str(end_date)+'"'''',
            "assure_comid":'''+'"'+str(bid_code)+'"'''',"assure_comname":"百盛通","now_place":"深圳南山","service_money":null,"user_card":null,"bid_limit":10,"borrow_rate":9,
            "credit_limit":0,"is_register":"0","repayment_src":"","idea_measure":"","carinitialtime":"","com_text":"","income_month":"10000","borrow_text":"0",
            "account_city_name":"","business_text":"","housename":"","assure_type":"1","companyName":", ","gys_borrowsq":20171020000034,"card_acct":null,
            "nation":"汉族","borrow_batch":"043201710200001","cardadr_type":"","province_name":"","validity_authority":"","user_phone":"13790384827",
            "idcard_place":"","companyAddress":", ","birthday":"1992年10月","city_name":"","contract_no":"123456","bid_personname":'''+'"'+str(name)+'"'''',"marriage":"0",
            "id_card":"452123199405100102","credit_enable":"N","carevaluation":"","education":"0","houseadr":"","use_text":"","user_age":null,"companyNature":null,
            "houseappraisal":"","area_name":"","carmodels":"","carnumber":"","period_validity":"","finance_text":null,"attachment":"","borrow_type":"01","district_name":"","user_sex":"0"}',
            %s,
            '0',
            NULL,
            SYSDATE(),
            '0',
            '0',
            NULL,
            NULL
        );'''
    if connect == 31:
        Cndb.connect_db('test', sql)
        Cndb.mysql_cursor.execute("""SELECT @borrow_sq;""")
        borrow_sq = Cndb.mysql_cursor.fetchall()
        print('连接测试环境')
        Cndb.mysql_cursor.execute(insert, (bid_code,))
        Cndb.commitDB()
    elif connect == 135:
        Cndb.connect_db('pre', sql)
        Cndb.mysql_cursor.execute("""SELECT @borrow_sq;""")
        borrow_sq = Cndb.mysql_cursor.fetchall()
        print('连接准生产环境')
        Cndb.mysql_cursor.execute(insert, (bid_code,))
        Cndb.commitDB()
    else:
        raise TypeError('1-测试，2-准生产')
    Cndb.disconnectDB()
    print('新增标的成功！')
    return borrow_sq[0][0]


if __name__ == '__main__':
    br_sql = create_borrow(31, 0, 1000)
    print(br_sql)
