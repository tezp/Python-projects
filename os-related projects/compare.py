#! /usr/bin/python3
""" This script is used to find duplicate files in folder provided by user."""
__author__ = '__tp__'

import os
import sys
import hashlib
import argparse

parser = argparse.ArgumentParser(description="Find duplicate files in given folder !!!")
parser.add_argument('-p', '--path', help='Path of folder', required=True)
result = parser.parse_args()


def main():
    list_of_files = []
    try:
        if len(sys.argv) != 3:
            print(result)
            sys.exit(1)
        mainPath = str(sys.argv[2])
        if not mainPath.endswith('/'):
            mainPath+"/"
        for (dirPath, dirName, fileNames) in (os.walk(mainPath)):
            for file in fileNames:
                # Get absolute path of file
                full_path = os.path.join(dirPath, file)

                # Get hash value of a file
                hash_value = md5_for_file(full_path)
                print("I saw : ", full_path)

                # Create list of file and hash value.
                list_of_files.append([full_path, hash_value])

        # If you want to see the pair of file name and its hash value then uncomment following
        # print("List", *list_of_files, sep="\n")
        compair(list_of_files)
    except Exception as e:
        print(str(e))


# This is main function which compares the files and finds similar files.
def compair(list_of_files):
    new_list = []
    set_to_check = set()
    list_of_files.sort()
    new_pre_list = []

    # Take one by one files.
    for file in list_of_files:

        # check if the file is in set() as Sets can't contain duplicates
        if (file[1] not in set_to_check):
            set_to_check.add((file[1]))
            new_pre_list.append(file)
        else:
            new_list.append(file)

    """
    Now we have collected original file list - new_pre_list[] and new file list - new_list[] which contains duplicate files only. 
    """
    # print('All : ', *new_pre_list, sep="\n")
    # print('New : ', *new_list, sep="\n")

    print("\nHey TP ... I got following duplicate files\n")
    # Take one file from original file list without duplicate contains.
    for file1 in new_pre_list:
        # Take one file from new_list which contains duplicate files only
        for file2 in new_list:
            if file1[1] == file2[1]:
                print("File 1 : ", file1[0])
                print("File 2 : ", file2[0])
                print()


# This function becomes slower for big files.
#
# def get_hash_value(file_name):
#     with open(file_name, 'rb') as file:
#         byte_file = file.read()
#         readable_hash = hashlib.sha1(byte_file).hexdigest()
#         return (readable_hash)

# gets md5 hash value and this function works faster as its block size is larger.
def md5_for_file(f, block_size=2 ** 20):
    md5 = hashlib.md5()
    with open(f, 'rb') as file:
        while True:
            data = file.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5.digest()


main()
