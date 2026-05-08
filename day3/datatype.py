# 리스트
subway=["아이유","변우석","박지훈","유재석"]
print(subway)

subway.append("장원영")
print(subway)

subway.insert(1, "카리나")
print(subway)

print(subway.index("박지훈"))

print(subway.pop()) #가장 뒤 자료 삭제 및 삭제 값 반환
print(subway)

name = subway.pop(1) #1번 인덱스 값 삭제 및 삭제 값 반환
print(name)

del(subway[3]) #subway.remove("유재석")과 같음.
print(subway)

subway.append("아이유")
print(subway)

print(subway.count("아이유"))

subway.remove("아이유")
print(subway)

num_list=[2,4,5,1,3]

num_list.sort() #오름차순

print(num_list)

num_list.reverse() #내림차순

print(num_list)

num_list.clear() #초기화

# 리스트: 순서가 있음. 나열형. 값을 수정할 수 있음. 대괄호 사용
# 튜플: 순서가 있음. 나열형. 값을 수정할 수 없음. 소괄호 사용
menu=("김밥","오뎅")
print(menu)
# menu[1]="피자" -> 튜플은 값 변경 불가(오류 발생)
# print(menu)

(name, age, addr) = ("이순신",30,"안산") #언패킹: 한 번에 많은 변수 선언, 리스트와 튜플도 가능
print(name, age, addr)

#딕셔너리: 키와 값이 쌍으로 구성
classroom = {407:"개발자 과정",
             402:"영상 과정"}

print(classroom)
print(classroom[407])
# print(classroom[404])

print(classroom.get(407)) 
print(classroom.get(404)) #안정성이 높다. (값이 없을 시 실행을 멈추지 않고, none출력) 

print(classroom.keys()) #키 출력
print(classroom.values()) #값 출력
print(classroom.items()) #키와 값 둘 다 출력

del classroom[402] #삭제
print(classroom)