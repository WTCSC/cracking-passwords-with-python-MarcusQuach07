import argparse
import hashlib
# Create a empty list called encrypted to put encrypted passwords into
encrypted = []
# Create a empty list called names to put names into
names = []
# Empty list to 
output = []

def parse_folder():

    parser = argparse.ArgumentParser()

    parser.add_argument("password_file")

    parser.add_argument("word_list")

    args = parser.parse_args()

def opening():

    with open(args.password_file) as f

    freading = f.read()
    
def loading():

    for encrypted in list:

        names.append(encrypted.split(":")[0])

        try:
            encrypted.append(hash.split)