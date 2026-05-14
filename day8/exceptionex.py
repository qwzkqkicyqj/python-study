try:
    num = int(input("정수 입력(0 제외): "))
    res = 10/num
except ValueError :
    print("오류: 정수를 입력하시오.")
except ZeroDivisionError:
    print("오류: 0을 입력하지 마십쇼.")
except Exception as e:
    print(f"오류: {e}")
else:
    print("정상적으로 실행되었습니다.")
    print(res)
finally:
    print("프로그램을 종료합니다.")