a_list = ['사과', "배", '오렌지']

try:
    index = int(input("번호 입력(0~2): "))
    if index < 0 or index>=len(a_list):
        raise IndexError # 예외를 발생시킴

except IndexError:
    print("없는 인덱스")
except ValueError:
    print("입력 오류")
except Exception as e:
    print(f"오류: {e}")
else :
    print(a_list[index])
    print("정상 작동")
