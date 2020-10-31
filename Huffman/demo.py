# -*- coding: utf-8 -*-
# @Time : 30/10/2020
# @Author : thefool
# @contact: weiyiwu00@gmail.com
# @File : domo.py

from Huffman import huffman
from Huffman import freq
import base64
import textwrap


# huffman.out_dic(freq_dict)
# dic = huffman.read_dic('dicfile.txt')
# print(freq_dict==dic) :true

def enc(filename):
    with open(filename) as f:
        in_str = f.read()

    freq_dict = freq.str_freq(in_str)  # Create frequency dictionary.

    huffman.out_dic(freq_dict)

    freqs = list(freq_dict.items())  # HuffmanCode requires (symbol, freq) pairs.

    # base 2, 3, 5
    n2_ray_huffman = huffman.HuffmanCode(freqs, 2)
    n3_ray_huffman = huffman.HuffmanCode(freqs, 3)
    n5_ray_huffman = huffman.HuffmanCode(freqs, 5)
    ascii_encoding = huffman.ascii_encode(in_str)  # 8-bit ascii encoding.

    n2_ray_encoding = n2_ray_huffman.encode(in_str)
    n3_ray_encoding = n3_ray_huffman.encode(in_str)
    n5_ray_encoding = n5_ray_huffman.encode(in_str)

    huffman.out(n2_ray_encoding, '2-ary-string')
    huffman.out(n3_ray_encoding, '3-ary-string')
    huffman.out(n5_ray_encoding, '5-ary-string')

    pass


def dec(filename):
    """

    :param filename: dictionary file
    :return:
    """
    freq_dict = huffman.read_dic(filename)
    freqs = list(freq_dict.items())

    n2_ray_huffman = huffman.HuffmanCode(freqs, 2)
    n3_ray_huffman = huffman.HuffmanCode(freqs, 3)
    n5_ray_huffman = huffman.HuffmanCode(freqs, 5)

    n2_ray_encoding = huffman.inpu("2-ary-string")
    n3_ray_encoding = huffman.inpu("3-ary-string")
    n5_ray_encoding = huffman.inpu("5-ary-string")

    out2 = n2_ray_huffman.decode(huffman.inpu("2-ary-string"))
    out3 = n3_ray_huffman.decode(huffman.inpu("3-ary-string"))
    out5 = n5_ray_huffman.decode(huffman.inpu("5-ary-string"))

    with open("2-ary-decode",'w') as f:
        f.write(out2)
        f.close()
    with open("3-ary-decode",'w') as f:
        f.write(out3)
        f.close()
    with open("5-ary-decode",'w') as f:
        f.write(out5)
        f.close()
    # print(out2==out3) : true
    # print(out3==out5)

    pass


def demo(type=0):
    if type == 1:
        with open('test.jpg', 'rb') as f:
            str = base64.b64encode(f.read())
            in_str = str.decode()
    else:
        with open("./test.txt") as f:
            in_str = f.read()

    freq_dict = freq.str_freq(in_str)  # Create frequency dictionary.

    freqs = list(freq_dict.items())  # HuffmanCode requires (symbol, freq) pairs.

    binary_huffman = huffman.HuffmanCode(freqs, 2)  # Usual base 2 Huffman coding.
    hexadecimal_huffman = huffman.HuffmanCode(freqs, 16)  # Or maybe base 16.

    ascii_encoding = huffman.ascii_encode(in_str)  # 8-bit ascii encoding.
    binary_encoding = binary_huffman.encode(in_str)
    hexadecimal_encoding = hexadecimal_huffman.encode(in_str)

    huffman.out(hexadecimal_encoding, 'hexstring')
    huffman.out(binary_encoding, 'binarystring')

    str1 = huffman.inpu('hexstring')
    # str2 = hexadecimal_encoding
    # flag = (str1 == str2)

    out = hexadecimal_huffman.decode(hexadecimal_encoding)
    # out1 = hexadecimal_huffman.decode(str1)
    # flag2 = (out == out1)

    if type == 1:
        file_str = open('outputjpg.jpg', 'wb')
        file_str.write(base64.b64decode(out.encode()))
        file_str.close()
    else:
        huffman.out(out, 'decode')

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
    demo(0)
    # demo(1)
