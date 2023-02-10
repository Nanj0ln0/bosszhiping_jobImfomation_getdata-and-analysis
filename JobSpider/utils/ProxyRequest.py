import requests
import random

class ProxyRequest:
    def __init__(self,proxy_radio):
        self.proxy_radio = proxy_radio

    def __del__(self):
        pass

    def get(self,url,headers,timeout=30):

        proxyHost = "127.0.0.1"
        proxyPort = "3679"

        proxyMeta = "http://%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
        }
        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }
        # random() 方法返回随机生成的一个实数，它在[0,1)范围内。
        if random.random() <= self.proxy_radio:
            res = requests.get(url, headers=headers, proxies=proxies, timeout=timeout)
        else:
            res = requests.get(url, headers=headers, timeout=timeout)

        return res

if __name__ == '__main__':
    for i in range(100):
        print(random.random())