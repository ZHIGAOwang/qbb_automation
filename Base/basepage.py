from Base.web_base_driver import WebBaseDriver


class BasePage(object):
    def __init__(self,basedriver:WebBaseDriver):
        self.basepage = basedriver