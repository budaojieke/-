import os
from hashlib import md5

file_md5_value = []
file_dict = {}

same_file_cnt = 0

FILE_DIR_PATH = 'E:/temp/'

def generate_file_md5value(fpath):
    '''以文件路径作为参数，返回对文件md5后的值'''
    m = md5()
    # 需要使用二进制格式读取文件内容
    a_file = open(fpath, 'rb')
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()

def doMd5sum(file_path):
    file_dict = {}
    file_md5_value = []
    filename_list = os.listdir(file_path)  # 扫描目标路径的文件,将文件名存入列表
    for file_name in filename_list:
        file_full_path = file_path + file_name
        md5_value = generate_file_md5value(file_full_path)
        file_md5_value.append(md5_value)
        file_dict[file_name] = md5_value
    print("file_md5_value len: %d" % len(file_md5_value))
    return file_md5_value, file_dict

def doFilesMd5Value(file_path):
    global file_md5_value
    global file_dict
    file_md5_value, file_dict = doMd5sum(file_path)

def get_key (dict, value):
    return [k for k, v in dict.items() if v == value]

def deleteFile(file_name):
    for i in range(len(file_name) - 1):
        file_name_full_path = FILE_DIR_PATH + file_name[i]
        if os.path.exists(file_name_full_path):
            print("delete file name:%s" % file_name_full_path)
            os.remove(file_name_full_path)


def dropRepeatedFile():
    list_output = []
    global same_file_cnt

    for i in file_md5_value:
        if i not in list_output:
            list_output.append(i)
        else:
            file_name = get_key(file_dict, i)
            same_file_cnt += 1
            print("same file name is: %s" % file_name)
            deleteFile(file_name)
    print("same file nums:%d" % same_file_cnt)

if __name__ == '__main__':
    doFilesMd5Value(FILE_DIR_PATH)
    dropRepeatedFile()
