#!/usr/bin/env python3
import requests
import os
import argparse
import json
from dotenv import load_dotenv


def parse_hash(response: str, fn: str):
    json_string = ''

    with open(response, 'r') as file:
        json_string = file.read()

    data = json.loads(json_string)
    samples = data['data']
    with open(fn, 'w') as file:
        for sample in samples:
            sha256hash = sample['sha256_hash']
            print(sha256hash)
            file.write(f'{sha256hash}\n')
    print(f'Hashes are written to file {fn}')


def parse_arguments():
    parser = argparse.ArgumentParser(description='Query malware samples by tag and returns SHA256 hash.')
    parser.add_argument('-t', '--tag', help='Tag you want to get malware samples for', required=True)
    parser.add_argument('-o', '--output', help='Hash file name', required=True)
    parser.add_argument('-l', '--limit', help='Max number of results to display')
    return parser.parse_args()


def main():
    args = parse_arguments()
    
    if not load_dotenv():
        print('Could not load environment variables, exiting.')
        exit(1)

    api_key = os.environ.get('MALWARE_BAZAAR_API')
    api_url = 'https://mb-api.abuse.ch/api/v1/'

    headers = { 'API-KEY': api_key }
    data = { 'query': 'get_taginfo', 'tag': args.tag }
    if args.limit:
        data['limit'] = args.limit

    res = requests.post(api_url, data=data, headers=headers)
 
    response_output = 'mb-response.json'
    with open(response_output, 'w') as file:
        file.write(res.text)
        print(f'Query response is  written to {response_output}')

    parse_hash(response_output, args.output)

if __name__ == '__main__':
    main()
