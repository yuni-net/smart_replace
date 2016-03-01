# -*- coding: utf-8 -*-

import os
import os.path
import re
import shutil

f = open("log.txt", "w")
f.close()
f = open("log.txt", "a")

def make_directory_as_needed(dir_path):
    if os.path.isdir(dir_path):
        return
    os.makedirs(dir_path)

def copy_file(from_dir, to_dir, ignore_extensions, node):
    f.write("    node[0:1]: " + node[0:1] + "\n")
    if node[0:1] == '.':
        return
    else:
        f.write("    let's split text")
    root, ext = os.path.splitext(node)
    f.write("    ext: " + ext + "\n")
    for ignore_ext in ignore_extensions:
        if ext == ignore_ext:
            f.write("    ext==ignore_ext:[ext: "+ext+", ignore_ext: "+ignore_ext+"]\n")
            return
    f.write("    from: " + from_dir+"\\"+node + ", to: " + to_dir+"\\"+node)
    shutil.copy(from_dir+"\\"+node, to_dir+"\\"+node)

def copy_dir(from_dir, to_dir, ignore_extensions, ignore_directorys, node):
    f.write("    node[0:1]: " + node[0:1] + "\n")
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
        f.write("node: " + node + "\n")
        if os.path.isfile(from_dir+"\\"+node):
            copy_file(from_dir, to_dir, ignore_extensions, node)
        if os.path.isdir(from_dir+"\\"+node):
            copy_dir(from_dir, to_dir, ignore_extensions, ignore_directorys, node)

if __name__ == "__main__":
    from_dir = r"C:\Users\yuni\projects\cpp\Fantomwaves"
    to_dir = r"C:\users\yuni\documents\damy2"
    ignore_extensions = [".bat", ".md", ".sdf"]
    ignore_directorys = ["Debug", "Release"]
    copy_all(from_dir, to_dir, ignore_extensions, ignore_directorys)