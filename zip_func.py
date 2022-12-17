import glob
import os
import zipfile

road = os.path.dirname(os.path.abspath(__file__))
resour = os.path.join(road, 'resources')
arch = os.path.join(resour, 'archive.zip')
list_dir = glob.glob(resour)

def create_arch():
    with zipfile.ZipFile(arch, mode='w', \
                         compression=zipfile.ZIP_DEFLATED) as zip_:
        for file in list_dir:
            add_file = os.path.join(resour, file)
            zip_.write(add_file)

def delete_arch():
    for file in list_dir:
        del_file = os.path.join(arch)
        os.remove(del_file)