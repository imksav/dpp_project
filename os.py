import re
import csv
from collections import Counter


def access_log_reader(logfile):
    myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open(logfile) as f:
        log = f.read()
        my_iplist = re.findall(myregex, log)
        ipcount = Counter(my_iplist)
        for k, v in ipcount.items():
            print("IP Address " + "=> " + str(k) +
                  " " + "Count " + "=> " + str(v))
        with open('os.csv', 'w') as f:
            for k, v in ipcount.items():
                f.write(str(k) + "\n")

        # Create entry point of our code
if __name__ == '__main__':
    access_log_reader("access.log")
