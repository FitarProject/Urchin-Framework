#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# author: Fitar
# 文件结构提取

import os


def get_structure(mypath):
    all_path = []
    all_file = []
    for root, _, files in os.walk(mypath, topdown=True):
        '''
        print(root[(len(mypath)+1):].replace('\\','/'))
        print(dirs)
        for i in files:
            print(i)
        print('****************')
        '''
        #all_path.append(root)
        all_path.append(os.path.relpath(root,start=mypath).replace('\\','/') + '/')
        for name in files:
            rel_path = root[(len(mypath)+1):]
            all_file.append(os.path.join(rel_path, name).replace('\\','/'))
    return (all_path,all_file)

def output(out_list):
    for i in out_list:
        print(i)

if __name__ == '__main__':
    #输入要提取的根目录
    try:
        mypath = input('请输入要提取的文件目录：')
        all_path, all_file = get_structure(mypath)
    except KeyboardInterrupt:
        print("\nCanceled by the user")
        exit(0)
    #打印相对目录结构
    output(all_path)
    #打印所有非目录文件
    output(all_file)
    #将字典写入文件
    with open('dict_file.txt', 'w') as f:
        for file_path in all_file:
            f.write(file_path + '\n')