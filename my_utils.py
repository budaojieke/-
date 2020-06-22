import os
import glob
import shutil
from PIL import Image

# for file in os.scandir(path):
#     print(file.name)
def move_file(srcPath, dstPath):
    i = 0
    for dirpath, dirnames, filenames in os.walk(srcPath):
        for file in filenames:
            try:
                shutil.copy(os.path.join(dirpath, file), dstPath)
            except shutil.Error:
                pass

def move_file_rename(srcPath, dstPath):
    i = 0
    for dirpath, dirnames, filenames in os.walk(srcPath):
        # for file in glob.glob(filenames + '*.png'):
        #     print(file)
        files = os.path.join(dirpath, '*.png')
        for file in glob.glob(files):
            new_file = dstPath + '\\' + str(i) + '.png'
            shutil.move(file, new_file)
            i += 1
            print(new_file)
        files = os.path.join(dirpath, '*.jpeg')
        for file in glob.glob(files):
            new_file = dstPath + '\\' + str(i) + '.jpeg'
            shutil.move(file, new_file)
            i += 1
            print(new_file)
        files = os.path.join(dirpath, '*.jpg')
        for file in glob.glob(files):
            new_file = dstPath + '\\' + str(i) + '.jpg'
            shutil.move(file, new_file)
            i += 1
            print(new_file)


def rename_file_list(path, string, start_index):
    i = start_index
    filename_list = os.listdir(path)
    for file in filename_list:
        old_name = path + file
        new_name = path + string + str(i) + ".jpg"
        os.rename(old_name, new_name)
        print(old_name, new_name)
        i += 1

def delete_img_with_size(path, size):
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            filepath = os.path.join(dirpath, file)
            img = Image.open(filepath)
            if img.width < size or img.height < size:
                print(img.size)
                img.close()
                os.remove(filepath)
