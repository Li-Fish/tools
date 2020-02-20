import os
import random

import cyaron
from cyaron import IO
from cyaron import randint
from cyaron import randrange
from cyaron import String


def p2176():
    if not os.path.exists('2176'):
        os.mkdir('2176')
    os.system('g++ code/2176.cpp')

    # case 1 1 #简单输入
    io = IO(file_prefix="2176/", data_id=1)
    io.input_writeln('3 3 3')

    io.output_gen('./a.out')

    # case 2 5 #不考虑输入大于 20
    io = IO(file_prefix="2176/", data_id=2)
    for x in range(50):
        a = randrange(-1, 21)
        b = randrange(-1, 21)
        c = randrange(-1, 21)
        io.input_writeln(a, b, c)
    io.output_gen('./a.out')

    # case 3 4 #小数据范围，暴力可过
    io = IO(file_prefix="2176/", data_id=3)
    for x in range(50):
        a = randrange(-1, 10)
        b = randrange(-1, 10)
        c = randrange(-1, 10)
        io.input_writeln(a, b, c)
    io.output_gen('./a.out')

    # case 3 4 #大数据范围
    io = IO(file_prefix="2176/", data_id=4)
    for x in range(10000):
        a = randrange(-1, 22)
        b = randrange(-1, 22)
        c = randrange(-1, 22)
        io.input_writeln(a, b, c)
    io.output_gen('./a.out')

    os.remove('./a.out')
    open('2176/scores', 'w').write(open('raw_data/scores/2176').read())


def p1730():
    if not os.path.exists('1730'):
        os.mkdir('1730')
    os.system('g++ code/1730.cpp')

    # case 1 1 #简单输入
    io = IO(file_prefix="1730/", data_id=1)
    io.input_writeln('5')
    io.input_writeln('10')
    io.input_writeln('3 8')
    io.input_writeln('8 1 0')
    io.input_writeln('2 7 4 4')
    io.input_writeln('4 5 2 6 5')

    io.output_gen('./a.out')

    # case 2~10 #小数据
    for x in range(2, 11):
        io = IO(file_prefix="1730/", data_id=x)
        n = randrange(1, 11)
        io.input_writeln(n)
        for y in range(n):
            row = []
            for z in range(y + 1):
                row.append(randrange(0, 100))
            io.input_writeln(row)

        io.output_gen('./a.out')

    # case 11~20 #大数据
    for x in range(11, 21):
        io = IO(file_prefix="1730/", data_id=x)
        n = randrange(90, 101)
        io.input_writeln(n)
        for y in range(n):
            row = []
            for z in range(y + 1):
                row.append(randrange(0, 100))
            io.input_writeln(row)

        io.output_gen('./a.out')

    open('1730/scores', 'w').write(open('raw_data/scores/1730').read())


def p2852():
    if not os.path.exists('2852'):
        os.mkdir('2852')
    os.system('g++ code/2852.cpp')

    # case 1 1 #简单输入
    io = IO(file_prefix="2852/", data_id=1)
    io.input_writeln('5')
    io.input_writeln('10')
    io.input_writeln('3 8')
    io.input_writeln('8 1 0')
    io.input_writeln('2 7 4 4')
    io.input_writeln('4 5 2 6 5')

    io.output_gen('./a.out')

    # case 2~10 #小数据
    for x in range(2, 11):
        io = IO(file_prefix="2852/", data_id=x)
        n = randrange(1, 11)
        io.input_writeln(n)
        for y in range(n):
            row = []
            for z in range(y + 1):
                row.append(randrange(0, 100))
            io.input_writeln(row)

        io.output_gen('./a.out')

    # case 11~20 #大数据
    for x in range(11, 21):
        io = IO(file_prefix="2852/", data_id=x)
        n = randrange(90, 101)
        io.input_writeln(n)
        for y in range(n):
            row = []
            for z in range(y + 1):
                row.append(randrange(0, 100))
            io.input_writeln(row)

        io.output_gen('./a.out')

    open('2852/scores', 'w').write(open('raw_data/scores/2852').read())


def p2080():
    if not os.path.exists('2080'):
        os.mkdir('2080')
    os.system('g++ code/2080.cpp')

    # case 1 1 #简单输入
    io = IO(file_prefix="2080/", data_id=1)
    io.input_writeln('ABCBDABF')
    io.input_writeln('BDCABAF')
    io.output_gen('./a.out')

    # case 2~10 #小数据输入
    for x in range(2, 11):
        io = IO(file_prefix="2080/", data_id=x)
        a = String.random(randrange(7, 11), charset=cyaron.ALPHABET_CAPITAL)
        b = String.random(randrange(7, 11), charset=cyaron.ALPHABET_CAPITAL)
        io.input_writeln(a)
        io.input_writeln(b)
        io.output_gen('./a.out')

    # case 11~20 #大数据输入
    for x in range(11, 21):
        io = IO(file_prefix="2080/", data_id=x)
        a = String.random(randrange(490, 501), charset=cyaron.ALPHABET_CAPITAL)
        b = String.random(randrange(490, 501), charset=cyaron.ALPHABET_CAPITAL)
        io.input_writeln(a)
        io.input_writeln(b)
        io.output_gen('./a.out')

    open('2080/scores', 'w').write(open('raw_data/scores/2080').read())


def p1299():
    if not os.path.exists('1299'):
        os.mkdir('1299')
    os.system('g++ code/1299.cpp')

    # case 1 1 #简单输入
    io = IO(file_prefix="1299/", data_id=1)
    io.input_writeln('7')
    io.input_writeln('1 7 3 5 9 4 10')
    io.output_gen('./a.out')

    # case 2~10 #小数据输入
    for x in range(2, 11):
        io = IO(file_prefix="1299/", data_id=x)
        n = randrange(1, 10)
        io.input_writeln(n)
        data_list = []
        for y in range(n):
            data_list.append(randrange(0, 10000 + 1))
        io.input_writeln(data_list)
        io.output_gen('./a.out')

    # case 11~20 #大数据输入
    for x in range(11, 21):
        io = IO(file_prefix="1299/", data_id=x)
        n = randrange(900, 1000 + 1)
        io.input_writeln(n)
        data_list = []
        for y in range(n):
            data_list.append(randrange(0, 10000 + 1))
        io.input_writeln(data_list)
        io.output_gen('./a.out')

    open('1299/scores', 'w').write(open('raw_data/scores/1299').read())


def p2171():
    if not os.path.exists('2171'):
        os.mkdir('2171')
    os.system('g++ code/2171.cpp')

    # case 1 1 #简单输入
    io = IO(file_prefix="2171/", data_id=1)
    io.input_writeln('7')
    io.input_writeln('1 7 3 5 9 4 10')
    io.output_gen('./a.out')

    # case 2~10 #小数据输入
    for x in range(2, 11):
        io = IO(file_prefix="2171/", data_id=x)
        n = randrange(1, 10)
        io.input_writeln(n)
        data_list = []
        for y in range(n):
            data_list.append(randrange(0, 1000 + 1))
        io.input_writeln(data_list)
        io.output_gen('./a.out')

    # case 11~20 #大数据输入
    for x in range(11, 21):
        io = IO(file_prefix="2171/", data_id=x)
        n = randrange(900, 1000 + 1)
        io.input_writeln(n)
        data_list = []
        for y in range(n):
            data_list.append(randrange(0, 1000 + 1))
        io.input_writeln(data_list)
        io.output_gen('./a.out')

    open('2171/scores', 'w').write(open('raw_data/scores/2171').read())


def p1304():
    if not os.path.exists('1304'):
        os.mkdir('1304')
    os.system('g++ code/1304.cpp')

    # case 1 1 #简单输入
    io = IO(file_prefix="1304/", data_id=1)
    io.input_writeln('2 2')
    io.input_writeln('0 2')
    io.input_writeln('1 0')
    io.output_gen('./a.out')

    # case 2~5 只有自然数，小数据
    for x in range(2, 6):
        io = IO(file_prefix="1304/", data_id=x)

        n = randrange(2, 6)
        m = randrange(2, 6)
        io.input_writeln(n, m)

        for _ in range(n):
            data_list = []
            for __ in range(m):
                data_list.append(randrange(0, 11))
            io.input_writeln(data_list)

        io.output_gen('./a.out')

    # case 6~10 只有自然数，小数据
    for x in range(6, 11):
        io = IO(file_prefix="1304/", data_id=x)

        n = randrange(8, 11)
        m = randrange(8, 11)
        io.input_writeln(n, m)

        for _ in range(n):
            data_list = []
            for __ in range(m):
                data_list.append(randrange(0, 11))
            io.input_writeln(data_list)

        io.output_gen('./a.out')

    # case 11~20 完全数据
    for x in range(11, 21):
        io = IO(file_prefix="1304/", data_id=x)

        n = randrange(8, 11)
        m = randrange(8, 11)
        io.input_writeln(n, m)

        for _ in range(n):
            data_list = []
            for __ in range(m):
                data_list.append(randrange(-10, 11))
            io.input_writeln(data_list)

        io.output_gen('./a.out')

    open('1304/scores', 'w').write(open('raw_data/scores/1304').read())


def p1366():
    if not os.path.exists('1366'):
        os.mkdir('1366')
    os.system('g++ code/1366.cpp')

    # case 1 1 #简单输入
    io = IO(file_prefix="1366/", data_id=1)
    io.input_writeln('5')
    io.input_writeln('5 1')
    io.input_writeln('4 1')
    io.input_writeln('6 1')
    io.input_writeln('7 2')
    io.input_writeln('8 3')
    io.input_writeln('0')
    io.output_gen('./a.out')

    # case 2 19 #大数据输入
    io = IO(file_prefix="1366/", data_id=2)
    io.input_write(open('raw_data/1366.in').read())
    io.output_gen('./a.out')

    open('1366/scores', 'w').write(open('raw_data/scores/1366').read())


def p1008():
    if not os.path.exists('1008'):
        os.mkdir('1008')
    os.system('g++ code/1008.cpp')

    # case 1 1 #简单输入
    io = IO(file_prefix="1008/", data_id=1)
    io.input_writeln('1')
    io.input_writeln('3')
    io.input_writeln('ab')
    io.input_writeln('ab')
    io.input_writeln('bc')
    io.output_gen('./a.out')

    # case 2~11 # n = 2
    for case_id in range(2, 11):
        io = IO(file_prefix="1008/", data_id=case_id)
        io.input_writeln(20)
        for x in range(20):
            io.input_writeln(2)
            b = String.random(randrange(90, 100), charset=cyaron.ALPHABET_CAPITAL)
            c = String.random(randrange(90, 100), charset=cyaron.ALPHABET_CAPITAL)
            io.input_writeln(b)
            io.input_writeln(c)
        io.output_gen('./a.out')

    # case 11~20 #边界输入
    for case_id in range(11, 21):
        io = IO(file_prefix="1008/", data_id=case_id)
        io.input_write(open('raw_data/1008/data{}.in'.format(case_id - 10)).read())
        io.output_gen('./a.out')

    open('1008/scores', 'w').write(open('raw_data/scores/1008').read())


def p1269():
    if not os.path.exists('1269'):
        os.mkdir('1269')
    os.system('g++ code/1269.cpp')

    # case 1~10 #边界输入
    for case_id in range(1, 11):
        io = IO(file_prefix="1269/", data_id=case_id)
        io.input_write(open('raw_data/1269/data{}.in'.format(case_id)).read())
        io.output_gen('./a.out')

    open('1269/scores', 'w').write(open('raw_data/scores/1269').read())


if __name__ == '__main__':
    random.seed(233)
    p2176()
    p1730()
    p2852()
    p2080()
    p1299()
    p2171()
    p1304()
    p1366()
    p1008()
    p1269()
