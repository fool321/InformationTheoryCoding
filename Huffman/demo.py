# -*- coding: utf-8 -*-
# @Time : 30/10/2020
# @Author : thefool
# @contact: weiyiwu00@gmail.com
# @File : domo.py

from Huffman import huffman
from Huffman import freq
import base64


def enc(filename):
    with open(filename) as f:
        in_str = f.read()

    freq_dict = freq.str_freq(in_str)  # Create frequency dictionary.

    huffman.out_dic(freq_dict)

    freqs = list(freq_dict.items())  # HuffmanCode requires (symbol, freq) pairs.

    # base 2, 3, 5
    n2_ray_huffman = huffman.HuffmanCode(freqs, 2)
    n2_ray_encoding = n2_ray_huffman.encode(in_str)

    n3_ray_huffman = huffman.HuffmanCode(freqs, 3)
    n3_ray_encoding = n3_ray_huffman.encode(in_str)

    n5_ray_huffman = huffman.HuffmanCode(freqs, 5)
    n5_ray_encoding = n5_ray_huffman.encode(in_str)

    huffman.out(n2_ray_encoding, '2-ary-string')
    huffman.out(n3_ray_encoding, '3-ary-string')
    huffman.out(n5_ray_encoding, '5-ary-string')

    pass


def dec(filename):
    """
    decode the string file using given dictionary file

    :param filename: dictionary file
    """

    freq_dict = huffman.read_dic(filename)
    freqs = list(freq_dict.items())

    n2_ray_huffman = huffman.HuffmanCode(freqs, 2)
    out2 = n2_ray_huffman.decode(huffman.inpu("2-ary-string"))

    n3_ray_huffman = huffman.HuffmanCode(freqs, 3)
    out3 = n3_ray_huffman.decode(huffman.inpu("3-ary-string"))

    n5_ray_huffman = huffman.HuffmanCode(freqs, 5)
    out5 = n5_ray_huffman.decode(huffman.inpu("5-ary-string"))

    with open("2-ary-decode", 'w') as f:
        f.write(out2)
        f.close()
    with open("3-ary-decode", 'w') as f:
        f.write(out3)
        f.close()
    with open("5-ary-decode", 'w') as f:
        f.write(out5)
        f.close()
    # print(out2==out3) : true

    pass


def demo(type=0, filename=None, base_list=[2, 3, 5]):
    """
    :param type:
        0 : encode only ;
        1 : encode & decode
    :param base_list:
        build Huffman tree with base_list
    """
    with open(filename, 'rb') as f:
        # read file as binary
        st = f.read()

        res = "".join(chr(x) for x in st)  # type(res) : str
        in_str = res

        # str = base64.b64encode(st)
        # in_str = str.decode()
        # lehth = len(in_str)

    freq_dict = freq.str_freq(in_str)  # Create frequency dictionary.
    huffman.out_dic(freq_dict)
    freqs = list(freq_dict.items())  # HuffmanCode requires (symbol, freq) pairs.

    binary_huffman = huffman.HuffmanCode(freqs, base_list[0])  # Usual base 2 Huffman coding.
    n3_ray_huffman = huffman.HuffmanCode(freqs, base_list[1])
    n5_ray_huffman = huffman.HuffmanCode(freqs, base_list[2])

    binary_encoding = binary_huffman.encode(in_str)
    n3_ray_encoding = n3_ray_huffman.encode(in_str)
    n5_ray_encoding = n5_ray_huffman.encode(in_str)

    huffman.out(n3_ray_encoding, '3-ary-string')
    huffman.out(n5_ray_encoding, '5-ary-string')
    huffman.out(binary_encoding, '2-ary-string')

    # decode and output
    if type == 1:
        out = n3_ray_huffman.decode(n3_ray_encoding)
        out_byte = b''
        file_str = open("out_" + filename, 'wb')
        for i in range(len(out)):
            out_byte = out_byte + ord(out[i]).to_bytes(length=1, byteorder='big')
        # file_str.write(base64.b64decode(out.encode()))
        file_str.write(out_byte)
        file_str.close()

    pass


def main():
    """ use Huffman in command line"""

    print("\n---- let us enjoy Huffman -----\n")
    type = int(input("0 for encode only, 1 for encode and decode, 3 for decode\n"))

    if type == 0:
        filename = input("please input the filename : \n")
        demo(0, filename)
        print("-----  Successfully !!!  -----\n")
        print("the frequency has been write to the 'dicfile' \n")
        print("and the file has been coverted to the 'n-ary-string' \n")
    elif type == 1:
        filename = input("please input the filename : \n")
        demo(1, filename)
        print("-----  Successfully !!!  -----\n")
        print("the frequency has been write to the 'dicfile' \n")
        print("and the file has been coverted to the 'out_filename' \n")
    elif type == 3:
        dicname = input("please input the dicfile for decode : \n")
        print("-----  we will decode 'n-ary-string' file to 'n-ary-decode' file -----\n")
        print("-----  maybe you should change the filename -----\n")
        dec(dicname)
        print("-----  Successfully !!!  -----\n")

    print("----- the end -----\n\n")
    pass


if __name__ == '__main__':
    main()
    # demo(0,"bigtest.txt")
    # demo(1,"test.zip")
