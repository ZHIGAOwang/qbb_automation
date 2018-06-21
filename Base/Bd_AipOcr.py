from aip import AipOcr
import os


class Bd_AipOcr():
    """ 你的 APPID AK SK """
    APP_ID = '11402378'
    API_KEY = 'sim9AnjAvRYLKuoyIpdQYkua'
    SECRET_KEY = 'BrhtIyX0NhKctUURWUIWr34NOMtA7GSP'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    os.makedirs('../image/', exist_ok=True)
    PA_IMAGE_URL = "https://my-st1.orangebank.com.cn/corporbank/%s"
    QBB_IMAGE_URL = 'http://192.168.10.135:8080/userCenter/%s'

    def url_fet_yzm(self, url_parameter):
        """ 调用通用文字识别, 图片参数为远程url图片 """
        url = self.PA_IMAGE_URL % url_parameter
        print(url)
        result = self.client.basicGeneralUrl(url)
        print(result)
        return result['words_result']
        # """ 如果有可选参数 """
        # options = {}
        # options["language_type"] = "CHN_ENG"
        # options["detect_direction"] = "true"
        # options["detect_language"] = "true"
        # options["probability"] = "true"
        # """ 带参数调用通用文字识别, 图片参数为远程url图片 """
        # # client.basicGeneralUrl(url, options)


    def get_file_content(self, filePath):
        # """ 读取图片 """
        with open(filePath, 'rb') as fp:
            return fp.read()


    def mig_get_yzn(self, filePath):
        """ 调用通用文字识别, 图片参数为本地图片 """
        image = self.get_file_content(filePath)
        result = self.client.basicGeneral(image)
        result = result['words_result']
        return result[0]['words']
        # """ 如果有可选参数 """
        # options = {}
        # options["language_type"] = "CHN_ENG"
        # options["detect_direction"] = "true"
        # options["detect_language"] = "true"
        # options["probability"] = "true"
        #
        # """ 带参数调用通用文字识别, 图片参数为本地图片 """
        # client.basicGeneral(image, options)

    def mig_gjd_yzm(self, filePath):
        """ 调用通用文字识别（高精度版） """
        image = self.get_file_content(filePath)
        result = self.client.basicAccurate(image)
        result = result['words_result']
        return result[0]['words']
        # """ 如果有可选参数 """
        # options = {}
        # options["detect_direction"] = "true"
        # options["probability"] = "true"
        #
        # """ 带参数调用通用文字识别（高精度版） """
        # client.basicAccurate(image, options)


    def urllib_download(self, url_parameter, is_host):
        from urllib.request import urlretrieve
        if is_host == 2:
            urlretrieve(self.PA_IMAGE_URL % url_parameter, '../image/pa_yzm.png')
            return '../image/pa_yzm.png'
        else:
            urlretrieve(self.QBB_IMAGE_URL % url_parameter, '../image/qbb_yzm.png')
            return '../image/qbb_yzm.png'

    # def request_download(url_parameter):
    #     import requests
    #     r = requests.get(QBB_IMAGE_URL % url_parameter)
    #     with open('../image/qbb_yzm.png', 'wb') as f:
    #         f.write(r.content)
    #     return '../image/qbb_yzm.png'

    # def chunk_download():
    #     import requests
    #     r = requests.get(IMAGE_URL, stream=True)
    #     with open('../image/img3.png', 'wb') as f:
    #         for chunk in r.iter_content(chunk_size=32):
    #             f.write(chunk)


if __name__ == '__main__':
    qbb_url = 'imageCode.html?pageId=register&d=0.5518015352539027'
    pa_url = 'VerifyImage?update=0.008738163584545378'