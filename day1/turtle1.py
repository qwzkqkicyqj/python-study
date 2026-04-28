import turtle

t=turtle.Turtle() # turtle 객체 생성, t 변수에 할당
t.shape("turtle") # shape 모양 생성
radius = 50 #반지름 설정
t.circle(radius) #원 그리기
t.fd(30) #앞으로 이동
t.circle(radius)
t.fd(50)
for i in range(4):
    t.forward(2*radius)
    t.right(90)
for i in range(3) :
    t.forward(2*radius)
    t.right(120)
# 한 변의 길이가 반지름*2인 정삼각형 그리기