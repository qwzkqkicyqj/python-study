money = int(input("투입할 돈을 입력하세요.: "))
price = int(input("물건값을 입력하세요.: "))
if(money < price) :
    print("돈이 부족합니다.")
else :
    a = money - price
    print("거스름돈:",a)
    a500 = a // 500
    a = a % 500
    a100 = a // 100
    a = a % 100
    print("500원 동전의 개수:", a500)
    print("100원 동전의 개수:", a100)
    print("환전 불가 금액:", a)