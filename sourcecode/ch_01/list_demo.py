evens = [0, 2, 4, 6, 8, 10]

# reverses the list
print(evens.reverse())

# adds an object to the list
evens.append(100)
print(evens)

# merges another list with the list
evens.extend([1, 3, 5, 7, 9])
print(evens)

# pops an item from the list
print(evens.pop())

# iterating over a list
for x in evens:
    print(x)
