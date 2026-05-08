# a = input("영어 한 글자를 입력하세요")
# if (a >= "A" and a<="Z"):
#         print("대문자 -> 소문자")
#         print(a.lower())
# else :
#         print("소문자 -> 대문자")
#         print(a.upper())
# 아래와 위 모두 같은 결과
# a = input("영어 한 글자를 입력하세요")
# if(a.isupper()) : #대문자인가?
#     print("대문자 -> 소문자")
#     print(a.lower())
# else : 
#     print("소문자 -> 대문자")
#     print(a.upper())


#점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
#사용자로부터 score를 입력받아 학점을 출력하라.
#점수  학점
#81~10 A
#61~80 B
#41~60 C
#21~40 D
#0~20  E
while (True): 
    try:
        score = int(input("점수를 입력하세요(0~101사이 입력, 101입력시 종료): ")) 
    except:
        print("입력 오류(정수를 입력하세요.)")
        continue
    if (score >= 81 and score <= 100 ):
        print("A")
    elif (score >= 61 and score <= 80) :
        print("B")
    elif (score >= 41 and score <= 60):
        print("C")
    elif (score >= 21 and score <= 40):
        print("D")
    elif (score >= 0 and score <= 20):
        print("E")
    elif (score == 101):
        print("시스템을 종료합니다.")
        exit()
    else :
        print("입력 오류(0~101 사이의 숫자를 입력하세요.)") 
    