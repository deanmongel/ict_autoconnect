#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
import os
import time

def auto_connect():
    print('open a phantomJS browser...\n')
    browser = webdriver.PhantomJS()
    browser.get('http://159.226.39.22')

    username, password = read_conf()

    browser.find_element_by_id('username').send_keys(username)
    browser.find_element_by_id('password').send_keys(password)
    #browser.find_element_by_id('button').click()
    browser.find_element_by_id('form2').submit()

    print('sleeping 10s...')
    time.sleep(10)
    browser.close()


def read_conf():
    un = ''
    pw = ''
    try:
        with open('user.conf', 'r') as file:
            for line in file.readlines():
                line = line.strip()
                if line == '':
                    continue
                if line[0] == '#':
                    continue
                if line.split('=')[0].strip() == 'username':
                    un = line.split('=')[1].strip()
                elif line.split('=')[0].strip() == 'password':
                    pw = line.split('=')[1].strip()
                else:
                    print('user.conf is a error format. \n')
    except IOError as e:
        print('cannot read user.conf file--' + str(e) + ', please create user.conf file. \n')
    return un, pw

def is_connect():
    flag = os.system('ping www.baidu.com')
    if flag == 0:
        return True
    return False

def con_connect():
    if is_connect():
        return 1
    else:
        auto_connect()
        if is_connect():
            print('\nCongratulations! Connect internet success.\n')
        else:
            print('\nFailed! Connect internet Failed.\n')
        return 1


if __name__ == '__main__':
    print("starting...")
    print('Please input Ctrl+C to break.')
    while 1:
        local_time = time.localtime(time.time())
        print('current time: ' + str(local_time.tm_hour) + ':' + str(local_time.tm_min) + ':' + str(local_time.tm_sec))
        con_connect()
        print('\nsleeping 1 hour ...\n')
        time.sleep(60*60)
