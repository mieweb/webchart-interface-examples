# Introduction

The document upload example code requires Python 3.6.8+ to run.

Given a [CSV file](sample_data.csv) with the names of documents to upload, this program will parse each row, read in the file from disk, and upload the document to the chart specified by the patient_id column in the CSV.

# Setup

```
# Create a virtualenv for imported 3rd party library (requests)
$ /usr/bin/python -m venv my_venv

# Activate virtualenv
$ source my_venv/bin/activate

# Bash shell indicates active virtualenv
# Type 'deactivate' when done
(my_venv) $

# Install requests and python-magic
(my_venv) $ pip install requests python-magic
Collecting requests
  Using cached https://files.pythonhosted.org/packages/2d/61/08076519c80041bc0ffa1a8af0cbd3bf3e2b62af10435d269a9d0f40564d/requests-2.27.1-py2.py3-none-any.whl
Collecting python-magic
  Using cached https://files.pythonhosted.org/packages/6c/73/9f872cb81fc5c3bb48f7227872c28975f998f3e7c2b1c16e95e6432bbb90/python_magic-0.4.27-py2.py3-none-any.whl
Collecting charset-normalizer~=2.0.0; python_version >= "3" (from requests)
  Using cached https://files.pythonhosted.org/packages/06/b3/24afc8868eba069a7f03650ac750a778862dc34941a4bebeb58706715726/charset_normalizer-2.0.12-py3-none-any.whl
Collecting idna<4,>=2.5; python_version >= "3" (from requests)
  Using cached https://files.pythonhosted.org/packages/fc/34/3030de6f1370931b9dbb4dad48f6ab1015ab1d32447850b9fc94e60097be/idna-3.4-py3-none-any.whl
Collecting urllib3<1.27,>=1.21.1 (from requests)
  Using cached https://files.pythonhosted.org/packages/fe/ca/466766e20b767ddb9b951202542310cba37ea5f2d792dae7589f1741af58/urllib3-1.26.14-py2.py3-none-any.whl
Collecting certifi>=2017.4.17 (from requests)
  Using cached https://files.pythonhosted.org/packages/71/4c/3db2b8021bd6f2f0ceb0e088d6b2d49147671f25832fb17970e9b583d742/certifi-2022.12.7-py3-none-any.whl
Installing collected packages: charset-normalizer, idna, urllib3, certifi, requests, python-magic
Successfully installed certifi-2022.12.7 charset-normalizer-2.0.12 idna-3.4 python-magic-0.4.27 requests-2.27.1 urllib3-1.26.14
WARNING: You are using pip version 20.2.3; however, version 22.3.1 is available.
You should consider upgrading via the '/home/sstuck/.pyenv/versions/3.9.2/bin/python3.9 -m pip install --upgrade pip' command.
```

# Running

```
(my_venv) $ python upload.py
Usage: upload.py WebChartUrl docpath mrcsvfile wcuser

(my_venv) $ python upload.py "https://zeus.med-web.com/webchart/wctsstuck/webchart.cgi" ./ sample_data.csv dave
Please enter the webchart password for user [ dave ]: =>
Importing file [ 1 / 2 ]  ccr.xml => MIE-10019
Importing file [ 2 / 2 ]  example.pdf => MIE-10019

Document import process complete:
Uploaded: 2
Skipped: 0
Errors: 0

See import.log for details
```
