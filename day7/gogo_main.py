from gugu_modul import *

b = True
while (b) :
    menu = int(input("출력 방식을 선택하시오.(1 or 2 / 0입력시 종료): "))

    match menu:
        case 1 :
            v_gugudan()
            
        case 2 : 
            h_gugudan()
        
        case 0:
            print("프로그램을 종료합니다.")
            b = False
        
        case _:
            print("잘못된 입력")