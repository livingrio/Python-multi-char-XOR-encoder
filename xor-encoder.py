#!/bin/env python3                                                                                                                                            
                                                                                                                                                              
import argparse                                                                                                                                               
import os


def xor(data, key_byte):
    return bytearray([a ^ key_byte for a in data])


def encrypt_file(source, dest, xor_key):
    with open(source, 'rb') as in_file:
        data = in_file.read()

    data_enc = xor(data, xor_key)

    with open(dest, 'wb') as out_file:
        out_file.write(data_enc)


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='append_file.py',
        description='XOR encrypt the contents of a file using a dynamic XOR key.'
    )
    parser.add_argument('-i', '--input', required=True, help='File with contents to XOR encrypt.')
    parser.add_argument('-o', '--output', required=True, help='File to place encrypted contents.')
    parser.add_argument('-k', '--key', required=True, type=str, help='XOR key in hexadecimal format (e.g., 0xFA).')
    return parser.parse_args()


def main():
    args = parse_arguments()

    # Convert the key to an integer, supporting both "0xFA" and "FA" format
    try:
        xor_key = int(args.key, 16)  # Interpret the key as a hexadecimal integer
    except ValueError:
        print(f'[-] Invalid key format: {args.key}. Please provide a valid hexadecimal key.')
        os.exit(1)

    print(f'[+] XOR encrypting {args.input} into {args.output} using key {hex(xor_key)}')
    try:
        encrypt_file(args.input, args.output, xor_key)
    except Exception as e:
        print(f'[-] Encryption failed: {e}')
        return
    print('[+] Encryption completed successfully')


if __name__ == '__main__':
    main()
