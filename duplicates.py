import os
import hashlib
import argparse
from collections import defaultdict


def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "folder_path",
        help="folder to find duplicates"
    )
    return parser.parse_args()


def get_duplicates(folder):
    dictionary_of_duplicate_files = defaultdict(list)
    for dirs, subdirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(dirs, file)
            with open(file_path, 'rb') as checked_file:
                file_hash = hashlib.sha1(checked_file.read()).digest()
            dictionary_key = (file_hash, file)
            dictionary_of_duplicate_files[dictionary_key].append(file_path)
    return dictionary_of_duplicate_files


def print_duplicates(duplicates):
    dividing_line = ('-' * 120)
    for key in duplicates:
        file_name = key[1]
        file_path = duplicates[key]
        number_of_paths = len(duplicates[key])
        if number_of_paths > 1:
            print(dividing_line)
            print('File "{}" has duplicate:'.format(file_name))
            print('\n'.join(file_path))


if __name__ == '__main__':
    args = parse_arg()
    folder_path = args.folder_path
    list_of_duplicates = get_duplicates(folder_path)
    print_duplicates(list_of_duplicates)
