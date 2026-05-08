#주민번호를 입력
#1, 3 -> 남자 아니면 2, 4 -> 여자

# ID = input("주민번호를 입력하세요.(\"-\"포함): ") #080101-3123456
# if (int(ID[7]) == 1 or int(ID[7]) == 3) :
#     print("남자")
# elif (int(ID[7]) == 2 or int(ID[7]) == 4):
#     print("여자") 
# ID = input("주민번호를 입력하세요.(\"-\"포함): ").split("-") #080101-3123456
# if (int(ID[1][0]) == 1 or int(ID[1][0]) == 3) :
#     print("남자")
# elif (int(ID[1][0]) == 2 or int(ID[1][0]) == 4):
#     print("여자") 

#사용자로부터 세 개의 숫자를 입력 받은 후
#가장 큰 숫자를 출력하라

num = list(map(int, input("숫자 3개를 입력하시오.(숫자간 띄어쓰기 사용): ").split()))
if(num[0] < num[1] and num[1] > num[2]) :
    print(num[1])
elif(num[0] < num[2] and num[2] > num[1]) :
    print(num[2])
elif(num[1] < num[0] and num[0] > num[2]) :
    print(num[0])