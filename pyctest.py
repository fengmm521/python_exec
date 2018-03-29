#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading  
import time  


xxx = 'aaa'

class TESTObj(object):
    """docstring for TESTObj"""
    def __init__(self, arg):
        super(TESTObj, self).__init__()
        self.arg = arg
        
    def showP(self):
        print(self.arg)
        print(time.time())

def pyctest():
    print('pyctest....')
    return 'isRunOK'

def main():
    pyctest()


if __name__ == '__main__':
    main()