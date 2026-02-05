import struct
import binascii

def read_bytes(data, index, length):
    return data[index:index+length], index+length

def little_endian_to_int(b):
    return int.from_bytes(b, 'little')

def decode_varint(data, index):
    prefix = data[index]
    if prefix < 0xfd:
        return prefix, index + 1
    elif prefix == 0xfd:
        return little_endian_to_int(data[index+1:index+3]), index + 3
    elif prefix == 0xfe:
        return little_endian_to_int(data[index+1:index+5]), index + 5
    else:
        return little_endian_to_int(data[index+1:index+9]), index + 9

def decode_transaction(raw_tx):
    tx = bytes.fromhex(raw_tx)
    index = 0

    version_bytes, index = read_bytes(tx, index, 4)
    version = little_endian_to_int(version_bytes)

    print("Transaction Version:", version)


raw_tx = "0100000001"
decode_transaction(raw_tx)
