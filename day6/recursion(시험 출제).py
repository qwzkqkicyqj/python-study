# #재귀 호출(함수)(함수 내부에서 자기자신을 호출)
# # 5!(팩토리얼): 1*2*3*4*5 = 120 #n! = n * (n-1)!
# def fact(n): #fact: 함수명(매개변수는 1개)
#     if n <= 1:
#         return 1
#     else :
#         return 1 * n * fact(n-1) #n! = n * (n-1)!

# a=int(input("정수 입력: "))
# res = fact(a) #함수 호출, 인수 a(정수) 보냄
# # 반환되어서 온 결과값을 res에 저장
# print(f"{a}! = {res}")

#순환(재귀)함수를 활용하여 1부터 입력받은 숫자까지 합을 구하는 프로그램 작성
def sum(n):
    if n == 0:
        return 0
    else:
        print(n, end="x")
        if n == 1 :
            print("\b", end="=")
        return n + sum(n-1)
    

n = int(input())

print(sum(n))