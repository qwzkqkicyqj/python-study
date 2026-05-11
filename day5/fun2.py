# 디폴트인수: 함수의 매개변수가 기본값을 갖고 있을 수 있음
def greet(name, msg="별일없지"):
    print("안녕 "+name+", "+ msg)
greet("홍길동")