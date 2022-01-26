from tkinter import *

tictac=Tk()
tictac.geometry('800x500')
tictac.title('tictactao')

def change(b):

          b.config(text='cc')
b1=Button(text='',font=('arial', 20),width=5,command=lambda :change(b1))
b2=Button(text='',font=('arial',20),width=5,command= lambda :change(b2))
b3=Button(text='',font=('arial',20),width=5,command= lambda :change(b3))
b4=Button(text='',font=('arial',20),width=5,command= lambda :change(b4))
b5=Button(text='',font=('arial',20),width=5,command= lambda :change(b5))
b6=Button(text='',font=('arial',20),width=5,command= lambda :change(b6))
b7=Button(text='',font=('arial',20),width=5,command= lambda :change(b7))
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)
b4.grid(row=0,column=4)
b5.grid(row=0,column=5)
b6.grid(row=0,column=6)
b7.grid(row=0,column=7)



bb1=Button(text='',font=('arial',20),width=5,command= lambda :change(bb1))
bb2=Button(text='',font=('arial',20),width=5,command= lambda :change(bb2))
bb3=Button(text='',font=('arial',20),width=5,command= lambda :change(bb3))
bb4=Button(text='',font=('arial',20),width=5,command= lambda :change(bb4))
bb5=Button(text='',font=('arial',20),width=5,command= lambda :change(bb5))
bb6=Button(text='',font=('arial',20),width=5,command= lambda :change(bb6))
bb7=Button(text='',font=('arial',20),width=5,command= lambda :change(bb7))

bb1.grid(row=1,column=1)
bb2.grid(row=1,column=2)
bb3.grid(row=1,column=3)
bb4.grid(row=1,column=4)
bb5.grid(row=1,column=5)
bb6.grid(row=1,column=6)
bb7.grid(row=1,column=7)

bbb1=Button(text='',font=('arial',20),width=5,command= lambda :change(bbb1))
bbb2=Button(text='',font=('arial',20),width=5,command= lambda :change(bbb2))
bbb3=Button(text='',font=('arial',20),width=5,command= lambda :change(bbb3))
bbb4=Button(text='',font=('arial',20),width=5,command= lambda :change(bbb4))
bbb5=Button(text='',font=('arial',20),width=5,command= lambda :change(bbb5))
bbb6=Button(text='',font=('arial',20),width=5,command= lambda :change(bbb6))
bbb7=Button(text='',font=('arial',20),width=5,command= lambda :change(bbb7))


bbb1.grid(row=2,column=1)
bbb2.grid(row=2,column=2)
bbb3.grid(row=2,column=3)
bbb4.grid(row=2,column=4)
bbb5.grid(row=2,column=5)
bbb6.grid(row=2,column=6)
bbb7.grid(row=2,column=7)

bbbb1=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbb1))
bbbb2=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbb2))
bbbb3=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbb3))
bbbb4=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbb4))
bbbb5=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbb5))
bbbb6=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbb6))
bbbb7=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbb7))


bbbb1.grid(row=3,column=1)
bbbb2.grid(row=3,column=2)
bbbb3.grid(row=3,column=3)
bbbb4.grid(row=3,column=4)
bbbb5.grid(row=3,column=5)
bbbb6.grid(row=3,column=6)
bbbb7.grid(row=3,column=7)

bbbbb1=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbbb1))
bbbbb2=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbbb2))
bbbbb3=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbbb3))
bbbbb4=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbbb4))
bbbbb5=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbbb5))
bbbbb6=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbbb6))
bbbbb7=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbbb7))



bbbbb1.grid(row=4,column=1)
bbbbb2.grid(row=4,column=2)
bbbbb3.grid(row=4,column=3)
bbbbb4.grid(row=4,column=4)
bbbbb5.grid(row=4,column=5)
bbbbb6.grid(row=4,column=6)
bbbbb7.grid(row=4,column=7)

bbbbbb1=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbbbb1))
bbbbbb2=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbbbb2))
bbbbbb3=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbbbb3))
bbbbbb4=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbbbb4))
bbbbbb5=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbbbb5))
bbbbbb6=Button(text='',font=('arial',20),width=5,command=lambda :change(bbbbbb6))
bbbbbb7=Button(text='',font=('arial',20),width=5,command= lambda :change(bbbbbb7))

bbbbbb1.grid(row=5,column=1)
bbbbbb2.grid(row=5,column=2)
bbbbbb3.grid(row=5,column=3)
bbbbbb4.grid(row=5,column=4)
bbbbbb5.grid(row=5,column=5)
bbbbbb6.grid(row=5,column=6)
bbbbbb7.grid(row=5,column=7)

l=Label(text="PUISSANCE 4",font=('arial',40)).place(x=200,y=350)


l=Label(text="mehdi",bg='SystemButtonFace')
tictac.mainloop()
