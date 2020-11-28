c = input('1')


def merge_sort(a, b):
    s, e, new = 0, 0, []
    while s < int(len(a)-1) and e < int(len(b)-1):
        if a[s] >= b[e]:
            new.append(b[s])
            s += 1
        else:
            new.append(a[e])
            e += 1

    print(new)


a = [2, 1, 3]
b = [4, 6, 0]
merge_sort(a, b)
