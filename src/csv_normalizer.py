# Import needed things
import argparse
import os.path
import sys

from normalizer import Normalizer

# Description text
description = """Python script that normalizes CSVs for a coding exercise. 
    Read out the README.md in ../sample_input/ for more information. 
    Example Use: python3 csv_normalizer.py csv ../sample_input/sample.csv outcsv ./normalized.csv"""


# Take input arguments
parser = argparse.ArgumentParser(description=description)
parser.add_argument('csv', help='CSV file for normalization.')
parser.add_argument('-o', '--outcsv', help='Name the normalized CSV that is saved at the end. \
    Defaults to ./normalized.csv if this option isn\'t set')
parser.add_argument('-f', '--force', help='Overwrites existing output file if present', type=bool)
args = parser.parse_args()
print(args)

# Check for optional outcsv argument. Use default if not present.
if args.outcsv is None:
    outcsv = './normalized.csv'
else:
    outcsv = args.outcsv

# Reject missing file with reasonable feedback
if os.path.isfile(args.csv) is not True:
    sys.exit(''.join(('Error: ', args.csv, ' not found. Please provide a valid CSV file path.')))

# If -f is used and file outcsv already exists delete it
if os.path.isfile(outcsv) is True:
    os.remove(outcsv)


# Parse CSV and replace bad values with proper ones (normalizing)
norm = Normalizer()
if outcsv is None:
    norm.parse_file(args.csv)
else:
    norm.parse_file(args.csv, outcsv)


#end
print('Complete.')