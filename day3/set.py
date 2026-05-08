#set(집합)
#순서가 없음. 중복 안됨
#중괄호 사용, set({})
my_set={"홍길동","김길동","장길동"}
print(my_set)

football = {"홍길동","김길동","장길동"}
# baseball = {"홍길동","오길동","백길동"}
baseball =set( {"홍길동","오길동","백길동"})

#교집합
print(baseball & football)
print(baseball.intersection(football))

#합집합
print(baseball | football)
print(baseball.union(football))

print(football - baseball)
print(football.difference(baseball))

#추가
football.add("김길동") #중복되는 값이 있다면 추가되지 않음(오류X)
print(football)

#삭제
baseball.remove("오길동")
print(baseball)

#자료형 확인
print(type(baseball))

spo1 = list(baseball)
print(type(spo1))

spo2 = tuple(baseball)
print(type(spo2))