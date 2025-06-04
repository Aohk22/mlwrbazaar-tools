# mlwrbazaar-tools
Some tools to interact with Malware Bazaar API.

## Setup

`$ git clone <this_repo>`.  
Create `.env` file inside the same directory that was cloned.  
Add your API keys `<name>=<api_key>`.  
Install python-dotenv:  
```shell
# use pipx or create virtual environment if needed
$ pip install python-dotenv
```

## Usage

mlwrbazaar-query.py only returns SH256 hashes, the output is written to chosen file (hashes are separated by `\n`).  
```bash
$ ./mlwrbazaar-query.py -h
usage: mlwrbazaar-query.py [-h] -t TAG -o OUTPUT [-l LIMIT]

Query malware samples by tag and returns SHA256 hash.

optional arguments:
  -h, --help            show this help message and exit
  -t TAG, --tag TAG     Tag you want to get malware samples for
  -o OUTPUT, --output OUTPUT
                        Hash file name
  -l LIMIT, --limit LIMIT
                        Max number of results to display
```

mlwrbazaar-download.py can either download using SHA256 hash as query or bulk download from file containing SHA256 hashes.  
*Note*: downloaded files are zip files encrypted with password "infected".  
```bash
$ ./mlwrbazaar-download.py -h
usage: mlwrbazaar-download.py [-h] (--hash HASH | --file FILE) [-i]

Download malware sample from Malware Bazaar.

optional arguments:
  -h, --help   show this help message and exit
  --hash HASH  SHA256 hash of file
  --file FILE  File containing SHA256 hashes
  -i, --info   Get file info from hash only
```

## Example

Get samples with the tag 'redline':  
```bash
$ ./mlwrbazaar-query.py -t redline -l 4 -o redlinehashes.txt
Query response is  written to mb-response.json
989db46562126cd83b6148da103cb17d770ed14c5a09b899bd225e77ff1b054d
0379d402a94f960380d7d91e3bfa106eeac01cd39ae7b0ba5010ba737088a215
0e9ebbf4391a1ce11ceecab0c0699a229a7f2a20b9909600310db15b1b3cf772
22c5a786602a46b23ff82c4165daf2eb777357c49434f9997c74eae4bed52c5b
Hashes are written to file redlinehashes.txt
```

Download the samples using hashes from output file:  
```bash
$ ./mlwrbazaar-download.py --file redlinehashes.txt 
File written to ./989db46562126cd83b6148da103cb17d770ed14c5a09b899bd225e77ff1b054d.zip
File written to ./0379d402a94f960380d7d91e3bfa106eeac01cd39ae7b0ba5010ba737088a215.zip
File written to ./0e9ebbf4391a1ce11ceecab0c0699a229a7f2a20b9909600310db15b1b3cf772.zip
File written to ./22c5a786602a46b23ff82c4165daf2eb777357c49434f9997c74eae4bed52c5b.zip
$ ll *.zip
-rw-rw-r-- 1 remnux remnux 40 Jun  4 07:44 0379d402a94f960380d7d91e3bfa106eeac01cd39ae7b0ba5010ba737088a215.zip
-rw-rw-r-- 1 remnux remnux 40 Jun  4 07:44 0e9ebbf4391a1ce11ceecab0c0699a229a7f2a20b9909600310db15b1b3cf772.zip
-rw-rw-r-- 1 remnux remnux 40 Jun  4 07:44 22c5a786602a46b23ff82c4165daf2eb777357c49434f9997c74eae4bed52c5b.zip
-rw-rw-r-- 1 remnux remnux 40 Jun  4 07:44 989db46562126cd83b6148da103cb17d770ed14c5a09b899bd225e77ff1b054d.zip
```

Verifying that the download is actually correct (run hash on extracted file):  
```bash
$ sha256sum 0379d402a94f960380d7d91e3bfa106eeac01cd39ae7b0ba5010ba737088a215.exe 
0379d402a94f960380d7d91e3bfa106eeac01cd39ae7b0ba5010ba737088a215  0379d402a94f960380d7d91e3bfa106eeac01cd39ae7b0ba5010ba737088a215.exe
```
