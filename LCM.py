user_input = int(input('The number of values you have to work with:\n'))
factors = []
result = []
answer = []
x = 2
counter = 0

for y in range(0, user_input):
    user_value = int(input('The number:\n'))

    while user_value != 1:

        while user_value % x == 0:
            user_value = user_value/x
            factors.append(x)
        x = x+1
    counter = counter+1

    for n in factors:

        if n in result:
            result.remove(n)

        answer.append(n)

    answer = answer+result
    result = answer
    answer = []
    factors = []
    x = 2

x = 1
for n in result:
    x = x*n
print('LCM:', x)
