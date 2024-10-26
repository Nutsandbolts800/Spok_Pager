import requests
import sys

class pager:    
    def __init__(self, number):
        self.number = number
    
    def send_page(self, message):
        data = 'PIN={0}&MSSG={1}'.format(self.number, message)
        r = requests.post('http://www.usamobility.net/cgi-bin/wwwpage.exe', data=data)
        return r

if __name__ == "__main__":
    try:
        if sys.argv[1]:
            p = pager(sys.argv[1])
            if sys.argv[2]:
                p.send_page(sys.argv[2])
    except:
        print("usage: page.py [number] [message] or import and use the pager class")