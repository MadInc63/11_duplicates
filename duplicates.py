import os
import hashlib
import argparse
from collections import namedtuple


def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "folder_path",
        help="folder to find duplicates"
    )
    return parser.parse_args()


def get_duplicates_dictionary(folder):
    dictionary_of_duplicate_files = namedtuple(list)
    for dirs, subdirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(dirs, file)
            with open(file_path, 'rb') as checked_file:
                file_hash = hashlib.sha1(checked_file.read()).digest()
            dictionary_key = (file_hash, file)
            dictionary_of_duplicate_files[dictionary_key].append(file_path)
    return dictionary_of_duplicate_files


def print_duplicates(dictionary):
    print(dictionary)
    for hash, file in dictionary:
        print ((hash, file))


if __name__ == '__main__':
    args = parse_arg()
    folder_path = args.folder_path
    duplicates_dictionary = get_duplicates_dictionary(folder_path)
    print_duplicates(duplicates_dictionary)
