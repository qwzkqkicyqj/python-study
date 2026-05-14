import random as r

# def get_lotto():
#     lotto=[]
#     while len(lotto) != 7:
#         lotto.append(r.randint(1,45))
#         lotto=list(set(lotto))
#     return lotto
# print(get_lotto())

def get_lotto():
    lotto=[]
    while len(lotto) != 7:
        a=r.randint(1,45)
        if a not in lotto:
            lotto.append(a)    
        else :
            continue
    return lotto
print(f"로또 번호: {get_lotto()}")