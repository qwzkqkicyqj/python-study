# try :
#     menu = int(input("메뉴를 선택하세요.(1: 입금, 2: 출금, 3: 잔액 없음)"))
# except:
#     print("입력 오류: 정수를 입력하세요")
#     exit()
# match menu :
#     case 1:
#         print("입금")
#     case 2:
#         print("출금")
#     case 3:
#         print("잔액 없음")
#     case _ :
#         print("입력 오류: 1 혹운 2를 입력하세요.")


# try :
#     num1 = int(input("짝수 입력(정수): "))
#     num2 = int(input("홀수 입력(정수): "))
# except:
#     print("입력 오류: 정수를 입력하세요")
#     exit()
# match num1%2, num2%2 :
#     case 0,1:
#         print("num1은 짝수 num2는 홀수")
#     case 0,_:
#         print("num1은 짝수 num2는 아무숫자")
#     case _,1:
#         print("num2는 홀수 num1은 아무숫자")
#     case _ :
#         print("입력 오류")


try :
    num1 = int(input("3의 배수 입력(정수): "))
    num2 = int(input("5의 배수 입력(정수): "))
except:
    print("입력 오류: 정수를 입력하세요")
    exit()
match num1%3, num2%5 :
    case 0, 0:
        print("num1은 3의 배수, num2는 5의배수")
    case 0,_:
        print("num1은 3의 배수, num2는 아무숫자")
    case _,0:
        print("num1은 아무숫자, num2는 5의 배수")
    case _ :
        print("입력 오류")