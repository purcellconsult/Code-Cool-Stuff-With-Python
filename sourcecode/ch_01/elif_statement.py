from random import randint
# picks a random number in range 1...100
grade = randint(1, 100)
if grade >= 90 <= 100:
    print('A')
elif grade >= 80 <= 89:
    print('B')
elif grade >= 70 <= 79:
    print('C')
elif grade >= 60 <= 69:
    print('D')
else:
    print('F!')