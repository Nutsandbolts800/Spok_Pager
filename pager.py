import requests
import sys

class pager:    
    def __init__(self, number):
        self.number = number
    
    def send_page(self, message):
        if len(message) < 240:
            data = 'PIN={0}&MSSG={1}'.format(self.number, message)
            try:
                r = requests.post('http://www.usamobility.net/cgi-bin/wwwpage.exe', data=data)
            except Exception as e:
                raise e
            return r
        else:
            print('Error: Message too long. More than 240 characters')
            return 1

if __name__ == "__main__":
    try:
        p = pager(sys.argv[1])
        p.send_page(sys.argv[2])

    except:
        print("usage: page.py [number] [message] or import and use the pager class")