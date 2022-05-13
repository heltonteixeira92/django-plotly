import hashlib
import random
import string


def generate_hash():
    hash_str = ''.join(random.choices(string.ascii_letters, k=6))
    return hashlib.sha1(hash_str.encode()).hexdigest()
