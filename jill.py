import argparse
import hashlib
# Parses through argument
parser = argparse.ArgumentParser()
# Goes through password file
parser.add_argument('pswdfile')
# Goes through word list
parser.add_argument('dict')
# Gives args a parser argument
args = parser.parse_args()
# Opens password file in read mode
pswds = open(args.pswdfile, "r")
# Opens word list in read mode
word_list = open(args.dict, "r")
# Reads through password file 
pswd_split = passwords.readlines()
# Reads through word list
word_split = dictionary_file.readlines()
# Creates for loop
for hash in pswd_split:
    # Splits the : from the username and password
    hash = hash.split(":")
    # Creates for loop
    for pw in word_split:
    # If the password is sha256 it strips all the white spaces and then encodes the string into a hexadecimal and then compares it
        if hashlib.sha256(pw.strip().encode()).hexdigest() == hash[1].strip():
            #Prints the result if it matches the password
            print(f'{hash[0]}:{pw.strip()}')