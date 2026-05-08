# #문자열
# s="hello python"
# print(s[6]) #인덱싱
# print(s[6:12]) #슬라이싱

# jumin="080101-3123456"
# print("성별: "+jumin[7])
# print("월: "+jumin[2:4])
# print("일: "+jumin[4:6])
# # print("뒷번호: "+jumin[7:])
# print("뒷번호: "+jumin[-7:])

# s1="나는 학생입니다"
# s2="파이썬을 배웁니다"
# s3='재미있습니다'

# #여러 문자열 저장할 때, 입력한 그대로 저장
# s4=""" 
# 나는 학생입니다
# 파이썬을 배웁니다
# 재미있습니다
# """

# print(s4)

# year = "1979"
# month="08"
# day= "23"
# date = year+"-"+month+"-"+day
# print(date)

# date2 = date.split("-")
# print(date2)

# print(type(date2))

# print(date2[1][0:], end = "*")

# name = "kakao taxi"
# name2 = name.replace("k", "t", 1)
# print(name2)

# print("python " * 5) #반복


# #문자열에서 컴마 제거
# won = "63,120,450"
# won2 = won.replace(","," ")
# print(won2)

# won3 = 345900000
# won4 = format(won3, ",")
# print(won4)

# #문자열 대소문자, 길이
# p = "Python is Amazing"
# print(p.lower())
# print(p.upper())
# print(p.capitalize())
# print(p[0].isupper())
# print(len(p))
# print(p.count("i"))

# #위치
# index = p.index("i") #7
# print(index)
# index = p.index("i", index+1) #14
# print(index)

#문자열 연결
words = ["Python","is","easy"]
result = "/".join(words) #sep같은 기능
print(result)

#제거
text = "          hello           Python****"
print(text.strip()) #공백 제거
print(text.rstrip("*")) #오른쪽 "*" 제거, lstrip(): 왼쪽부터

#자리수만큼 0으로 채우기
num = "5"
result = num.zfill(3)
print(result)

#format
age = 19
print("나는 %d살입니다." %age) #19을 %d 자리에 넣음
print("나는 {}살 입니다.".format(age))

like="노래부르기"
print("나는 %d살이고 %s를 좋아해요" %(age,like))
print("나는 {0}살이고 {1}를 좋아해요".format(age,like))

#f스트링
print(f"나는 {age}살이고 {like}를 좋아해요.")


print("나의 주소는 {addr}이며, 나의 키는{height}cm입니다.".format(addr = "안전", height=165))

#이스케이프(탈출) 문자
print("\n배우는 과목은\n \"파이썬\" 입니다.")
#\r: 커서를 맨앞으로 이동
print("red apple\rpine")
print("I like you\b!!") #\b는 한 글자 삭제
print("red\t apple") #\t: tap

p="Python is Amazing"
#인덱스 찾기
print(p.find("A")) #왼쪽부터 찾아서 인덱스 번호 출력, 10
print(p.rfind("A")) #오른쪽부터
print(p.index("a")) #왼쪽부터 찾아서 인덱스 번호 출력, 12
print(p.rindex("a"))  #오른쪽부터

print(p.find("java")) #없는 문자를 찾으면 -1
# print(p.index("java")) #없는 문자를 찾으면 에러 발생

arr_Str=input("input String: ").split("-") #infomation-technology
arr_Len=int(input("input number: ")) #12
arr_Val = list(range(0, arr_Len, 2))
arr_Val.remove(4)
print(arr_Str[1].find("i")+arr_Val[2])