# -*- coding: utf-8 -*-
# @Time : 31/10/2020
# @Author : thefool
# @contact: weiyiwu00@gmail.com
# @File : main.py

import sys, os, argparse

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

def main():
    parser = argparse.ArgumentParser(description="Simple Huffman encoding and decoding")
    parser.add_argument("-e", '--encode', default='bigtest.txt', help="input the filename for encoding")
    parser.add_argument("-d", "--decode", default='decode', help="input the filename for decoding")
    parser.add_argument("-k", "--key", default='dictfile', help="input the dictionary file")

    args = parser.parse_args()
    encodefile = args.encode
    decodefile = args.decode
    dic = args.dictfile

    print(encodefile, decodefile, dic)

    pass


if __name__ == '__main__':
    # main()
    demo_dec()
# import argparse
#
# def main():
#     parser = argparse.ArgumentParser(description="Demo of argparse")
#     parser.add_argument('-n','--name', default=' Li ')
#     parser.add_argument('-y','--year', default='20')
#     args = parser.parse_args()
#     print(args)
#     name = args.name
#     year = args.year
#     print('Hello {}  {}'.format(name,year))
#
# if __name__ == '__main__':
#     main()
