class board:
    def set_data(self, title, writer):
        self.title = title #오른쪽 title은 호출할때 받아 온 매개변수 값
        # 왼쪽 title은 객체의 멤버변수
        # 내자신(객체) 의미: self
        self.writer = writer
        self.cnt = 0

    def cntup(self):
        self.cnt += 1

    def __init__(self):
        print('객체 생성 완료')
    
board1 = board()
board2 = board()

board1.set_data("파이썬 정석", "홍길동")
board2.set_data("자바 정석", "김길동")

board1.cntup()
board1.cntup()
board2.cntup()
print(board1.title,board1.writer,board1.cnt)
print(board2.title,board2.writer,board2.cnt)

board3 = board()
# board3 = cntup() #set_data 함수를 호출하지 않아 cnt가 생성되지 않음. -> 오류