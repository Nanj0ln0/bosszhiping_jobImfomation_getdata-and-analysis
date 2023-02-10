import user_agent
import inspect
import psutil
from selenium import webdriver
from utils.ProxyRequest import ProxyRequest

class base():
    def __init__(self,logger,proxy_radio,chrome_driver_path):
        self.logger = logger
        self.proxy_radio = proxy_radio
        self.chrome_driver_path = chrome_driver_path

    def getCurrentFuncName(self):
        # name = sys._getframe().f_code.co_name
        name = inspect.stack()[1][3]
        return name
    def startWebDriver(self):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9555")
            self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path,
                                      options=chrome_options)

            return True
        except Exception as e:
            msg = "开启webdriver失败 %s"%(str(e))
            self.logger.error(msg)

            return False
    def stopWebDriver(self):
        try:
            try:
                if self.driver:
                    self.driver.close()
            except Exception as e:
                self.logger.error("self.driver.close 失败：%s" % str(e))

            for pid in psutil.pids():
                try:
                    p = psutil.Process(pid)
                    # print(u"进程名 %-20s  内存利用率 %-18s 进程状态 %-10s 创建时间 %-10s "
                    #       % (p.name(), p.memory_percent(), p.status(), p.create_time()))
                    if "chromedriver" in p.name():
                        try:
                            p.kill()
                            self.logger.info("杀死chromedriver进程成功：%s",p.name())
                        except Exception as e:
                            self.logger.error("杀死chromedriver进程失败：%s"%str(e))
                except Exception as e:
                    self.logger.error("通过pid获取chromedriver进程失败：%s" % str(e))



            self.driver = None

            return True
        except Exception as e:
            self.logger.error(e)
            return False

    def getRandomUa(self):
        ua = user_agent.generate_user_agent()
        return ua
    def get(self,name,url,headers=None):

        if not headers:
            headers = {}
        headers["User-Agent"] = self.getRandomUa()

        try:
            res = ProxyRequest(proxy_radio=self.proxy_radio).get(url=url, headers=headers)
            if 200 == res.status_code:
                # print(type(res.text)) # str
                # print(type(res.content)) # bytes
                return res
            else:
                self.logger.error("%s-status_code=%d|%s" % (name,res.status_code, url))
        except Exception as e:
            self.logger.error("%s-%s|%s" % (name,str(e), url))


