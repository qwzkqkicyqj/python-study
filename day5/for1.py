import time
# a="봄"
# b="여름"
# print(a,b, sep="과 ", end=" 끝 ")
# print()
#sep: 변수사이에 들어가는 것을 나타냄
#end: 줄을 바꾸지 않고, 옆으로 작성 (주로 줄바꿈 무력화를 위해 사용됨)

# for i in range(0,11,2): #0~10까지 2씩 증가
# 구구단에서 원하는 단을 입력받아서 출력


# for j in range(1, 10, 1):
#     print(str(j)+"단")
#     for i in range(1, 10, 1):
#         if i == 9:
#             print(str(j)+"x"+str(i)+"="+str(j*i), end="")
#         else:
#             print(str(j)+"x"+str(i)+"="+str(j*i), end=", ")
#     print()

for k in range(10,0,-1):
    print(k)
    time.sleep(1) #1초 정지
print("발사!")
