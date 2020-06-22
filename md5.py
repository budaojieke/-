import hashlib
import os
from PIL import Image
import numpy as np

set_path = 'E:/images/'
files_path = 'E:/temp/'


count = 0  # 删除的文件计数

def get_md5(filename):
    m = hashlib.md5()
    mfile = open(filename, "rb")
    m.update(mfile.read())
    mfile.close()
    md5_value = m.hexdigest()
    return md5_value


def create_md5_set(path):
    count = 0
    md5_set = set()  # 创建一个set()
    set_files = os.listdir(path)  # 遍历文件夹下的所有文件
    for file in set_files:
        file_path = set_path + file  # 获得完整的路径
        file_md5 = get_md5(file_path)
        if file_md5 not in md5_set:  # 如果当前的md5码不在集合中
            md5_set.add(file_md5)  # 则添加当前md5码到集合中
            count += 1
    print('set size：', count)
    return md5_set

md5_set = create_md5_set(set_path)

files = os.listdir(files_path)  # 遍历文件夹下的所有文件
for file in files:
    file_path = files_path + file  # 获得完整的路径
    file_md5 = get_md5(file_path)
    if file_md5 in md5_set:  # 如果当前的md5码不在集合中
        os.remove(file_path)
        print('delete :', file_path)
