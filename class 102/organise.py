import os
import shutil

from_dir = "/Users/admin/Downloads/Assets"
to_dir = '/Users/admin/Downloads/Imagedownload'
list_off_files = os.listdir(from_dir)
print(list_off_files)
for filename in list_off_files:
    name,extension = os.path.splitext(filename)
    print(name)
    print(extension)

    if extension == '':
        continue
    if extension in ['.gif','png','.jpg','.jpeg','.jfif']:
        path1 = from_dir+'/'+filename
        path2 = to_dir+'/'+"image_files"
        path3 = to_dir+'/'+"image_files"+'/'+filename
        if os.path.exists(path2):
            print("Moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Movie")
            shutil.move(path1,path3)