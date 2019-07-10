# -*- coding: utf-8 -*-
# @File  : Calculate.py
# @Author: 周璐
# @Date  : 2019/7/9 21:56
# @Desc  :

from test_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Calculate(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

    def And(a, b):
        return int(a and b)

    def Or(a, b):
        return int(a or b)

    def Nand(a, b):
        return int(not Calculate.And(a, b))

    def Xor(a, b):
        return Calculate.And(Calculate.Nand(a, b), Calculate.Or(a, b))

    def Half_adder(a, b):
        s = Calculate.Xor(a, b)
        co = Calculate.And(a, b)
        return s, co

    def Full_adder(a, b, ci):
        s, co1 = Calculate.Half_adder(a, b)
        s, co2 = Calculate.Half_adder(ci, s)
        co = Calculate.Or(co1, co2)
        return s, co

    # 二进制字符-1运算
    def Eight_bit_adder(x, y, sub, length):  # sub=0:add, sub=1:subtract
        result = ""
        y = list(y)
        for i in range(len(y)):
            y[i] = Calculate.Xor(sub, y[i])
        ans = [Calculate.Full_adder(int(x[length * 4 - 1]), int(y[length * 4 - 1]), sub)]
        for i in range(length * 4 - 2, -1, -1):
            ans.insert(0, Calculate.Full_adder(int(x[i]), int(y[i]), ans[0][1]))
        ans.insert(0, (Calculate.Xor(sub, ans[0][1]), None))
        for eachBit in ans:
            result += str(eachBit[0])
        return result[1:]

    # 十六进制转换二进制
    def exchange_hex_to_binary(hex_num):
        return str(bin(int(hex_num.upper(), 16)))[2:]

    # 二进制转换十进制
    def exchange_binary_to_int(binary_num):
        return str(int(binary_num, 2))

    # 十六进制转换十进制
    def exchange_hex_to_int(hex_num):
        return str(int(hex_num.upper(), 16))

    def get_complement_code(num):
        # print(~int(num))
        return ~int(num)

    # 二进制字符补齐0，为-1运算前做处理
    def polish_binary_code(binary_code):
        length = len(binary_code) % 4
        if length == 0:
            return binary_code
        else:
            for i in range(0, 4 - length):
                binary_code = "0" + binary_code
            return binary_code

    # 二进制字符1补齐0，为-1运算前做处理
    def polish_sub(binary_code):
        length = len(binary_code)
        result = "1"
        for i in range(0, length - 1):
            result = "0" + result
        return result

    def calculate_with_symbol(num, coefficient, offset, length):
        binary_code = Calculate.polish_binary_code(Calculate.exchange_hex_to_binary(num))  # 将输入的十六进制的字符转换为二进制，并补齐0
        if binary_code[0] == "1":
            Calculate.Eight_bit_adder(binary_code, Calculate.polish_sub(binary_code), 1, length)
            compement_code = Calculate.get_complement_code(Calculate.exchange_hex_to_int(num))
            result = compement_code * coefficient + offset
            print("-----------", num, coefficient, offset, result)
        elif binary_code[0] == "0":
            result = Calculate.exchange_hex_to_int(num) * coefficient + offset
            print(num, coefficient, offset, result)

    def calculate_without_symbol(num, coefficient, offset):
        int_num = int(Calculate.exchange_hex_to_int(num))
        result = int_num * coefficient + offset
        print(num, coefficient, offset, result)

    @staticmethod
    def calculate_main(num, length, coefficient, offset, symbol):
        if symbol == 1:
            Calculate.calculate_with_symbol(num, coefficient, offset, length)
        else:
            Calculate.calculate_without_symbol(num, coefficient, offset)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Calculate()
    window.show()
    sys.exit(app.exec_())
    # num = input("请输入需要转换并计算的字符：")
    # coefficient = input("请输入系数：")
    # offset = input("请输入偏移量：")
    # symbol = input("请输入有无符号（0为无，1为有）：")
    # length = input("请输入长度：")
    Calculate.calculate_main("BC", 2, 1, 1, 1)
    Calculate.calculate_main("BC", 2, 1, 1, 0)
    # Calculate.get_complement_code(5)
    # Calculate.Eight_bit_adder("111110111011", "000000000001", 1, 3)
    # Calculate.polish_binary_code("11111101")
    # Calculate.polish_sub("11111101")
    # Calculate.calculate_main("BD", 1, 1, 1)
    # Calculate.calculate_main("13", 1, 1, 1)
    # Calculate.calculate_main("2", 1, 1, 1)
