from tkinter import *

window = Tk()

a=0

def kg_to_3t():
    global a
    if a==1:
        clearValues()
    
    grams = round(float(e1_value.get())*1000)
    t1.insert(END,grams)
    t1.insert(END," grams")
    pounds = round(float(e1_value.get())*2.20462)
    t2.insert(END,pounds)
    t2.insert(END," pounds")
    ounces = round(float(e1_value.get())*35.274)
    t3.insert(END,ounces)
    t3.insert(END," ounces")

    a=1

   
def clearValues():
   t1.delete("1.0",END)
   t2.delete("1.0",END)
   t3.delete("1.0",END)

kg_label = Label(window, text="KG")
kg_label.grid(row=0,column=0)

e1_value = StringVar()
e1=Entry(window, textvariable=e1_value, name="kg")
e1.grid(row=0,column=1)

b2 = Button(window, text="Convert",command=kg_to_3t)
b2.grid(row=0, column=2)  # You can also use pack()

t1=Text(window,height=1, width=20,  )
t1.grid(row=1, column=0)

t2=Text(window,height=1, width=20,  )
t2.grid(row=1, column=1)

t3=Text(window,height=1, width=20,  )
t3.grid(row=1, column=2)

window.mainloop()

"""

 def kg_to_3t():
    miles = float(e1_value.get())*1.6
    t1.insert(END,miles)

b1 = Button(window, text="Execute",command=km_to_miles)
b1.grid(row=0, column=0)  # You can also use pack()


e1_value = StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1, width=20,  )
t1.grid(row=0, column=2)
"""
