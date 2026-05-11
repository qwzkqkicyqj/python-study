def add(a, b):
    return a+b
# n1 = int(input())
# n2 = int(input())
# print(add(n1,n2))

def avg(a):
    if len(a) == 0:
        return
    return sum(a) / len(a)


score_list = [80, 90, 100,50,70]
score_list2 = []

print(avg(score_list))