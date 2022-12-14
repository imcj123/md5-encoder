#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import chardet


def get_file_md5(file_tuple):
    """
    计算文件的md5
    :param file_name:
    :return:
    """
    md5_list =[]
    for file_name in file_tuple:
        m = hashlib.md5()  # 创建md5对象
        with open(file_name, 'rb') as fobj:
            while True:
                data = fobj.read(1024)
                if not data:
                    break
                m.update(data)  # 更新md5对象
        md5_list.append(m.hexdigest())
    return md5_list  # 返回md5对象


def get_str_md5(content):
    """
    计算字符串md5
    :param content:
    :return:
    """

    m = hashlib.md5(content.encode("gb2312"))  # 创建md5对象
    return m.hexdigest()


if __name__ == '__main__':
    print(get_file_md5('main.py'))
    print(get_str_md5("陈杰"))
