import os
import hashlib
import argparse


def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "folder_path",
        help="folder to find duplicates"
    )
    return parser.parse_args()


def get_duplicates(folder):
    dictionary_of_files = {}
    for dirs, subdirs, file in os.walk(folder):
        for name in file:
            file_path = os.path.join(dirs, name)
            with open(file_path, 'rb') as checked_file:
                file_hash = hashlib.sha1(checked_file.read()).digest()
            add_to_dict = dictionary_of_files.get((file_hash, name))
            if add_to_dict:
                try:
                    dictionary_of_files[(file_hash, name)].append(file_path)
                except KeyError:
                    dictionary_of_files[(file_hash, name)] = [file_path]
            else:
                dictionary_of_files[(file_hash, name)] = [file_path]
    return dictionary_of_files


def print_duplicates(duplicates_dictionary):
    for index in duplicates_dictionary:
        if len(duplicates_dictionary[index]) > 1:
            print('-----------------------------------------------------------'
                  '-----------------------------------------------------------'
                  '-------------------------------------')
            print(
                ' File:      {}'.
                format('\n duplicate: '.join(duplicates_dictionary[index]))
            )


if __name__ == '__main__':
    args = parse_arg()
    folder_path = args.folder_path
    dictionary_of_duplicates = get_duplicates(folder_path)
    print_duplicates(dictionary_of_duplicates)
