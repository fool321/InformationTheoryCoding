# -*- coding: utf-8 -*-
# @Time : 30/10/2020
# @Author : thefool
# @contact: weiyiwu00@gmail.com
# @File : domo.py

from Huffman import huffman
from Huffman import freq
# import huffman
# import freq
import textwrap
import json


def out_dic(dict):
    """output the dictionary into 'dicfile.txt' for decode,
    which contains the freq info

    :param dict: the dict to be write
    :return: null
    """
    with open('dicfile.txt', 'w') as f:
        print(dict, file=f)

    pass


def read_dic(filename='dicfile.txt'):
    """
    reload the dictionary file to rebuild the Huffman tree for decoding

    :return: dictionary contains the freq info
    """
    with open(filename, 'r') as f:
        content = f.read()
    dic = eval(content)
    return dic
    pass


def out(str, filename):
    """output str into the file """

    with open(filename, 'w') as f:
        print(str, file=f)
    pass


def demo():
    with open("./test.txt") as f:
        in_str = f.read()

    freq_dict = freq.str_freq(in_str)  # Create frequency dictionary.
    out_dic(freq_dict)
    dic = read_dic('dicfile.txt')
    # print(freq_dict==dic) :true

    freqs = list(freq_dict.items())  # HuffmanCode requires (symbol, freq) pairs.

    binary_huffman = huffman.HuffmanCode(freqs, 2)  # Usual base 2 Huffman coding.
    hexadecimal_huffman = huffman.HuffmanCode(freqs, 15)  # Or maybe base 5.

    ascii_encoding = huffman.ascii_encode(in_str)  # 8-bit ascii encoding.
    binary_encoding = binary_huffman.encode(in_str)
    hexadecimal_encoding = hexadecimal_huffman.encode(in_str)

    # print("ascii encoding:")
    # print(textwrap.fill(ascii_encoding))
    # print()
    # print("binary encoding:")
    # print(textwrap.fill(binary_encoding))
    # print()



    print("hex encoding:")
    hexstring = textwrap.fill(hexadecimal_encoding)
    print(hexstring)

    out(hexstring, 'hexstring.txt')
    out(textwrap.fill((binary_encoding)),'binarystring.txt')

    # print()

    print("Decoding hex:")
    print(hexadecimal_huffman.decode(hexadecimal_encoding))

    print("Sizes relative to ascii:")
    print("\t ascii:", len(ascii_encoding) / len(ascii_encoding))
    print("\tbinary:", len(binary_encoding) / len(ascii_encoding))
    print("\t   hex:", len(hexadecimal_encoding) / len(ascii_encoding))

    pass


def main():
    """
    1) compare 2\3\5 -ary huffman encoding using text file
    2) compare 2\3\5 -ary huffman encoding using picture file
    3) compare both of them and come to conclusion

    :return: null, (print out the result
    """
    with open("./test.txt") as f:
        in_str = f.read()

    freq_dict = freq.str_freq(in_str)  # Create frequency dictionary.
    freqs = list(freq_dict.items())  # HuffmanCode requires (symbol, freq) pairs.

    binary_huffman = huffman.HuffmanCode(freqs, 2)  # Usual base 2 Huffman coding.
    hexadecimal_huffman = huffman.HuffmanCode(freqs, 15)  # Or maybe base 5.

    ascii_encoding = huffman.ascii_encode(in_str)  # 8-bit ascii encoding.
    binary_encoding = binary_huffman.encode(in_str)
    hexadecimal_encoding = hexadecimal_huffman.encode(in_str)

    pass


if __name__ == '__main__':
    demo()
    # main()

# TODO : encode and decode the picture(png\jpg..?) using huffman? how to do that ?
# TODO : figure out how the n-ary Huffman decoding work.
