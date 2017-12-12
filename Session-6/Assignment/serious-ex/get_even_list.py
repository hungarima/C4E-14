
def get_even_list(l):
    new_l = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            new_l.append(l[i])
    return new_l
