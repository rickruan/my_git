# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='Rick Ruan'

import time,threading

def Rolling():
    print('Thread %s is running....' %threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('Thread %s>>>%s' %(threading.current_thread().name,n))
        time.sleep(1)
    print('Thread %s is ended' %threading.current_thread().name)

print('Thread %s is running....' %threading.current_thread().name)
t = threading.Thread(target=Rolling,name='RollingThread')
t.start()
t.join()
print('thread %s ended.' %threading.current_thread().name)
