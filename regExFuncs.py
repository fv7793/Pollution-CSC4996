import re

#function to take a sentence and return the date in it - one format

str = """A chemical was spilled on 10/10/2015"""

#MM/DD/YYYY
all = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", str)

for s in all:
    print(s)





    
