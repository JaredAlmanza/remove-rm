#!/usr/bin/env python3

import os
import sys
import shutil

def restore(file_name):
    trash_dir = os.path.expanduser("~/rm_trash")

    matching_files = [f for f in os.listdir(trash_dir) if f.startswith(file_name)]
    if not matching_files:
        print("No matching files found in trash for '{}'".format(file_name))
        return


    matching_files.sort(reverse=True)
    most_recent_file = matching_files[0]

    
    src_path = os.path.join(trash_dir, most_recent_file)
    dst_path = os.path.join(os.getcwd(), most_recent_file)
    shutil.move(src_path, dst_path)
    print("Restored '{}' to '{}'".format(most_recent_file, os.getcwd()))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python3 restore.py file_name\n")
        sys.exit(1)
    restore(sys.argv[1])
