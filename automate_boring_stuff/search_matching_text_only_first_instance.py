import re


phoneNumRegex = re.compile(r' \d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group()) #  will return only '415-555-9999'
