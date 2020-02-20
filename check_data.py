import json
import logging
import os
import sys

import requests

base_url = '''https://acm.sdut.edu.cn/onlinejudge2/index.php/API_ng/'''
login_cookie = None


def get_solution_list(pid, limit_num):
    r = requests.get(base_url + 'solutions',
                     params={'problemId': pid, 'limit': limit_num, 'result': 1})
    return r


def down_code(pid, num):
    solution_list = get_solution_list(pid, num)
    tmp = json.loads(solution_list.content)

    code_list = []

    cnt_ = 0
    for r in tmp['data']['rows']:
        sid = r['solutionId']
        code_list.append(get_code(sid))

        cnt_ += 1
        logging.info('downloading\tpid: {}\tsid:{}\tcode: {}/{}'.format(pid, sid, cnt_, len(tmp['data']['rows'])))

    return code_list


def get_code(sid):
    r = requests.get(base_url + 'solutions/' + str(sid),
                     cookies=login_cookie)
    tmp = json.loads(r.content)
    return tmp['data']['code']


def login():
    r = requests.post(base_url + 'session',
                      json={'loginName': 'test_233', 'password': '123456'})
    global login_cookie
    login_cookie = r.cookies


def check_problem(pid, data_path):
    code_list = down_code(pid, 10)

    data_list = []
    for x in os.listdir(data_path):
        if x[-2:] == 'in':
            data_list.append(x[:-3])

    for x in code_list:
        if x is None:
            continue
        open('test.cpp', 'w').write(x)
        rst_code = os.system('g++ test.cpp -ansi')
        logging.info(rst_code)
        if rst_code != 0:
            continue

        cnt_ = 0
        for y in data_list:
            cnt_ += 1
            logging.info('running\tpid: {}\tcase: {}/{}'.format(pid, cnt_, len(data_list)))
            os.system('./a.out < {}/{}.in > test.out'.format(data_path, y))

            t1 = open('test.out').read()
            t2 = open(data_path + '/' + y + '.out').read()

            while len(t1) != 0 and t1[-1] == '\n':
                t1 = t1[:-1]
            while len(t2) != 0 and t2[-1] == '\n':
                t2 = t2[:-1]

            if t1 != t2:
                logging.error('pid {} error in test case {}'.format(pid, y))
                # return False
                break

    os.remove('test.cpp')
    os.remove('test.out')
    os.remove('a.out')


'''
use "python xxx.py <pid>" to check data
'''
if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)

    if len(sys.argv) < 2:
        exit(0)
    pid = int(sys.argv[1])
    logging.info('check problem: ' + str(pid))
    login()
    check_problem(pid, '.')
