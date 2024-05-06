 
'''
root = tkt.Tk()
root.title("이름")

lbl = tkt.Label(root, text = "부트캠프")
lbl.pack()

txt = tkt.Entry(root)
txt.pack()

btn = tkt.Button(root,text="OK")
btn.pack()

root.mainloop()
'''
import tkinter as tkt
from tkinter.filedialog import *
 
window = tkt.Tk()
window.title('Notepad')
window.geometry('400x400+0+0') #창크기(400,400) 창 우ㅣ치
window.resizable(0,0) # 창 크기 설정 불가

#window.iconbitmap("C:\\Users\\AAA\\Desktop\\새 폴더\\memo.ico")
photo = tkt.PhotoImage(file="haedal.png")
window.iconphoto(False, photo)

#텍스트 창 만들기 
text_area = tkt.Text(window)
#공백 설정하기 
window.grid_rowconfigure(0, weight =1)
window.grid_columnconfigure(0, weight = 1)
#텍스트 화면을 윈도우에 동서남북으로 붙인다
text_area.grid(sticky = tkt.N+tkt.E+tkt.S+tkt.W)

def new_file():
    text_area.delete(1.0, 'end')
def save_file():
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, 'end'))
def maker():
    makerr = tkt.Tk()
    makerr.title("만든 이")
    makerr.geometry('300x100+0+0')
    makerr.resizable(0,0)
    label=tkt.Label(makerr, text="김재민!!",background='gray')
    label.pack()
    makerr.mainloop() 

#    tkt.messagebox.showinfo("만든 이", "나")
      
#메뉴 생성
menuMaker = tkt.Menu(window)
#첫번째 메뉴 만들기 
first_menu = tkt.Menu(menuMaker, tearoff=0)
#첫번째 메뉴의 세부메뉴 추가 및 함수 연결
first_menu.add_command(label = '새 파일', command = new_file)
first_menu.add_command(label = '저장', command = save_file)
#메뉴 바 추가 
menuMaker.add_cascade(label='파일', menu=first_menu)

first_menu.add_separator()
#메뉴 구성
window.config(menu = menuMaker)

#종료 옵션 추가하기
first_menu.add_command(label='종료', command=window.destroy) 


#두번째 메뉴 추가 
second_menu = tkt.Menu(menuMaker, tearoff=0)
#세부 메뉴 추가, 함수 연결
second_menu.add_command(label = '만든 이', command = maker)
#메뉴 바 추가
menuMaker.add_cascade(label='정보', menu = second_menu)

window.mainloop() # 창 실행!


