import requests, time, json
from PyQt5.QtCore import QThread, pyqtSignal
from bs4 import BeautifulSoup


class Community_spider():
    # trigger_list = pyqtSignal(str)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'Connection': 'close'}

    def __init__(self, parent, server_ip: str, server_port: str, extra=''):
        # super(QThread, self).__init__(parent)
        self.url = 'http://' + server_ip + ':' + server_port + extra
        self.refresh_status()
        self.flag = None

    def server_init(self, server_addr):
        self.url = server_addr

    def refresh_status(self):
        try:
            requests.get(url=self.url)
            self.flag = True
        except Exception:
            self.flag = False

    def get_list(self):
        self.refresh_status()
        if self.flag:
            try:
                config_list = {}
                r = requests.get(url=self.url, headers=self.headers, timeout=2)
                soup = BeautifulSoup(r.content, 'lxml')
                files = soup.find_all(name='a')  # 匹配要爬去的链接，class用来筛除百度快照链接（百度快照：一般可以用来查看已失效网页的内容）
                for file in files:
                    # print(file['href'])
                    if file.text.endswith('.json'):
                        # print(file.text)
                        # print(file['href'])
                        r_get_url = requests.get(url=self.url + '/' + file['href'], headers=self.headers, timeout=8)
                        if r_get_url.status_code == 200:
                            # print(r_get_url.url)
                            # print(r_get_url.content)
                            config_list[file.text[:-5]] = r_get_url.content
                # print(config_list)
                return config_list
            except Exception as e:
                print(e, 'Community_spider', 'get_list')
                return False
        else:
            return False

    def upload_file(self, widget_name: str):
        try:
            request_headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Connection': 'close', 'Referer': 'http://8.131.57.209:5555/'}
            path = 'F:\\Urchin Framework\\logs\\tmp\\upload_tmp.json'
            # path = 'logs/tmp/upload_tmp.json'
            files = {'file': (widget_name + '.json', open(path, 'rb'), 'application/json', {'Expires': '0'})}
            r = requests.post(url=self.url, headers=request_headers, files=files)
            soup = BeautifulSoup(r.content, 'lxml')
            flag = soup.find_all(name='strong')
            if flag[0].text == 'Success:':
                print('上传成功！')
        except Exception as e:
            print(e, 'Community_spider', 'upload_file')

    def download_file(self, widget_name: str):
        try:
            r = requests.get(url=self.url + '/' + widget_name + '.json')
            if r.status_code == 200:
                return r.content
            return False
        except Exception as e:
            print(e, 'Community_spider', 'upload_file')

    def delete_file(self, widget_name: str):
        try:
            requests.get(url=self.url + '/delete/' + widget_name + '.json')
            return False
        except Exception as e:
            print(e, 'Community_spider', 'delete_file')
            return True


if __name__ == '__main__':
    aaa = Community_spider('8.131.57.209', '5555')
    # aaa.upload_file('2')
    # aaa.delete_file('2')
    aaa.get_list()

