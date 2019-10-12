for x in range(10):
    print(x, end=' ')

print()

x, y = 0, 1
for z in range(10):
    next = x + y
    x, y = y, next
print('12th fib number = {}'.format(next))
