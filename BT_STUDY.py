import hashlib
from ecdsa import SECP256k1, SigningKey
import random
import sys
import time
from os import system, name 
from time import sleep 
import urllib.request

  
INDIRIZZO_NUM = 0
INDIRIZZO_HEX = 0x0
INDIRIZZO_STR = ""
LUNGH_STRINGA = 0
STRINGA2 = ""
FINALE = ""
decode = ""
ask = "y"

BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


        
def base58_encode(version, public_address):

    version = bytes.fromhex(version)
    checksum = hashlib.sha256(hashlib.sha256(version + public_address).digest()).digest()[:4]
    payload = version + public_address + checksum
    
    result = int.from_bytes(payload, byteorder="big")

    padding = len(payload) - len(payload.lstrip(b'\0'))
    encoded = []

    while result != 0:
        result, remainder = divmod(result, 58)
        encoded.append(BASE58_ALPHABET[remainder])

    return padding*"1" + "".join(encoded)[::-1]


def get_private_key(hex_string):
    return bytes.fromhex(hex_string.zfill(64))


def get_public_key(private_key):
    return (bytes.fromhex("04") + SigningKey.from_string(private_key, curve=SECP256k1).verifying_key.to_string())


def get_public_address(public_key):
    address = hashlib.sha256(public_key).digest()
    h = hashlib.new('ripemd160')
    h.update(address)
    address = h.digest()
    return address

def generate_adresses_bin(n):
    addresses = list()
    print ("-- GENERATING PRIVATE KEY (BIN) 256 BIT --")
    sleep(2) 
    for i in range(n):
        n = 256
        alphabet = "01"
        s = ""
        clear()
        for i in range(n):
            clear()
            s += random.choice(alphabet)
            print ("-- GENERATING PRIVATE KEY (BIN) 256 BIT --")
            print("")
            print (s)
            sleep(0.05) 
        binario = int(s, base=2) 
        binario2 = hex(binario) 
#        print (binario2)
        esad = str(binario2[2:])
        s = esad
        print ("")
        print ("PRIVATE KEY (HEX)")
        print ("")
        print (s)
        try:
            print("")
            private_key = get_private_key(s)
#            print("PRIVATE KEY (HEX): = " + private_key.hex())
#            print ("")

            print ("-- GENERATING PUBLIC KEY (HEX) --")
            sleep(2) 
            print ("")
            public_key = get_public_key(private_key)
            print(public_key.hex())
            print ("")

            print ("-- GENERATING PUBLIC ADDRESS (HEX) --")
            sleep(2) 
            print ("")
            public_address = get_public_address(public_key)
            print(public_address.hex())

            print ("")
            print ("-- GENERATING BITCOIN ADDRESS (BASE58 starts with 1) --")
            sleep(2) 
            print ("")

            bitcoin_address = base58_encode("00", public_address)
            print(bitcoin_address)
            chiave = base58_encode("80", private_key)  # vedi https://en.bitcoin.it/wiki/List_of_address_prefixes
            print ("")

            print ("-- GENERATING BITCOIN PRIVATE KEY (BASE58 starts with 5) --")
            sleep(2) 
            print ("")
            print(chiave)
            addresses.append([bitcoin_address, public_key, private_key, chiave])
            

        except KeyboardInterrupt:
            print("Bye")
            sys.exit()
        except:
            print("Failed to create address " + s)
#    bitcoin_address="18XrReT5ChW8qgXecNgKTU5T6MrMMLnV8H"
    contents = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + bitcoin_address).read()
    print("")
    print("BITCOIN IN ADDRESS: = " + str(contents.decode('UTF8')))
    return addresses
    
def generate_adresses_hex(n):
    addresses = list()
    print ("-- GENERATING PRIVATE KEY (HEX) 64 CHAR --")
    sleep(2) 
    for i in range(n):
        n = 64
        alphabet = "0123456789ABCDEF"
        s = ""
        clear()
        for i in range(n):
            clear()
            s += random.choice(alphabet)
            print ("-- GENERATING PRIVATE KEY (HEX) 64 CHAR --")
            print("")
            print (s)
            sleep(0.05) 

        try:
            print("")
            private_key = get_private_key(s)
#            print("PRIVATE KEY (HEX): = " + private_key.hex())
#            print ("")

            print ("-- GENERATING PUBLIC KEY (HEX) --")
            sleep(2) 
            print ("")
            public_key = get_public_key(private_key)
            print(public_key.hex())
            print ("")

            print ("-- GENERATING PUBLIC ADDRESS (HEX) --")
            sleep(2) 
            print ("")
            public_address = get_public_address(public_key)
            print(public_address.hex())

            print ("")
            print ("-- GENERATING BITCOIN ADDRESS (BASE58 starts with 1) --")
            sleep(2) 
            print ("")

            bitcoin_address = base58_encode("00", public_address)
            print(bitcoin_address)
            chiave = base58_encode("80", private_key)  # vedi https://en.bitcoin.it/wiki/List_of_address_prefixes
            print ("")

            print ("-- GENERATING BITCOIN PRIVATE KEY (BASE58 starts with 5) --")
            sleep(2) 
            print ("")
            print(chiave)
            addresses.append([bitcoin_address, public_key, private_key, chiave])
            

        except KeyboardInterrupt:
            print("Bye")
            sys.exit()
        except:
            print("Failed to create address " + s)
#    bitcoin_address="18XrReT5ChW8qgXecNgKTU5T6MrMMLnV8H"
    contents = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + bitcoin_address).read()
    print("")
    print("BITCOIN IN ADDRESS: = " + str(contents.decode('UTF8')))
    return addresses

while ask != "n" and ask!= "N":
    clear()
    tipo_generazione = input('PRESS 1 FOR BINARY OR 2 FOR EXADECIMAL ')
#    print (tipo_generazione)
#    sleep(5)
    if tipo_generazione == "1":
        clear()
        generate_adresses_bin(1)
    else:
        clear()
        generate_adresses_hex(1)
    ask = input('Continue? Y/N ')

