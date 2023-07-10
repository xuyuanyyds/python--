#! /usr/bin/python
# -*-coding: UTF-8 -*-
import os
import time
from threading import Thread

def say():
    time.sleep(2)
    print("%s say hello "%os.getpid())


def main():
    t1 = Thread(target=say)
    t2 = Thread(target=say)

    t1.start()
    t2.start()

    print("主线程")

    pass




    pass

if __name__=='__main__':
    main()
