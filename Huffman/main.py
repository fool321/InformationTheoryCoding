# -*- coding: utf-8 -*-
# @Time : 31/10/2020
# @Author : thefool
# @contact: weiyiwu00@gmail.com
# @File : main.py

import sys, os
from Huffman import demo

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


def demo_enc():
    demo.enc('bigtest.txt')
    pass


def demo_dec():
    demo.dec('dicfile')


if __name__ == '__main__':
    demo.main()
