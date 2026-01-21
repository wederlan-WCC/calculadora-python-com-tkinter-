from tkinter import *
from sympy import sympify
#cria uma janela
j = Tk()
#configura a cor da janela para cinza
j.config(bg="#2F2F2F")
#cria o valor do display
value=""
#cria o disaplay e o configura
display = Label(
    j,
    text="",
    bg="#004F00",
    fg="#000000",
    width=30
)
display.place(x=110,y=15)
#cria uma class botão sem si inporta com carmelcase
class bot:
    def __init__(self,num,ro,co):
        self.num = num
        self.botn = Button(j, text=str(num),command=self.clik)
        self.botn.config(bg="#341539",fg="#9F9F9F")
        self.botn.place(x=int(ro),y=int(co))
    #cria uma funsão para adisionar o botão no display
    def clik(self):
        global value
        global display
        value=value+str(self.num)
        display.config(text=value)
#cria uma funsão para pegar o resultado comsympify em vez de eval por não dar bugs com a base numerica octal
def eq():
    global value
    value2=value.replace("x","*")
    value3=value2.replace("÷","/")
    value=float(sympify(value3))
    value=str(value)
    display.config(text=str(value))
#cria uma função para limpa o display
def clr():
    global value
    value=""
    display.config(text=value)
#outra para limpar apenas um numero
def clrear():
    global value
    value=str(value)[:-1]
    display.config(text=value)
#cria todos os botoes
bc=Button(j,text="C",command=clr)
bex=Button(j,text="\u2190",bg="#341539",fg="#9F9F9F",command=clrear)
bex.place(x=400,y=70)
bc.place(x=500,y=70)
bc.config(bg="#341539",fg="#9F9F9F")
b9 = bot(9,400,150)
bdiv=bot("÷",500,150)
b8=bot("8",300,150)
b7=bot(7,200,150)
b4=bot(4,200,230)
b5=bot(5,300,230)
b6=bot(6,400,230)
b1=bot(1,200,310)
b2=bot(2,300,310)
b3=bot(3,400,310)
b0=bot(0,200,390)
bpt=bot(".",300,390)
bmul=bot("x",500,230)
bmin=bot("-",500,310)
bmas=bot("+",500,390)
equal=Button(j,text="=",command=eq)
equal.config(bg="#341539",fg="#9F9F9F")
equal.place(x=400,y=390)
#usa-se mainloop para a janela não feichar
j.mainloop()
