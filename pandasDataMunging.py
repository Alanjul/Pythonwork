"""Introduction to Data science: Pandas, Regular Expressions and Data Munging
Cleaning
Delete observation from missing values
Substituting reasonable values for missing values
Delete observations  with bad values
Substituting reasonable values for bad values
Tossing outliers (although sometimes you'll want to keep them
Duplicating elimination(although sometimes duplicate are valid
dealing with inconsistent data'
#transforming data
   -removing unnecessary data and features
    -Combining related features
     -Sampling data to obtain a representative subset
      standarding the data formats
      grouping data
"""

import pandas as pd
import re
#using regular expressions
zipcodes = pd.Series({"Kansas city": "66108", "Miami" : "3310"})
print(zipcodes)
#provide  as string of 5 numbers of zip codes
print(zipcodes.str.match(r'\d{5}') )
#
cities = pd.Series(["Kansas, KS 66103", "Miami, FL 33101" ])
result = cities.str.contains(r' [A-Z]{2} ')
print(result)
result2 = cities.str.match(r' [A-Z]{2} ')
print(result2)  # false it will match the entire string
contacts = [["ALan Julius", "alan@ru,com", 5555668124],
            ["Emily Josephine", "Emily@j.com", 4414436214]]
contactsdataframe= pd.DataFrame(contacts, columns=["Name", "Email", 'Phone'])

print(contactsdataframe)

def format_phone(value):
    value = str(value)
    results3 = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)
    return f'({results3.group(1) }) {results3.group(2)}-{results3.group(3)}'if results3 else value
formatPhone = contactsdataframe["Phone"].map(format_phone)
print(formatPhone)
contactsdataframe['Phone'] = formatPhone
print(contactsdataframe)
def formated_phone(value):
    value = str(value)
    results3 = re.fullmatch(r'(\d{3})(\d{3})', value)
    if results3:
        part1, part2, part3 = results3.groups()
        return f'({part1}) {part2} - {part3}'
    else:
        return value
formatsPhone = contactsdataframe["Phone"].map(formated_phone)
print(formatsPhone)



