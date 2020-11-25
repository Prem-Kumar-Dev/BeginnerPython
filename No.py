a = int(input('Number:\n'))


def fac(n):

    if n > 0:
        return(n*fac(n-1))

    else:
        return 1


print('The factorial of {} is equal to {}'.format(a, fac(a)))
