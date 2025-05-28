lst = [12,19,20.1,9.9999999999999999,
       'soner','samsun',21,10.00001
    ]

def sayilar(my_list):
    res = []
    for item in my_list:
        if (item % 2 == 0) and item> 10 and type(item) == int:
            res.append(item)
    res(res)
    
print(sayilar(lst))