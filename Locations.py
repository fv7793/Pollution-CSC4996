import re

class locations():
    # reading from a body of text to find locations
    test = open("LocationTest.txt", "r")
    lakes = re.compile(r'(?i) lake (\w+)')
    rivers = re.compile(r'(?i)\w+(?=\s+river)')
    # return all locations found in body of text from file
    for line in test:
        lake = lakes.findall(line)
        for location in lake:
            print(location)
        river = rivers.findall(line)
        for location in river:
            print(location)