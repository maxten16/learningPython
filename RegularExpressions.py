import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line'

phoneNumberRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumberRegEx.findall(message))
