# def calc(r) :
#     result = 3.14 *r** 2   # r: 반지름
#     return result
# a = calc(r = float(input("반지름 입력(실수): ")))
# print(f"원의 넓이: {a}")
# 함수가 종료되면 함수에서 사용하던 지역변수는 삭제된다.

def calc(r) :
    global b
    b = 3.14 *r** 2   # r: 반지름
    return b
b = 0
r = float(input("반지름 입력(실수): "))
a = calc(r)
print(f"원의 넓이: {a}") 
print(b) # 0출력: 지역변수 b와 전역변수 b는 서로 다른 주소를 가진다(다른 메모리). 단, global를 사용하면 지역변수로 선언한 변수도 전역변수가 된다. (같은 메모리)

    