import csv
from time import sleep
import pymysql
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

class WebBaseDriver(object):
    csv_file = None
    sql_file = None
    mysql_connect = None
    mysql_cursor = None


    def __init__(self,browser):
        if browser == 'Firefox':
            driver = webdriver.Firefox()#切记勿漏括号
            try:
                self.driver = driver
            except Exception:   #try部分代码执行有问题时，就会执行except内部的语句
                raise NameError('Firefox Not Found')
        elif browser == 'Chrome':
            driver = webdriver.Chrome()
            try:
                self.driver = driver
            except Exception:
                raise NameError('Chrome Not Found')
        else:
            print('Not Found Browser !')

    def get_element(self,selector):
        '''定位元素'''
        if ',' not in selector:     #例：'i,password'
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split(',')[0].strip() #获取定位方式（split：间隔）
        selector_value = selector.split(',')[1].strip() #获取定位方式对应的值

        if selector_by == 'i' or selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
        elif selector_by == 'n' or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == 'c' or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == 'l' or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == 's' or selector_by == 'css_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        elif selector_by == 'x' or selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
        elif selector_by == 't' or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        else:
            raise NameError('please enter a valid type of targeting element')

        return element
    def get_elements(self,selector):
        '''定位元素'''
        if ',' not in selector:     #例：'i,password'
            return self.driver.find_elements_by_id(selector)
        selector_by = selector.split(',')[0].strip() #获取定位方式（split：间隔）
        selector_value = selector.split(',')[1].strip() #获取定位方式对应的值

        if selector_by == 'i' or selector_by == 'id':
            element = self.driver.find_elements_by_id(selector_value)
        elif selector_by == 'n' or selector_by == 'name':
            element = self.driver.find_elements_by_name(selector_value)
        elif selector_by == 'c' or selector_by == 'class_name':
            element = self.driver.find_elements_by_class_name(selector_value)
        elif selector_by == 'l' or selector_by == 'link_text':
            element = self.driver.find_elements_by_link_text(selector_value)
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            element = self.driver.find_elements_by_partial_link_text(selector_value)
        elif selector_by == 's' or selector_by == 'css_selector':
            element = self.driver.find_elements_by_css_selector(selector_value)
        elif selector_by == 'x' or selector_by == 'xpath':
            element = self.driver.find_elements_by_xpath(selector_value)
        elif selector_by == 't' or selector_by == 'tag_name':
            element = self.driver.find_elements_by_tag_name(selector_value)
        else:
            raise NameError('please enter a valid type of targeting element')

        return element
    def type(self,selector,text):
        '''输入内容'''
        ele = self.get_element(selector)    #元素定位
        ele.clear()
        ele.send_keys(text)

    def click(self,selector):
        '''点击操作'''
        ele = self.get_element(selector)
        ele.click()
    def ele_click(self,selector):
        selector.click()

    def switch_to_frame(self,selector):
        '''进入iframe'''
        ele = self.get_element(selector)
        self.driver.switch_to.frame(ele)

    def switch_default_frame(self):
        '''退出到最外层iframe'''
        self.driver.switch_to.default_content()

    def switch_to_parent_frame(self):
        '''退出到上一层iframe'''
        self.driver.switch_to.parent_frame()

    def select_by_index(self,selector,num):
        '''以index方式选择下拉框选项'''
        ele =  self.get_element(selector)
        select = Select(ele)
        select.select_by_index(num)

    def select_by_value(self,selector,value):
        '''以value方式选择下拉框选项'''
        ele =  self.get_element(selector)
        select = Select(ele)
        select.select_by_value(value)

    def select_by_visible_text(self,selector,text):
        '''以text方式选择下拉框选项'''
        ele =  self.get_element(selector)
        select = Select(ele)
        select.select_by_visible_text(text)

    def accept_alert(self):
        '''确定alert框'''
        self.driver.switch_to_alert().accept()

    def dismiss_alert(self):
        '''取消alert框'''
        self.driver.switch_to_alert().dismiss()

    def navigate(self,url):
        '''打开网页'''
        self.driver.get(url)

    def current_window_handle(self):
        '''获取当前窗口句柄'''
        return self.driver.current_window_handle

    def window_handles(self):
        '''获取所有窗口句柄'''
        return self.driver.window_handles

    def get_attribute(self,selector,name):
        '''获取元素属性值'''
        ele = self.get_element(selector)
        return ele.get_attribute(name)

    def open_new_window(self, selector):
        '''进入新窗口页面'''
        current_handle = self.driver.current_window_handle
        ele = self.get_element(selector)
        try:
            ele.click()
        except Exception:
            pass
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to.window(handle)

    def open_last_window(self):
        '''进入最后一个窗口'''
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[-1])

    def maximize_window(self):
        '''窗口最大化'''
        self.driver.maximize_window()

    def implicitly_wai(self,second):
        '''智能等待元素'''
        self.driver.implicitly_wait(second)

    def quit_browser(self):
        '''退出浏览器'''
        self.driver.quit()

    def close_browser(self):
        '''关闭当前浏览器窗口'''
        self.driver.close()

    def sleep(self,time):
        sleep(time)

    def get_url(self):
        '''获取当前页面url'''
        return self.driver.current_url
    def get_text(self,selector):
        """
        获取元素文本
        :return: 
        """
        ele = self.get_element(selector)
        return ele.text

    def get_title(self):
        '''获取当前页面的标题'''
        return self.driver.title

    def belong_to_pro(self,num):
        return "s,li[Test_result-option-array-index='%d']" %num

    def get_csv_data(self,file_path,zfj):
        self.csv_file = open(file_path, mode="r", encoding=zfj)
        '''中文数据出现乱码处理方法:settings-editor-file encodings,设置GBK'''
        '''读取文件内容'''
        csv_data = csv.reader(self.csv_file)
        return csv_data

    def close_csv_file(self):
        self.csv_file.close()

    def get_sql_data(self,file_path,zfj1,address,database,zfj2):
        '''读取sql文件'''
        self.sql_file = open(file_path,
                        mode='r',
                        encoding=zfj1)
        sql_scripts = self.sql_file.read()  # 仅读到sql语句，还没读取到数据
        '''连接数据库,要现在cmd模式下用命令导入pymsql包，pip install pymysql'''
        self.mysql_connect = pymysql.connect(host=address,  # 数据库所在机器的地址
                                        user='root',
                                        passwd='',
                                        db=database,  # 数据库
                                        port=3306,  # 端口不要加引号
                                        charset=zfj2)  # 防止读取数据库数据出现乱码
        '''创建游标并读取数据库数据'''
        self.mysql_cursor = self.mysql_connect.cursor()  # 创建游标，逐行读取数据
        self.mysql_cursor.execute(sql_scripts)  # 执行sql语句
        mysql_data = self.mysql_cursor.fetchall()  # 接收全部的返回结果行
        return mysql_data

    def close_sql(self):
        self.sql_file.close()#关闭文件
        self.mysql_connect.close()#关闭数据库连接
        self.mysql_cursor.close()#关闭游标

    def right_click(self, selector):
        """
        右击
        """
        el = self.get_element(selector)
        ActionChains(self.driver).context_click(el).perform()
    def double_click(self, selector):
        """
        双击
        """
        el = self.get_element(selector)
        ActionChains(self.driver).double_click(el).perform()
    def move_to(self, selector):
        """
        移动到
        """
        el = self.get_element(selector)
        ActionChains(self.driver).move_to_element(el).perform()
    def click_and_hold(self, selector):
        """
        点击并且按住
        """
        el = self.get_element(selector)
        ActionChains(self.driver).click_and_hold(el).perform()
    def drag_and_drop(self, source, target):
        """
        拖拽
        """
        el = self.get_element(source)
        el1 = self.get_element(target)
        ActionChains(self.driver).drag_and_drop(el,el1).perform()

    def screenshot(self, selector, is_host):
        pa_yzm_file = "E:\页面自动化\image\pa_yzm.png"
        qbb_yzm_file = "E:\页面自动化\image\qbb_yzm.png"
        """验证码截图"""
        if is_host == 2:
            self.driver.get_screenshot_as_file(pa_yzm_file)
        else:
            self.driver.get_screenshot_as_file(qbb_yzm_file)
        location = self.get_element(selector).location_once_scrolled_into_view
        size = self.get_element(selector).size
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        if is_host == 2:
            a = Image.open(pa_yzm_file)
            im = a.crop((left, top, right, bottom))
            im.save(pa_yzm_file)
            return pa_yzm_file
        else:
            a = Image.open(qbb_yzm_file)
            im = a.crop((left, top, right, bottom))
            im.save(qbb_yzm_file)
            return qbb_yzm_file
