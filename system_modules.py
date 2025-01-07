import sys
print(sys.path)
print(sys.version)
print(sys.platform)
print(sys.argv)


# for i in range(10):
#   print(i)
#   if(i==3):
#     sys.exit()


import os
print(os.name)
print(os.getcwd())
print(os.listdir())

print("\n\n\n")

# loop though all the files in a directory
for path,dirs,files in os.walk(f"{os.getcwd()}/oopc"):
  print(files)

import datetime
time = datetime.datetime.now()
print(time)
print(time.year)
print(time.month)
print(time.day)
print(time.hour)
print(time.minute)
print(time.second)
print(time.microsecond)


import re  # regex
email = "arpitparekh9@gmail.com"
# "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
ans=re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",email)

if ans:
  print("valid email")
else:
  print("invalid email")

"""
# Email Address
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# URL
url_pattern = r'^https?://[^\s/$.?#].[^\s]*$'

# IP Address
ip_address_pattern = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'

# Date (YYYY-MM-DD)
date_pattern = r'^\d{4}-\d{2}-\d{2}$'

# Time (HH:MM:SS)
time_pattern = r'^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$'

# Password Complexity
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

# Phone Number
phone_number_pattern = r'^\+?[1-9]\d{1,14}$'

# File Path
file_path_pattern = r'^([a-zA-Z]:)?(\\[a-zA-Z0-9_.-]+)+\\?$
"""

"""


    os: Interact with the operating system.
    sys: Access system-specific parameters and functions.
    math: Mathematical functions.
    datetime: Manipulate dates and times.
    re: Regular expressions for string matching.

    // database
    csv: Read and write CSV files.
    sqlite3: SQLite database access.

    random: Generate random numbers.  // check
    itertools: Functions that create iterators for efficient looping. // check
    functools: Higher-order functions for functional programming. // check

    threading: Thread-based parallelism.
    multiprocessing: Process-based parallelism.
    subprocess: Spawn new processes, connect to their input/output/error pipes.

    http: Modules for HTTP requests and responses.  // api calling
    urllib: URL handling modules. // api calling
    json: Work with JSON data. // api calling

    socket: Low-level networking interface.  // socket programming

    xml: XML processing modules.  // api call

"""
