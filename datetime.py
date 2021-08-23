import re
import csv
from collections import Counter


def access_log_reader(logfile):
    myregex = r'[0-9]..\\*.[a-zA-z].\\*.[0-9].[0-9]..[0-9]..[0-9]..[0-9].'

    with open(logfile) as f:
        log = f.read()
        my_iplist = re.findall(myregex, log)
        ipcount = Counter(my_iplist)
        for k, v in ipcount.items():
            print("Date and Time " + "=> " + str(k) +
                  " " + "Count " + "=> " + str(v))
        with open('datetime.csv', 'w') as f:
            for k, v in ipcount.items():
                f.write(str(k) + "\n")


        # Create entry point of our code
if __name__ == '__main__':
    access_log_reader("access.log")
