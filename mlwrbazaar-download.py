#!/usr/bin/env python3
import requests
import os
import argparse
import time
from dotenv import load_dotenv


def parse_arguments():
    parser = argparse.ArgumentParser(description='Download malware sample from Malware Bazaar.')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--hash', help='SHA256 hash of file')
    group.add_argument('--file', help='File containing SHA256 hashes')

    parser.add_argument('-i', '--info', action='store_true', help='Get file info from hash only')
    return parser.parse_args()


def download_from_hash(url: str, headers: dict, data: dict, h: str):
    res = requests.post(url, data=data, timeout=15, headers=headers)
    raw_data = res.content
    with open(f'{h}.zip', 'wb') as zipfile:
        zipfile.write(raw_data)
        print(f'File written to ./{h}.zip')


def download_from_file(fn: str, url: str, headers: dict, data: dict):
    hashes = open(fn, 'r').readlines()
    for h in hashes:
        h = h.strip()
        if not h:
            continue
        download_from_hash(url, headers, data, h)
        time.sleep(3)


def main():
    args = parse_arguments()

    if not load_dotenv():
        print('Could not load environment variables, exiting.')
        exit(1)

    url = 'https://mb-api.abuse.ch/api/v1/'
    headers = { 'API-KEY': os.environ.get('MALWARE_BAZAAR_API') }
    data = { 'query': 'get_file' }

    if args.hash:
        download_from_hash(url, headers, data, args.hash)
    elif args.file:
        download_from_file(args.file, url, headers, data)

    if args.info:
        data['query'] = 'get_info'
        data['hash'] = args.hash
        res = requests.post(url, data=data, timeout=15, headers=headers)
        print(res.text)


if __name__ == '__main__':
    main()
