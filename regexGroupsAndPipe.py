import re
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo= phoneNumberRegex.search('My number is 415-555-4242')
print(mo.group())
print(mo.group(1))
print(mo.group(2))

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo2 = batRegex.search('Batmobile lost a batputo inside a Batman')
print(mo2.group())