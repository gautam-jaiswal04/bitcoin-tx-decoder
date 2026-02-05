import struct
import binascii

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

def decode_transaction(raw_hex):
    data = bytes.fromhex(raw_hex)
    index = 0

    version = little_endian_to_int(data[index:index+4])
    index += 4
    print("Transaction Version:", version)

    input_count, index = decode_varint(data, index)
    print("Number of Inputs:", input_count)

    for i in range(input_count):
        print(f"\nInput {i+1}")

        prev_txid = data[index:index+32][::-1].hex()
        index += 32
        print("Previous TXID:", prev_txid)

        vout = little_endian_to_int(data[index:index+4])
        index += 4
        print("Output Index:", vout)

        script_length, index = decode_varint(data, index)
        index += script_length
        print("ScriptSig Length:", script_length)

        sequence = data[index:index+4].hex()
        index += 4
        print("Sequence:", sequence)

    output_count, index = decode_varint(data, index)
    print("\nNumber of Outputs:", output_count)

    for i in range(output_count):
        print(f"\nOutput {i+1}")

        amount = little_endian_to_int(data[index:index+8])
        index += 8
        print("Amount (satoshis):", amount)
        print("Amount (BTC):", amount / 100000000)

        script_length, index = decode_varint(data, index)
        print("ScriptPubKey Length:", script_length)

        script_pubkey = data[index:index+script_length].hex()
        index += script_length
        print("ScriptPubKey:", script_pubkey)

    locktime = little_endian_to_int(data[index:index+4])
    print("\nLocktime:", locktime)

raw_tx = "0100000001813f79011acb80925dfe69b3def355fe914bd1d96a3f5f71bf8303c6a989c7d5000000006b483045022100f3581e1972ae8ac7c7367a7a253bc1135223adb9a468bb3a59233f45bc57838022059af01ca17d00e41837a1d58f8f08f6b14b14d3b6b06c7a7b57c0a7a0b4c012102b46342b1a1fdd8db1d6b4fdf7e6e6b7965a7ab6b5234f6b31d9114ef95b1ffffffff"

decode_transaction(raw_tx)
