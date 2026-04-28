name = input("과일 이름: ")
price = int(input("개당 가격: "))
count = int(input("총 개수: "))
print(name, "의 총 가격은 ",price*count,"원입니다.")
print(name+"의 총 가격은 "+str(price*count)+"원입니다.")
print(f"{name}의 총 금액은 {price*count}원입니다.")
# print안에서 f는 f-string이라하며 포맷 문자열
# --> f"{변수 값}""
# 숫자 -> 문자로 변환: str
# 실수는 float만 있음(8byte)