import re
import csv
from collections import Counter


def access_log_reader(logfile):
    myregex1 = r'Windows'
    myregex2 = r'Ubuntu'
# count windows
    with open(logfile) as f:
        log = f.read()
        my_windows = re.findall(myregex1, log)
        windows_count = Counter(my_windows)
        for k, v in windows_count.items():
            print("IP Address " + "=> " + str(k) +
                  " " + "Count " + "=> " + str(v))
        with open('os.csv', 'w') as f:
            for k, v in windows_count.items():
                f.write(str(k) + ","+str(v)+",")
# count ubuntu
    with open(logfile) as f:
        log = f.read()
        my_ubuntu = re.findall(myregex2, log)
        ubuntu_count = Counter(my_ubuntu)
        for k, v in ubuntu_count.items():
            print("IP Address " + "=> " + str(k) +
                  " " + "Count " + "=> " + str(v))
        with open('os.csv', 'a') as f:
            for k, v in ubuntu_count.items():
                f.write(str(k) + ","+str(v))

        # Create entry point of our code
if __name__ == '__main__':
    access_log_reader("access.log")
