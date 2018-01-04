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


def get_files_from_dir(folder):
    number_of_bytes_to_read = 4096
    dictionary_of_files = defaultdict(list)
    for dirs, subdirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(dirs, file)
            with open(file_path, 'rb') as checked_file:
                file_hash = hashlib.sha1(
                    checked_file.read(number_of_bytes_to_read)
                ).digest()
            dictionary_key = (file_hash, file)
            dictionary_of_files[dictionary_key].append(file_path)
    return dictionary_of_files


def get_duplicate_files(files):
    return {key: files[key] for key in files if len(files.get(key)) > 1}


def print_duplicates(duplicates):
    dividing_line = ('-' * 100)
    for (file_hash, file_name), file_paths in duplicates.items():
        print(dividing_line)
        print('File "{}" has duplicate:'.format(file_name))
        print('\n'.join(file_paths))


if __name__ == '__main__':
    args = parse_arg()
    folder_path = args.folder_path
    all_files_from_dir = get_files_from_dir(folder_path)
    duplicate_files = get_duplicate_files(all_files_from_dir)
    print_duplicates(duplicate_files)
