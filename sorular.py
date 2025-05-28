# def isPowTwo(num:int) -> bool:
#     i = 0
#     while i < num:
#         if 2 **i == num:
#             return True
#         i+=1
#     return False




# # 2^x == num --> True , or: 1,2,4,8,64,256,1024
# # 3,5


# print(isPowTwo(16))



def isPowTwo(num:int) -> bool:
    for i in range(num):
        if 2**i == num:
            return True
    return False
    
    
print(isPowTwo(32))
print("i love python")