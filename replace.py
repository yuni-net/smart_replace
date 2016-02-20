# -*- coding: utf-8 -*-

import os
import os.path
import re
import shutil

f = open("log.txt", "w")
f.close()
f = open("log.txt", "a")

def get_related(root, from_dir):
    return root[len(from_dir):]

def make_directory_as_needed(dir_path):
    if os.path.isdir(dir_path):
        return
    os.makedirs(dir_path)

def is_match(full_path, error_list):
    for error in error_list:
        if re.search(error, full_path):
            return True
    return False

def copy_forced(from_path, to_path):
    f.write("    in function copy_forced\n")
    f.write("        to_path: " + to_path + "\n")
    dirname = os.path.dirname(to_path)
    f.write("        dirname: " + dirname + "\n")
    make_directory_as_needed(dirname)
    shutil.copy(from_path, to_path)

def copy(from_dir, to_dir, error_list):
    f.write("in function copy\n")
    for (root, dirs, files) in os.walk(from_dir):
        f.write("    for (root, dirs, files) in os.walk(from_dir)\n")
        f.write("    root: "+root+"\n")
        to_root = to_dir + get_related(root, from_dir)
        f.write("    to_root: " + to_root + "\n")
        for file in files:
            if file[0:1] == '.':
                continue
            full_path = root + "\\" + file
            f.write("    full_path: "+full_path+"\n")
            if is_match(full_path, error_list):
                continue
            copy_forced(full_path, to_root + "\\" + file)

if __name__ == "__main__":
    from_dir = r"C:\Users\yuni\projects\cpp\Fantomwaves"
    to_dir = r"C:\users\yuni\documents\damy2"
    error_list = []
    copy(from_dir, to_dir, error_list)