# -*- coding: utf-8 -*- 
# @Time : 31/10/2020 
# @Author : thefool
# @contact: weiyiwu00@gmail.com 
# @File : compare.py

import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from Huffman import huffman
from Huffman import freq
from Huffman import demo


def compare(baselist=[2, 3, 5], type=0):
    with open('2-ary-string') as f:
        in_str = f.read()
        generate(in_str, baselist[0], type)
        f.close()

    with open('3-ary-string') as f:
        in_str = f.read()
        generate(in_str, baselist[1], type)
        f.close()

    with open('5-ary-string') as f:
        in_str = f.read()
        generate(in_str, baselist[2], type)
        f.close()
    pass


def generate(in_str, n_ary, type=0):
    """
    in 5-ary-string file, we have a string of {01234}, but actually,
    computer use binary data, so we generate binary code from x-ray
    string (using Huffman encode with digit of 2)

    :type
        0 : compare base 2\3\5
        1 : compare base n_ary\n_ary+1\n_ary+2\
    :return: string of {01}
    """

    freq_dict = freq.str_freq(in_str)

    freqs = list(freq_dict.items())

    n2_ray_huffman = huffman.HuffmanCode(freqs, 2)

    n2_ray_encoding = n2_ray_huffman.encode(in_str)

    if n_ary == 2:
        filename = "final-2-ray"
    elif n_ary == 3:
        filename = "final-3-ray"
    elif n_ary == 5:
        filename = "final-5-ray"

    # for the use of function compare_Compression_rati,
    # we should change the filename a little...
    if type == 1:
        if n_ary % 3 == 2:
            filename = "final-2-ray"
        elif n_ary % 3 == 0:
            filename = "final-3-ray"
        elif n_ary % 3 == 1:
            filename = "final-5-ray"

    huffman.out(n2_ray_encoding, filename)
    pass


def compare_Compression_ratio(filename="test.txt", baselist=[2, 3, 5]):
    demo.demo(0, filename, baselist)
    compare(baselist, 1)
    filesize = os.path.getsize(filename)
    filesize2 = os.path.getsize("final-2-ray")
    filesize3 = os.path.getsize("final-3-ray")
    filesize5 = os.path.getsize("final-5-ray")
    res1 = round(filesize2 / 8 / filesize * 100, 3)
    res2 = round(filesize3 / 8 / filesize * 100, 3)
    res3 = round(filesize5 / 8 / filesize * 100, 3)
    print(res1, "% \t")
    print(res2, "% \t")
    print(res3, "% \t")
    pass


if __name__ == '__main__':
    compare()
    # filename = "test.pdf"
    # for i in range(2, 35, 3):
    #     baselist =  [i, i + 1, i + 2]
    #     compare_Compression_ratio(filename=filename,baselist=baselist)
