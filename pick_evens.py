from icecream import ic
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

def isPalindorme(word):
    return word == word[::-1]
        
for word in lst:
    ic(word,isPalindorme(word))



def gt_3(astr):
    res = []
    if len(astr)>3:
        res.append(astr)
    return res

for astr in lst:
    ic(gt_3(astr))
    
print('hello world')
