# -*- coding: utf-8 -*-

import os
import os.path
import re
import shutil

def make_directory_as_needed(dir_path):
    if os.path.isdir(dir_path):
        return
    os.makedirs(dir_path)

def copy_file(from_dir, to_dir, ignore_extensions, node):
    if node[0:1] == '.':
        return
    root, ext = os.path.splitext(node)
    for ignore_ext in ignore_extensions:
        if ext == ignore_ext:
            return
    shutil.copy(from_dir+"\\"+node, to_dir+"\\"+node)

def copy_dir(from_dir, to_dir, ignore_extensions, ignore_directorys, node):
    if node[0:1] == '.':
        return
    for ignore_dir in ignore_directorys:
        if node == ignore_dir:
            return
    make_directory_as_needed(to_dir+"\\"+node)
    copy_all(from_dir+"\\"+node, to_dir+"\\"+node, ignore_extensions, ignore_directorys)

def copy_all(from_dir, to_dir, ignore_extensions, ignore_directorys):
    make_directory_as_needed(to_dir)
    for node in os.listdir(from_dir):
        if os.path.isfile(from_dir+"\\"+node):
            copy_file(from_dir, to_dir, ignore_extensions, node)
        if os.path.isdir(from_dir+"\\"+node):
            copy_dir(from_dir, to_dir, ignore_extensions, ignore_directorys, node)

if __name__ == "__main__":
    from_dir = r"C:\Users\yuni\projects\cpp\Fantomwaves"
    to_dir = r"C:\users\yuni\documents\damy2"
    ignore_extensions = [".bat", ".md", ".sdf", ".opensdf"]
    ignore_directorys = ["Debug", "Release"]
    copy_all(from_dir, to_dir, ignore_extensions, ignore_directorys)