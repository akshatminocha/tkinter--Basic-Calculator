from tkinter import *
import math
root=Tk()

root.title('Calculator') 
root.geometry()
e = Entry(root)
e.grid(row=0,column=0,columnspan=6,pady=3)
e.focus_set()

#entry_val=StringVar()
#entry=Entry(root,textvariable=entry_val)
#entry.grid(row=0,column=1,rowspan=2,columnspan=3,padx=20,pady=10)
def getandreplace():
    expression=e.get()
    newtext=expression.replace('/','/')
    newtext=newtext.replace('*','*')
def equals():
    getandreplace()
    expression=e.get()
    newtext=expression.replace('/','/')
    newtext=newtext.replace('*','*')
    try:
        val=eval(newtext)
    except SyntaxError or NameError:
        e.delete(0,END)
        e.insert(0,'Invalid Input!')
    else:
        e.delete(0,END)
        e.insert(0,val)

def squareroot():
    getandreplace()
    expression=e.get()
    newtext=expression.replace('/','/')
    newtext=newtext.replace('*','*')
    try: 
        value= eval(newtext) #evaluate the expression using the eval function
    except SyntaxError or NameErrror:
        e.delete(0,END)
        e.insert(0,'Invalid Input!')
    else:
        sqrtval=math.sqrt(value)
        e.delete(0,END)
        e.insert(0,sqrtval)                      

def square():
    getandreplace()
    expression=e.get()
    newtext=expression.replace('/','/')
    newtext=newtext.replace('*','*')
    try: 
        value= eval(newtext) #evaluate the expression using the eval function
    except SyntaxError or NameErrror:
        e.delete(0,END)
        e.insert(0,'Invalid Input!')
    else:
        sqval=math.pow(value,2)
        e.delete(0,END)
        e.insert(0,sqval)

def clearall(): 
    e.delete(0,END)

def clear1():
    txt=e.get()[:-1]
    e.delete(0,END)
    e.insert(0,txt)    

def action(argi): 
    e.insert(END,argi)


'''def _init(root):
    root.title('Calculator') 
    root.geometry()
    e = Entry(root)
    e.grid(row=0,column=0,columnspan=6,pady=3)
    e.focus_set() #Sets focus on the input text area
'''    
    
    #newdiv=div.decode('utf-8')
'''    
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def sqrt(a):
    return (a**(1/2))
def sqr(a):
    return (a**2)'''
    
#frame=Frame(root)
#frame.grid(row=1,column=0)
'''entry_val=StringVar()
entry=Entry(root,textvariable=entry_val)
entry.grid(row=0,column=1,rowspan=2,columnspan=3,padx=20,pady=10)
'''


button1=Button(root,text="7",height=2,width=5,command=lambda:action(7),bg='sandy brown',font='Times 11 bold',fg='gray10')#fg=foreground colour(for font)
button2=Button(root,text="8",height=2,width=5,command=lambda:action(8),bg='sandy brown',font='Times 11 bold',fg='gray10')
button3=Button(root,text="9",height=2,width=5,command=lambda:action(9),bg='sandy brown',font='Times 11 bold',fg='gray10')
button4=Button(root,text="/",height=2,width=5,command=lambda:action('/'),bg='AntiqueWhite3',font='Times 11 bold',fg='gray10')
button5=Button(root,text="AC",height=2,width=5,command=lambda:clearall(),bg='indian red',font='Times 11 bold',fg='gray10')
button6=Button(root,text="C",height=2,width=5,command=lambda:clear1(),bg='indian red',font='Times 11 bold',fg='gray10')
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=1,column=3)
button5.grid(row=1,column=4)
button6.grid(row=1,column=5)
button7=Button(root,text="4",height=2,width=5,command=lambda:action(4),bg='sandy brown',font='Times 11 bold',fg='gray10')
button8=Button(root,text="5",height=2,width=5,command=lambda:action(5),bg='sandy brown',font='Times 11 bold',fg='gray10')
button9=Button(root,text="6",height=2,width=5,command=lambda:action(6),bg='sandy brown',font='Times 11 bold',fg='gray10')
button10=Button(root,text="*",height=2,width=5,command=lambda:action('*'),bg='AntiqueWhite3',font='Times 11 bold',fg='gray10')
button11=Button(root,text="(",height=2,width=5,command=lambda:action('('),bg='indian red',font='Times 11 bold',fg='gray10')
button12=Button(root,text=")",height=2,width=5,command=lambda:action(')'),bg='indian red',font='Times 11 bold',fg='gray10')
button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
button10.grid(row=2,column=3)
button11.grid(row=2,column=4)
button12.grid(row=2,column=5)

button13=Button(root,text="1",height=2,width=5,command=lambda:action(1),bg='sandy brown',font='Times 11 bold',fg='gray10')
button14=Button(root,text="2",height=2,width=5,command=lambda:action(2),bg='sandy brown',font='Times 11 bold',fg='gray10')
button15=Button(root,text="3",height=2,width=5,command=lambda:action(3),bg='sandy brown',font='Times 11 bold',fg='gray10')
button16=Button(root,text="-",height=2,width=5,command=lambda:action('-'),bg='AntiqueWhite3',font='Times 11 bold',fg='gray10')
button17=Button(root,text="sqrt()",height=2,width=5,command=lambda:squareroot(),bg='indian red',font='Times 11 bold',fg='gray10')
button18=Button(root,text="x^2",height=2,width=5,command=lambda:square(),bg='indian red',font='Times 11 bold',fg='gray10')
button13.grid(row=3,column=0)
button14.grid(row=3,column=1)
button15.grid(row=3,column=2)
button16.grid(row=3,column=3)
button17.grid(row=3,column=4)
button18.grid(row=3,column=5)
button19=Button(root,text="0",height=2,width=5,command=lambda:action(0),bg='sandy brown',font='Times 11 bold',fg='gray10')
button20=Button(root,text=".",height=2,width=5,command=lambda:action('.'),bg='AntiqueWhite3',font='Times 11 bold',fg='gray10')
button21=Button(root,text="%",height=2,width=5,command=lambda:action('%'),bg='AntiqueWhite3',font='Times 11 bold',fg='gray10')
button22=Button(root,text="+",height=2,width=5,command=lambda:action('+'),bg='AntiqueWhite3',font='Times 11 bold',fg='gray10')
button23=Button(root,text="=",height=2,width=11,command=lambda:equals(),bg='lemon chiffon',font='Times 11 bold',fg='gray10')
button19.grid(row=4,column=0)
button20.grid(row=4,column=1)
button21.grid(row=4,column=2)
button22.grid(row=4,column=3)
button23.grid(row=4,column=4,columnspan=2)

#root=Tk()



root.mainloop()