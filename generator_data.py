import os

import cyaron
from cyaron import IO
from cyaron import randint
from cyaron import randrange


def p2176():
    if not os.path.exists('2176'):
        os.mkdir('2176')
    os.system('g++ code/2176.cpp')

    # case 1 1 #简单样例
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

    # case 3 4 #小数据范围，暴力可过
    io = IO(file_prefix="2176/", data_id=4)
    for x in range(10000):
        a = randrange(-1, 22)
        b = randrange(-1, 22)
        c = randrange(-1, 22)
        io.input_writeln(a, b, c)
    io.output_gen('./a.out')

    os.remove('./a.out')


if __name__ == '__main__':
    p2176()
