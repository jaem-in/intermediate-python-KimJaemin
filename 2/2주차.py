import tkinter as tkt
# 창 생성
root = tkt.Tk()
root.title("계산기")

# 아이콘 설정
# photo = tkt.PhotoImage(file="C:/Study/해달/부트캠프/2024-1-파이썬응용/2주차/윈도우계산기아이콘.png")
photo = tkt.PhotoImage(file="./2/윈도우계산기아이콘.png")
root.iconphoto(False, photo)

# 글 적을 공간 생성! 
#entry = tkt.Text(root)
#entry.grid(row=0, column=0)  # 0행, 0열에 배치

# 엔트리 생성 (한줄 텍스트) 한줄
#entry = tkt.Entry(root, width=35)
#entry.grid(row=0, column=0, columnspan=4, pady=10)  # 0행, 0열에 배치, 4개의 열을 차지, y축에패딩(여백)추가
# 엔트리 생성 (한줄 텍스트) 간지
entry = tkt.Entry(root, width=20, borderwidth=12, font=("Verdana", 13), justify="right")  # borderwitdh: 테두리두께
entry.grid(row=0, column=0, columnspan=4, pady=10)

def on_click(number):
    entry.insert(tkt.END, number)
'''
for number in range(9):
    button = tkt.Button(root, text=number+1, padx=40, pady=20, command=lambda n=number+1: on_click(n))
    button.grid(row=4-number//3, column=number%3)
    # 이 경우에 command에 담기는 것은 number+1을 인자로 받고, on_click(n)이라는 함수 내용을 가진 람다함수 그 자체
    # 람다 함수란? 이름조차 짓기귀찮은 간단한 함수 만들 때 사용
	    # lambda 인수: 반환값
    # 프로그램 실행 시 on_click(number+1) 함수가 실행되고, 그 결과가 command에 할당됨
    # 이 경우에는 함수의 return값이 없으므로 command에는 아무것도 담기지 않음
'''

def create_button(text, row, column, command, width=15, height=2, columnspan=1, bg='gainsboro', borderwidth=5):
    button = tkt.Button(root, text=text, padx=width, pady=height, command=command, borderwidth=borderwidth, bg=bg)
    button.grid(row=row, column=column, columnspan=columnspan, sticky='nsew')

for number in range(9):
    create_button(str(number + 1), 4-number//3, number%3, lambda n=number+1: on_click(n)) #, bg='gainsboro')
create_button("0", 5, 0, lambda: on_click(0), columnspan=2, bg='gainsboro')


def on_clear():
    entry.delete(0, tkt.END)

create_button("C", 1, 0, on_clear, bg='gray70')

def operate(operator):
    global first_num
    global 연산자
    연산자 = operator
    first_num = float(entry.get())
    entry.delete(0, tkt.END)

def on_equal():
    second_num = float(entry.get())
    entry.delete(0, tkt.END)

    if 연산자 == "+":
        entry.insert(0, first_num + second_num)
    elif 연산자 == "-":
        entry.insert(0, first_num - second_num)
    elif 연산자 == "*":
        entry.insert(0, first_num * second_num)
    elif 연산자 == "/":
        entry.insert(0, first_num / second_num)
    elif 연산자 == "%":
        entry.insert(0, first_num % second_num)
 


create_button("%", 1, 2, lambda: operate("%"), bg='gray70')
create_button("/", 1, 3, lambda: operate("/"), bg='gray70')
create_button("*", 2, 3, lambda: operate("*"), bg='gray70')
create_button("-", 3, 3, lambda: operate("-"), bg='gray70')
create_button("+", 4, 3, lambda: operate("+"), bg='gray70')
create_button("•", 5, 2, lambda: on_click('.'), bg='gainsboro')
create_button("=", 5, 3, on_equal, bg='orange')

root.mainloop()

# 소수점 계산 할수있게 구현하기 나머지 연산 버튼 테두리 있어보이게 만들기