# mlwrbazaar-tools
Some tools to interact with Malware Bazaar API.

## Setup

`git clone <this_repo>`.  
Create `.env` file inside the same directory that was cloned.  
Add your API keys `<name>=<api_key>`.  
Install python-dotenv:  
```shell
# use pipx or create virtual environment if needed
pip install python-dotenv
```

## Usage

mlwrbazaar-query.py only returns SH256 hashes, the output is written to chosen file (separated by `\n`).  
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
