# -*- coding: utf-8 -*-
# @Time : 31/10/2020
# @Author : thefool
# @contact: weiyiwu00@gmail.com
# @File : main.py

import sys, os, argparse,time

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from Huffman import huffman
from Huffman import demo


def demo_enc():
    demo.enc('bigtest.txt')
    pass

def demo_dec():
    demo.dec('dicfile')


if __name__ == '__main__':
    demo.main()
    # main()
    # demo_enc()
    # t1 = time.time()
    # demo_enc()
    # demo_dec()
    # print(time.time()-t1)
    # f = open('bigtest.txt','r')
    # g = open('bbbbbigtest.txt','w')
    #
    # res = f.read()
    # for i in range(0,3):
    #     res = res + res
    # g.write(res)