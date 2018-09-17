# Sample project

## Description

This is a command line python script that takes a csv in a given format and normalizes it to another specified format. The details regarding how it's formatted are in the README under ./sample_input.

## How to use it

1. (Optional) Set up and use a python virtual environment (if you're on macOS and installed python3 with brew you have pyvenv already)

2. Clone this repo.

3. Use pip to include any third party libraries you need. In this case, the only thing we needed was pytz (for time zone fun), this can be installed manually via 'pip install pytz' or using the requirements.txt file included here using 'pip install -r requirements.txt'

4. Running tests. Assuming you're in the main project directory you'll need to change directories to ./src . From there you can run the unit tests by running:

```
python -m unittest test.py
```

5. Run the actual app. You can run this app on the two sample data sets we have in ./sample_input. Ostensibly it could also be run on other csv files that follow the same structuring. To run this on sample.csv do the following from ./src:

```
python csv_normalizer.py -f true ../sample_input/sample.csv
```

This example is using -f true which means it's going to overwrite if there's a filename conflict. Below is the help output you get if you use the script with the -h flag.

```
usage: csv_normalizer.py [-h] [-o OUTCSV] [-f FORCE] csv

Python script that normalizes CSVs for a coding exercise. Read out the
README.md in ../sample_input/ for more information. Example Use: python3
csv_normalizer.py csv ../sample_input/sample.csv outcsv ./normalized.csv

positional arguments:
  csv                   CSV file for normalization.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTCSV, --outcsv OUTCSV
                        Name the normalized CSV that is saved at the end.
                        Defaults to ./normalized.csv if this option isn't set
  -f FORCE, --force FORCE
                        Overwrites existing output file if present
                        
```