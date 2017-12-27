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


def list_of_duplicate(folder):
    list_of_files = {}
    for dirs, subdirs, files in os.walk(folder):
        for name in files:
            file_path = os.path.join(dirs, name)
            with open(file_path, 'rb') as checked_file:
                file_hash = hashlib.sha1(checked_file.read()).digest()
            add_duplicate_to_list = list_of_files.get(file_hash)
            if add_duplicate_to_list:
                try:
                    list_of_files[file_hash][name].append(file_path)
                except KeyError:
                    list_of_files[file_hash][name] = [file_path]
            else:
                list_of_files[file_hash] = {name: [file_path]}
    return list_of_files


def print_duplicates(duplicates_dictionary):
    for index in duplicates_dictionary:
        for file in duplicates_dictionary[index]:
            if len(duplicates_dictionary[index][file]) > 1:
                print(
                    'Duplicate files: {}'.
                    format(', '.join(duplicates_dictionary[index][file]))
                )


if __name__ == '__main__':
    args = parse_arg()
    folder_path = args.folder_path
    dictionary_of_duplicates = list_of_duplicate(folder_path)
    print_duplicates(dictionary_of_duplicates)
