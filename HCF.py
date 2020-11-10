user_input = int(input('The number of values you have to work with:\n'))
factors = []
result = []
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

    if counter == 1:
        result = factors

    else:
        answer = []
        for n in result:
            if n in factors:
                factors.remove(n)
                answer.append(n)
        result = answer

    x = 2
    factors = []

x = 1
for n in answer:
    x = x*n

print('HCF:', x)
