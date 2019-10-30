"""
Script to find groups of duplicated files. Given one or more directories as
input, recursively traverses those directories and hashes the files (SHA256).
Files with identical hashes are grouped and reported at the end.
"""
import hashlib
import sys
import os
import itertools
import collections

def hash_file(path):
    hash_builder = hashlib.sha256()
    with open(path, 'rb') as f:
        while True:
            data = f.read(20 * 4096) # Arbitrary buffer size.
            if not data:
                break
            hash_builder.update(data)
    return hash_builder.hexdigest()

def list_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield from [os.path.join(root, file) for file in files]

def group_duplicates(values, key_fn):
    duplicates_by_key = collections.defaultdict(list)
    for value in values:
        duplicates_by_key[key_fn(value)].append(value)
    return [(key, group) for key, group in duplicates_by_key.items() if len(group) > 1]

if __name__ == '__main__':
    directories = sys.argv[1:] or [input('Enter path of directory to be analyzed: ')]
    all_files = [path for directory in directories for path in list_all_files(directory)]
    print(f'Found {len(all_files)} files. Computing hashes and duplicates...')
    for hash, duplicate_group in group_duplicates(all_files, hash_file):
        print(f'\nFound group of {len(duplicate_group)} duplicate files (hash {hash}):')
        for path in duplicate_group:
            print('\t', path)