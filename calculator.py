from tkinter import *
calculation=""
def add_to_calculation(symbol):
    global calculation
    calculation +=str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0,calculation)
def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))

        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"ERROR")
def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")
    


window=Tk()
window.title("calculator")

window.geometry("300x275")
text_result=Text(window,height=2,width=16,font=("Arial",24))
text_result.grid(columnspan=5)
text_result.configure(background="lightgreen")

button=Button(window,text="1",command=lambda:add_to_calculation(1),width=5,font=("Arial",14))
button.grid(row=2,column=1)
button2=Button(window,text="2",command=lambda:add_to_calculation(2),width=5,font=("Arial",14))
button2.grid(row=2,column=2)
button3=Button(window,text="3",command=lambda:add_to_calculation(3),width=5,font=("Arial",14))
button3.grid(row=2,column=3)
button4=Button(window,text="4",command=lambda:add_to_calculation(4),width=5,font=("Arial",14))
button4.grid(row=3,column=1)
button5=Button(window,text="5",command=lambda:add_to_calculation(5),width=5,font=("Arial",14))
button5.grid(row=3,column=2)
button6=Button(window,text="6",command=lambda:add_to_calculation(6),width=5,font=("Arial",14))
button6.grid(row=3,column=3)
button7=Button(window,text="7",command=lambda:add_to_calculation(7),width=5,font=("Arial",14))
button7.grid(row=4,column=1)
button8=Button(window,text="8",command=lambda:add_to_calculation(8),width=5,font=("Arial",14))
button8.grid(row=4,column=2)
button9=Button(window,text="9",command=lambda:add_to_calculation(9),width=5,font=("Arial",14))
button9.grid(row=4,column=3)
button0=Button(window,text="0",command=lambda:add_to_calculation(0),width=5,font=("Arial",14))
button0.grid(row=5,column=2)
buttonplus=Button(window,text="+",command=lambda:add_to_calculation("+"),width=5,font=("Arial",14))
buttonplus.grid(row=2,column=4)
buttonmin=Button(window,text="-",command=lambda:add_to_calculation("-"),width=5,font=("Arial",14))
buttonmin.grid(row=3,column=4)
buttonmul=Button(window,text="*",command=lambda:add_to_calculation("*"),width=5,font=("Arial",14))
buttonmul.grid(row=4,column=4)
buttondiv=Button(window,text="/",command=lambda:add_to_calculation("/"),width=5,font=("Arial",14))
buttondiv.grid(row=5,column=4)
buttonopen=Button(window,text="(",command=lambda:add_to_calculation("("),width=5,font=("Arial",14))
buttonopen.grid(row=5,column=1)
buttonclose=Button(window,text=")",command=lambda:add_to_calculation(")"),width=5,font=("Arial",14))
buttonclose.grid(row=5,column=3)
buttonequal=Button(window,text="=",command=lambda:add_to_calculation("="),width=11,font=("Arial",14))
buttonequal.grid(row=6,column=1,columnspan=2)
buttonclear=Button(window,text="C",command=clear_field,width=11,font=("Arial",14))
buttonclear.grid(row=6,column=3,columnspan=2)
buttonequal=Button(window,text="=",command=evaluate_calculation,width=11,font=("Arial",14))
buttonequal.grid(row=6,column=1,columnspan=2)
button2.configure(background="grey")
button3.configure(background="grey")
button4.configure(background="grey")
button6.configure(background="grey")
button7.configure(background="grey")
button8.configure(background="grey")
button9.configure(background="grey")
button0.configure(background="grey")
buttonplus.configure(background="grey")
buttonmin.configure(background="grey")
buttonmul.configure(background="grey")
buttondiv.configure(background="grey")
buttonequal.configure(background="grey")
buttonopen.configure(background="grey")
buttonclose.configure(background="grey")
buttonclear.configure(background="grey")
button.configure(background="grey")
button5.configure(background="grey")

window.mainloop()

