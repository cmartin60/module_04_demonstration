"""
Description: program will provide salary increases of 20% to all 
executives at PiXELL-River Financial. prior to implementing this change, 
the program will see how many executives will end up with salaries greater than
the high-salary mark.

Author: Christian Jorge R. Martin

Date: 02-15-2024


steps on Exception Handling:
DETECT
RAISE
HANDLE
RESUME
"""

"""
try:
        1/0
        file = open ('module_4_dat.txt')
        data = file.readlines()

        file.close()
        print("File Closed")
except FileNotFoundError as fnfe:
        print("File does not exist: ", fnfe)
except Exception as e:
        print("Something went wrong", e)
"""
data = []
new_data = []

RECOMMENDED_INCREASE = 12000

# LECTURE SECTION 1
# Specific to general exceptions
try:
    file = open ('module_4_data.txt')
    data = file.readlines()
except FileNotFoundError as fnfe:
    print("File does not exist: ", fnfe)
except Exception as e:
    print("Something went wrong: ", e)
finally:
    if file is not None:
        file.close()
        print("File Closed")

# LECTURE SECTION 2
try:
    if len(data) == 0:
            raise Exception("No Data exists")
    else:
        for record in data:
            items = record.split(',')
            title = items [0]
            name = items [1]
            salary = float(items[2])
except FileNotFoundError as fnfe:
        print("File does not exist: ", e)

# LECTURE SECTION 3
        salary *= (1 - RECOMMENDED_INCREASE)
        new_data.append([title,name,salary])


##### LOGGING #####
import logging

logging.basicConfig(
     level = logging.DEBUG,
     filename = "app.log",
     filemode = "a", #'w' for one time use , 'a' to add on existing file.
     format = ('%(asctime)s - %(levelname)s - %(message)s')
)

logging.debug("Debug message.")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

