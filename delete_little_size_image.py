import os
from PIL import Image

path = 'E:/temp/'

def delete_img_with_size(path, size):
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            filepath = os.path.join(dirpath, file)
            try:
                img = Image.open(filepath)
                if img.width < size or img.height < size:
                    print(img.size)
                    img.close()
                    os.remove(filepath)
            except:
                #open fail 文件可能不是图片，直接删除
                os.remove(filepath)
                print('remove ' + filepath)
                pass


delete_img_with_size(path, 300)