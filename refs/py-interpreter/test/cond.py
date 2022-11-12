import dis


def cond():
    x = 3
    if x < 5:
        return 'yes'
    else:
        return 'no'

print(cond.__code__.co_code)
print(list(cond.__code__.co_code))
print(dis.dis(cond))

