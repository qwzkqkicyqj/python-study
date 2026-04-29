movie_list = ["아바타","왕사남","살목지","극한직업"]
print(movie_list)

#메서드(insert. append, remove)
movie_list.insert(1, "범죄도시") #해당 인덱스에 삽입 (그 자리에 있던 값은 뒤로 밀려남)
print(movie_list)

movie_list.append("슈퍼맨") #맨 뒤에 값이 추가됨
print(movie_list)

movie_list.remove("살목지") #값을 지정하여 삭제
print(movie_list)

#del: 명령어
del movie_list[2] #인덱스 번호를 지정하여 삭제
print(movie_list)

x = 10
print(x)
del x 
# print(x)

print(len(movie_list)) #len: 배열의 길이

a = [1,2,3]
print(sum(a))

a = [90, 50, 70, 80, 55]
print(sum(a) / len(a))
