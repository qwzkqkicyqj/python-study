#숫자 입력 -> 출력 반복 -> 0 입력시 종료

# while(True):
#     num = float(input("숫자를 입력하세요.(0 입력시 프로그램 종료): "))
#     if (num == 0):
#         print("프로그램 종료")
#         exit()
    
#     print(num)

print("=" * 20)

menu =["쫄면", "김밥", "냉면", "오뎅"]
b=input("메뉴 선택: ")

while b in menu: #조건이 참일때 수행 #in은 포함 연산자
    print(b)
    b=input("메뉴 선택: ")
    print(b)
    # while문장안에서 반드시 거짓으로 변경되는 문장이 나와야 함.