import hashlib
from urllib.request import urlopen
import os
import time


class KeyGeneration:
    def __init__(self):
        self.user_path = os.path.expanduser('~/')
        self.keys_path = os.path.join(self.user_path, ".bostadssokare/")
        isDir = os.path.isdir(self.keys_path)
        if not isDir:
            os.mkdir(self.keys_path)

    def read_key(self):
        """
        This function opens an existing text file and
        reads the existing key and return that key.
        input:
            nothing
        output:
            hash_key        - string with key
        """

        with open(f'{self.keys_path}hash_key.txt', 'r') as f:
            hash_key = f.readline()
        return hash_key

    def create_md5(self, key):
        """
        This function will create a text file containing
        a new hash key in a text file.
        input:
            key             - string , hash key
        output:
            hash_key.txt    - txt file
        """
        with open(f'{self.keys_path}hash_key.txt', 'w') as f:
            f.write(key)
        print("im here")

    def check_md5(self, url):
        """
        This function will check if the existing
        hash key is the same as the same.
        input:
            url             - string website address
        output:
            none
        """
        if os.path.isfile(f'{self.keys_path}hash_key.txt'):
            existing_keys = self.read_key()

            pages = urlopen(url).read()
            hash_md5 = hashlib.sha224(pages).hexdigest()
            if existing_keys != hash_md5:
                self.create_md5(hash_md5)
