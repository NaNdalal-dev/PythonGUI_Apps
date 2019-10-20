from tkinter import *
from tkinter.ttk import Combobox
from tkinter import LabelFrame
from tkinter import messagebox
w=Tk()
w.title('Temperature converter')
frame=LabelFrame(w,text='Temperature converter',padx=10,pady=10)

def convert():
   try:
       c1 = f1.get()
       c2 = f2.get()
       res1 = combo1.get()
       res2 = combo2.get()
       if (res1 == res2 == 'Select unit:'):
           messagebox.showinfo('Info','Select the temperatue')
       elif(res1==res2):
           con=c1*1
           f2.set(con)
       elif(res1=='CELSIUS °C'and res2=='FAHRENHEIT °F'):
           con=(c1 * 9/5) + 32
           f2.set(con)
       elif (res2 == 'CELSIUS °C' and res1 == 'FAHRENHEIT °F'):
            con1=(c1-32)*(5/9)
            f2.set(con1)
            #(32°F − 32) × 5/9
       elif(res2=='CELSIUS °C' and res1=='KELVIN K'):
           con2=c1-273.15
           f2.set(con2)
       elif (res1 == 'CELSIUS °C' and res2 == 'KELVIN K'):
           con2 = c1 + 273.15
           f2.set(con2)
       elif (res1 == 'FAHRENHEIT °F' and res2 == 'KELVIN K'):
           #(32°F − 32) × 5/9 + 273.15
           con3=(c1-32)*(5/9)+273.15
           f2.set(con3)
       elif (res2 == 'FAHRENHEIT °F' and res1 == 'KELVIN K'):
           #0K − 273.15) × 9/5 + 32 = -459.7°F
           con4=(c1-273.15)*(9/5)+32
           f2.set(con4)
       elif(res1=='CELSIUS °C' and res2=='RANKINE °R'):
           #0°C × 9/5 + 491.67
           con5=c1*(9/5)+491.67
           f2.set(con5)
       elif (res2 == 'CELSIUS °C' and res1 == 'RANKINE °R'):
           #(0°R − 491.67) × 5/9
           con6=c1-491.67*(5/9)
           f2.set(con6)
       elif(res1=='FAHRENHEIT °F' and res2=='RANKINE °R'):
           #32°F + 459.67
           con7=c1+459.67
           f2.set(con7)
       elif (res1 == 'KELVIN K' and res2 == 'RANKINE °R'):
           con8=c1*1.8
           f2.set(con8)

       elif (res2 == 'KELVIN K' and res1 == 'RANKINE °R'):
           #1°R × 5/9
           con9=c1*(5/9)
           f2.set(con9)
       elif(res1=='CELSIUS °C' and res2=='REAUMUE °Re'):
           #C =  Re × 0.8
           con10=c1*.8
           f2.set(con10)
       elif(res2 == 'CELSIUS °C' and res1 == 'REAUMUE °Re'):
           # C =  Re × 1.25
           con11 = c1 * 1.25
           f2.set(con11)
       elif(res1=='FAHRENHEIT °F' and res2=='REAUMUE °Re'):
           #( F - 32) / 2.25
           con12=(c1-32)/2.25
           f2.set(con12)

       elif (res2 == 'FAHRENHEIT °F' and res1 == 'REAUMUE °Re'):
           #Re × 2.25 + 32
           con13=(c1*2.25)+32
           f2.set(con13)
       elif(res1=='RANKINE °R' and res2=='REAUMUE °Re'):
           #( Ra - 32 - 459.67) / 2.25
           con14=(c1-32-459.67)/2.25
           f2.set(con14)
       elif (res2 == 'RANKINE °R' and res1== 'REAUMUE °Re'):
            #Re × 2.25 + 32 + 459.67
           con15 = (c1*2.25+32+459.47)
           f2.set(con15)
       elif(res1=='KELVIN K'and res2=='REAUMUE °Re'):
           con16=c1-273.15*0.8
           #(K - 273.15) × 0.8
           f2.set(con16)
       elif (res2 == 'KELVIN K' and res1 == 'REAUMUE °Re'):
           #Re × 1.25 + 273.15
           con17= (c1*1.25)+273.15
           f2.set(con17)
       elif(res2=='FAHRENHEIT °F'and res1=='RANKINE °R'):
           # Ra - 459.67
           con18=c1-459.67
           f2.set(con18)


       else:
           messagebox.showerror('Error','Check the Conversion')

   except:
       messagebox.showerror('Error','Check the conversion')

temp1=['CELSIUS °C','FAHRENHEIT °F','KELVIN K','RANKINE °R','REAUMUE °Re']
temp2=['CELSIUS °C','FAHRENHEIT °F','KELVIN K','RANKINE °R','REAUMUE °Re']


combo1=Combobox(frame,values=temp1,height=6,width=30)
combo1.set('Select unit:')
combo1.grid(row=0,column=0,columnspan=1,sticky=E)
f1=DoubleVar()
e1=Entry(frame,textvariable=f1,width=30).grid(row=0,column=1)

Label(frame,text='Convert to :',bg='blue',fg='white').grid(row=1,column=1)
combo2=Combobox(frame,values=temp2,height=6,width=30)
combo2.set('Select unit:')
combo2.grid(row=2,column=0,columnspan=1,sticky=E)
f2=DoubleVar()
e2=Entry(frame,textvariable=f2,width=30).grid(row=2,column=1)
buttonget=Button(frame,text='convert',command=convert,activebackground='blue',activeforeground='white').grid(row=3,column=1)

'''
b1=Button(frame,text='1',width=10).grid(row=5,column=0,ipadx=55,sticky=E)
b2=Button(frame,text='2',width=10).grid(row=5,column=1,ipadx=70,sticky=W)
b3=Button(frame,text='3',width=10).grid(row=5,column=2,ipadx=50,sticky=E)
b4=Button(frame,text='4',width=10).grid(row=6,column=0,ipadx=55,sticky=E)
b5=Button(frame,text='5',width=10).grid(row=6,column=1,ipadx=70,sticky=W)
b6=Button(frame,text='6',width=10).grid(row=6,column=2,ipadx=50,sticky=E)
b7=Button(frame,text='7',width=10).grid(row=7,column=0,ipadx=55,sticky=E)
b8=Button(frame,text='8',width=10).grid(row=7,column=1,ipadx=70,sticky=W)
b9=Button(frame,text='9',width=10).grid(row=7,column=2,ipadx=50,sticky=E)
dot=Button(frame,text='.',width=10).grid(row=8,column=0,ipadx=55,sticky=E)
b0=Button(frame,text='0',width=10).grid(row=8,column=1,ipadx=70,sticky=W)
minus=Button(frame,text='+/-',width=10).grid(row=8,column=2,ipadx=50,sticky=E)

'''


frame.grid()
w.geometry('530x140+120+120')
w.mainloop()




