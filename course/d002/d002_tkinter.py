# 211005 그림판 만들기

# 모듈 불러오기
from tkinter import *

#변수 선언
window = None
canvas = None
x1, y1, x2, y2, x3, y3 = [None]*6


def mouseClick(self): #마우스 왼쪽 버튼과 연결
    global x1, y1, x2, y2, x3, y3
    x1 = self.x
    y1 = self.y
    print(x1, y1, x2, y2, x3, y3, type(self))
    # 각각의 글로벌 값이랑 self로 받는 값의 타입 확인하기
    # 원한다면 print(self)로 직접 어떻게 저장되는지 확인 가능


def mouseDrop(event): #마우스 왼쪽 버튼 떨어뜨림과 연결
    global x1, y1, x2, y2
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1 or x3, y1 or y3, x2, y2, width = 5, fill = 'red')
    # x1, y1 값이 None으로 뜨는 것을 확인하고 or으로 값을 대신 넣어줌
    print(x1, y1, x2, y2, x3, y3, type(event))


# <Button-1>과 <ButtonPress-1>의 차이 확인하기
# 그리고 굳이 event라고 적어야되는지도 확인하기
def mouseClick2(abcd): #마우스 왼쪽 버튼 클릭과 연결
    global x1, y1, x2, y2, x3, y3
    x3 = abcd.x
    y3 = abcd.y
    print(x1, y1, x2, y2, x3, y3, type(abcd))


window = Tk() # 메인 화면 만들기
window.title('almost paint') # 타이틀 만들기
# 여기서 Tk 클래스는 굳이 bind 안해도 바로 값이 적용됨을 알 수 있음
canvas = Canvas(window, height = 600, width = 600)
# Canvas 선언, window를 부모로 두며 높이와 넓이를 kwarg로 선언
canvas.bind('<Button-1>', mouseClick)
# bind 함수를 실행 시 <Button-1> 이벤트가 발생하면 mouseClick에
# tkinter.Event class 인스턴스를 넣음
# 이 클래스는 x, y, delta, keys 등등의 함수 선언 가능
canvas.bind('<ButtonRelease-1>', mouseDrop)
canvas.bind('<ButtonPress-1>', mouseClick2)
canvas.pack() # Canvas에 무슨 일이 일어났는지 화면에 표시
window.mainloop() # window에 입력이 일어날 때까지 대기
# tk 인터페이스를 닫을 때까지 다음 줄의 명령이 일어나지 않는 것을 알 수 있음
print(type(window)) # <class 'tkinter.Tk'>
print(type(canvas)) # <calss 'tkinter.Canvas'>
