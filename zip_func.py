import os
import zipfile
from os.path import basename


def create_arch(path_files, path_archive):
    list_dir = os.listdir(path_files)
    with zipfile.ZipFile(path_archive, mode='w', compression=zipfile.ZIP_DEFLATED) as zip_:
        for file in list_dir:
            add_file = os.path.join(path_files, file)
            zip_.write(add_file, basename(add_file))


def delete_arch(path_archive):
    del_file = os.path.join(path_archive)
    os.remove(del_file)
