import pager
import sys


try:
    if sys.argv[1]:
        p = pager(sys.argv[1])
        if sys.argv[2]:
            p.send_page(sys.argv[2])
except:
    print("usage: page.py [number] [message] or import and use the pager class")