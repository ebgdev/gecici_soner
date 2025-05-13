lst = [i for i in range(100)]

def ciftler(lst):
    res = []
    for sayi in lst:
        if sayi % 2 == 0:
            res.append(sayi)
    return res

print()