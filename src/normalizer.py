# Import needed things
import sys, csv, re, pytz
from datetime import datetime

# Normalizer Class
class Normalizer:
    """
    Has functions to do the following:
    - Unicode validation
    - Convert timestamp from PST to EST
    - Make name columns uppercase
    - Check zipcode length
    """

    # Function to open file and use a generator to iterate through each row of the csv.
    # Using a generator so that we can load one row into memory at a time.
    def execute_parse(self, file_name):
        # The errors="replace" argument is super important here. It tells the open
        # function call to replace invalid utf-8 characters with the unicode replacement
        # character

        with open(file_name, "r", encoding='utf-8', errors="replace") as csv_data:
            for row in csv.DictReader(csv_data):
                yield row

   # Function to call the generator and iterate through each row
    def parse_file(self,file_name, outcsv=None):
        iterate_file = iter(self.execute_parse(file_name))
        
        if outcsv is None:
            outcsv = './normalized.csv'

        # Open a file for our writer function. Doing it here to avoid the cost of opening
        # and closing it repeatedly
        with open(outcsv, "a", encoding='utf-8') as csv_out:
            csv_writer = csv.writer(csv_out)


            for index, row in enumerate(iterate_file):
                row['ZIP'] = self.zip_code_validation(row['ZIP'])
                row['FullName'] = row['FullName'].upper()
                row['Timestamp'] = self.timezone_convert_to_est(row['Timestamp'])

                if row['Timestamp'] is False:
                    print("Invalid character in datestampe for row:\n",file=sys.stderr)
                    print(row, file=sys.stderr)
                    next(iterate_file)
                
                row['FooDuration'] = self.convert_to_float_seconds(row['FooDuration'])

                if row['FooDuration'] == False:
                    print("Invalid character/format in FooDuration for row:\n", file=sys.stderr)
                    print(row, file=sys.stderr)
                    next(iterate_file)

                row['BarDuration'] = self.convert_to_float_seconds(row['BarDuration'])

                if row['BarDuration'] == False:
                    print("Invalid character/format in BarDuration for row:\n", file=sys.stderr)
                    print(row, file=sys.stderr)
                    next(iterate_file)
                
                row['TotalDuration'] = row['FooDuration'] + row['BarDuration']

                self.write_out_csv(index, csv_writer, row)

    # Function to write new csv file
    def write_out_csv(self, index, csv_writer, outrow):
        if index == 0:
            csv_writer.writerow(list(outrow.keys()))
        else:
            csv_writer.writerow(list(outrow.values()))



# Function to convert timestamp column values from PST to EST
    def timezone_convert_to_est(self,timestamp):
        # Instead of trying to match a for the Unicode replacement character this implements
        # a 'try' 'catch' so that we simply fail forward if we hit a ValueError caused by
        # that situation.
        try:
            pst = pytz.timezone('US/Pacific')
            timestamp = datetime.strptime(timestamp, "%m/%d/%y %I:%M:%S %p").replace(tzinfo=pst)
            est_timestamp = timestamp.astimezone(pytz.timezone('US/Eastern'))
            return est_timestamp.isoformat()
        except ValueError:
            # This returns false in this situation so that we can print the full row to stderr
            # in parse_file() in order to make the output more useful
            return False
        
# Function to convert FooDuration and BarDuration to floating point seconds format
    def convert_to_float_seconds(self,time_value):
        try:
            time_value = time_value.split(":")
            hours = int(time_value[0])
            minutes = int(time_value[1])
            seconds = float(time_value[2])
            seconds = (hours * 3600) + (minutes * 60) + seconds
            return seconds
        except ValueError:
            # This returns false in this situation so that we can print the full row to stderr
            # in parse_file() in order to make the output more useful
            return False

# Function to check if Zip code has less than 5 digits, if it does prefix with 0
    def zip_code_validation(self,zip_code):
        length = len(zip_code)
        if length < 5:
            zip_code = '0' * (5-length) + zip_code
        return zip_code



