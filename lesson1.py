import my_utils
import glob

srcPath = "D:\download\sd06\data\\"
dstPath = "D:\download\sd06\img\\"

rename_path = 'E:/temp/'

#path = "D:\download\googleDownload\motobike\\"
# my_utils.move_file(srcPath, dstPath)

my_utils.rename_file_list(rename_path, "sky_temp_", 0)
#my_utils.delete_img_with_size(rename_path, 300)
# print(glob.glob('D:\download\googleDownload\motobike\*.jpg'))

# my_utils.move_file_rename(srcPath, dstPath)

#    print(glob.glob('*.jpg'))


