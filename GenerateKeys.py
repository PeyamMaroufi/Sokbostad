import hashlib
import requests


class KeyGeneration:
    def __init__(self):
        pass

    def read_key(self):
        """
        This function opens an existing text file and
        reads the existing key and return that key.
        input:
            nothing
        output:
            hash_key        - string with key
        """

        with open('hash_key.txt', 'r') as f:
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
        with open('hash_key.txt', 'w') as f:
            f.write(key)

    def check_md5(self, url):
        """
        This function will check if the existing
        hash key is the same as the same.
        input:
            url             - string website adress
        output:
            none
        """
        walin_page = requests.get(url)
        hash_md5 = hashlib.sha256(walin_page.text.encode('utf-8')).hexdigest()
        if not (hash_md5 == keys.read_key()):
            self.create_md5(hash_md5)
