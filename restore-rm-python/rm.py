#!/usr/bin/env python3
import os
import shutil
import sys

def move_to_trash(file_path):
    trash_dir = os.path.expanduser("~/rm_trash")
    if not os.path.exists(trash_dir):
        os.makedirs(trash_dir)

    file_name = os.path.basename(file_path)
    file_base, file_ext = os.path.splitext(file_name)

 
    new_file_path = os.path.join(trash_dir, file_name)
    count = 1
    while os.path.exists(new_file_path):
        new_file_base = "{}-{}".format(file_base, count) if count > 1 else file_base
        new_file_name = "{}{}".format(new_file_base, file_ext)
        new_file_path = os.path.join(trash_dir, new_file_name)
        count += 1


    shutil.move(file_path, new_file_path)

def rm(paths):
    for path in paths:
        if os.path.isdir(path):
            if '-r' in sys.argv:
                move_to_trash(path)
            else:
                sys.stderr.write("rm.py: cannot remove '{}': Is a directory\n".format(path))
        elif os.path.exists(path):
            move_to_trash(path)
        else:
            sys.stderr.write("rm.py: cannot remove '{}': No such file or directory\n".format(path))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: python3 rm.py [-r] file1 file2 ...\n")
        sys.exit(1)
    rm(sys.argv[1:])
