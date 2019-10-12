i = 0
# condition
while i < 10:
    print('i =  {}'.format(i, end=' ')) # print value of i, end='' means print on same line
    i += 1  # increment i

print()

i, sum = 0, 0
while i < 1000:
    i += 1
    sum += i

print('The summation of 1...1000 = {}'.format(sum))