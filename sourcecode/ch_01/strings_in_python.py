city = 'Los Angeles'
# indexing: python is a zero based indexed language
print(city[0])  # L
print(city[3])  # empty space is a string!
print(city[4])  # capital A
print(city[-1]) # negative indices are permitted
# len() function: gets the length of the string
print(len(city))    # 11
print(city[len(city)-1]) # s
# concatenation: the combining of multiple strings
print('john ' + 'doe ' + 'public') # john doe public
# slicing: retrieves ranges of a string
print(city[0:3])   # Los
print(city[4:11])  # Angeles
print(city[::])    # Los Angeles
print(city[::2])   # LsAgls
print(city[::-1])  # selegnA soL